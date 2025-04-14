import requests
import json

# 配置信息
API_URL = "https://aihub.cuc.edu.cn/console/v1/chat/completions"
API_KEY = "这里填写你的API-KEY"
MODEL_NAME = "DeepSeek-R1-Distill-Qwen-32B"

def deepseek_chat(messages, stream=False):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": stream
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, stream=stream, timeout=30)
        response.raise_for_status()
        return response if stream else response.json()
    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        return None

def process_stream_response(response):
    reasoning_buffer = []
    content_buffer = []
    stage = 0  # 0:等待思考过程 1:思考过程进行中 2:回复内容进行中
    
    print("\n思考过程：", end="", flush=True)
    
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8').strip()
            if decoded_line.startswith('data:'):
                try:
                    chunk = json.loads(decoded_line[5:])
                    delta = chunk["choices"][0].get("delta", {})
                    
                    # 处理思考过程
                    if "reasoning_content" in delta:
                        reasoning = delta["reasoning_content"]
                        reasoning_buffer.append(reasoning)
                        print(reasoning, end="", flush=True)
                        stage = 1
                        
                    # 处理正式回复
                    if "content" in delta:
                        if stage < 2:
                            print("\n\n助手：", end = "", flush=True)
                            stage = 2
                        content = delta["content"]
                        content_buffer.append(content)
                        print(content, end="", flush=True)
                        
                except json.JSONDecodeError:
                    continue
    print("\n")
    return "".join(reasoning_buffer), "".join(content_buffer)

def process_normal_response(response):
    result = response
    message = result["choices"][0]["message"]
    return message.get("reasoning_content", ""), message.get("content", "")

if __name__ == "__main__":
    print("DeepSeek 聊天助手（输入'退出'、'quit'或者'exit'结束对话）")
    
    # 模式选择
    while True:
        mode = input("请选择模式 (1-普通模式 / 2-流式模式)：").strip()
        if mode in ["1", "2"]:
            stream_mode = mode == "2"
            break
        print("输入无效，请重新选择")

    # 维护对话历史
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    while True:
        try:
            user_input = input("\n你：").strip()
            if user_input.lower() in ["退出", "exit", "quit"]:
                break
                
            messages.append({"role": "user", "content": user_input})
            
            if stream_mode:
                print("思考中...", end="\r", flush=True)
                response = deepseek_chat(messages, stream=True)
                if response:
                    reasoning, content = process_stream_response(response)
                    messages.append({"role": "assistant", "content": content})
            else:
                print("思考中...", end="\r", flush=True)
                response = deepseek_chat(messages)
                if response:
                    reasoning, content = process_normal_response(response)
                    print(f"\n思考过程：{reasoning}")
                    print(f"\n助手：{content}")
                    messages.append({"role": "assistant", "content": content})
                
        except KeyboardInterrupt:
            print("\n对话已终止")
            break
