# 中国传媒大学 DeepSeek API 使用手册

「测试」第一版：2025 年 04 月 11 日

「测试」第二版：2025 年 04 月 14 日

<u>**特别注意：中国传媒大学API仅可以在学校网络环境下调用，请确保在操作前连接学校网络，否则API将无法使用！**</u>

### 一、在 Windows 下使用 curl 直接调用

#### 步骤一：检查系统中的 curl 工具

- **安装之前请先检查您的电脑中是否自带 curl 工具**
  
  以 Windows 11 为例，按住电脑键盘上的 `Windows` 和 `R` 按键，弹出 “运行” 窗口。
  
  在窗口中输入 `cmd` 并按回车键，打开 CMD 控制台。
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-49-03-image.png)
  
  在弹出的窗口中输入 `curl --help` 。
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-49-53-image.png)
  
  如果您的电脑有与上图类似的输出，则表示 curl 工具已经正常安装。否则**请参考下面的安装流程**：[https://zhuanlan.zhihu.com/p/447058975/]()

#### 步骤二：调用校园 DeepSeek API

- **构造请求命令**  
  复制以下命令，将 `{API-KEY}` 替换为学校提供的 Key（删除花括号，格式为 `Bearer sk-xxxxxxxx`），并填入 CMD 控制台中。
  
  **<u>特别注意：由于Windows规范，该命令与 Linux 环境下的命令有些许差异！</u>**
  
  ```plaintext
  curl -X POST "https://aihub.cuc.edu.cn/console/v1/chat/completions" -H "Content-Type: application/json" -H "Authorization: Bearer {API-KEY}" -d "{\"model\": \"DeepSeek-R1-Distill-Qwen-32B\", \"messages\": [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"你好\"}], \"stream\": false}"
  ```

- **示例响应**  
  成功调用后，控制台显示包含 `content`（正式回答）和 `reasoning_content`（思考过程）的响应：
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-17-54-image.png)

- **自定义消息内容**  
  修改 `system` 或 `user` 字段内容（如设置日语机器人），响应结果中 `content` 会按规则返回：
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-18-44-image.png)

### 二、在 Linux 下使用 curl 直接调用

#### 注意

**<u>本方法操作较为复杂，且对用户有一定的 Linux 操作要求，建议排查问题时使用本方法，不推荐日常使用。</u>**

#### 步骤一：切换系统软件源（推荐使用清华大学软件源）

1. **获取管理员权限**  
   打开系统终端，输入 `su` 并输入管理员密码，获取管理员权限：
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-45-48-image.png)

2. **选择系统对应的软件源**
   以 Debian 12 为例，访问清华大学软件源文档： [debian | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/debian/)。  
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-45-53-image.png)

3. **编辑软件源配置文件**  
   在终端输入 `sudo vim /etc/apt/sources.list`，使用 vim 编辑器打开文件，按 `i` 键进入编辑模式。

4. **替换软件源内容**  
   根据系统版本，从清华源文档复制对应软件源，注释原有内容并粘贴新源（示例如下）：
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-45-58-image.png)

5. **保存并退出**  
   按 `ESC` 键退出编辑模式，输入 `:wq!` 保存并退出。

#### 步骤二：安装 curl 工具包

1. **更新软件包列表并升级**  
   输入 `sudo apt update` 和 `sudo apt upgrade`，按提示输入 `y` 确认。

2. **安装 curl**  
   输入 `sudo apt-get install curl`，等待下载并确认安装，成功后显示如下（示例）：
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-46-04-image.png)

#### 步骤三：调用校园 DeepSeek API

- **构造请求命令**  
  复制以下命令，将 `{API-KEY}` 替换为学校提供的 Key（删除花括号，格式为 `Bearer sk-xxxxxxxx`）：
  
  ```plaintext
  curl -X POST 'https://aihub.cuc.edu.cn/console/v1/chat/completions' -H 'Content-Type: application/json' -H 'Authorization: Bearer {API-KEY}' -d '{"model": "DeepSeek-R1-Distill-Qwen-32B", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "你好"}], "stream": false}'  
  ```

- **示例响应**  
  成功调用后，终端显示包含 `content`（正式回答）和 `reasoning_content`（思考过程）的响应：
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-46-15-image.png)

- **自定义消息内容**  
  修改 `system` 或 `user` 字段内容（如设置日语机器人），响应结果中 `content` 会按规则返回：
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-46-22-image.png)

### 三、编写 Python 脚本进行连续对话

#### 环境准备

1. **使用VSCode代码编辑器编写代码**
   
   首先安装 Python ，从官网选择适合您系统版本的 Python 软件并安装到本地。
   
   ```url
   https://www.python.org/downloads/
   ```
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-19-49-image.png)
   
   然后打开 VSCode 官网，选择适合您系统版本的代码编辑器并安装到本地。
   
   ```url
   https://code.visualstudio.com/
   ```
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-20-20-image.png)
   
   您可以打开 VSCode 并在左侧插件栏目搜索 `Chinese` ，下载并安装汉化插件。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-21-13-image.png)
   
   安装完成之后重启 VSCode ，即可使用汉化的开发环境。

2. **配置 Python 清华源**
   
   打开 VSCode ，打开一个项目文件夹，准备编写 Python 代码。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-21-49-image.png)
   
   点击右上角的 “切换面板” 按钮，弹出下方的终端界面。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-22-20-image.png)
   
   在终端中分别粘贴下面两行代码，将PYPI源切换到清华大学镜像站。
   
   ```plaintext
   python -m pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --upgrade pip  
   ```
   
   ```plaintext
   pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
   ```
   
   *（对于高级用户：在 Linux 环境下，若提示缺少 pip，请先执行 `sudo apt-get install python3-pip` ，如果 pip 命令无法直接安装库，请切换到 `venv` 环境）*

3. **安装 requests 库**
   
   在终端中输入下面的命令，安装`requests`库。
   
   ```plaintext
   pip install requests
   ```
   
   如果终端中显示如下结果，则表示安装成功。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-26-06-image.png)

#### 编写脚本

- **代码模板**  
  
  您可以通过以下网址下载示例代码（需替换 `API-KEY` ）：
  
  ```url
  https://github.com/VALONSIDE/CUC-API/
  ```
  
  点击右上角的 `Code` ，然后点击 `Download ZIP` 。
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-27-57-image.png)
  
  如果您无法下载，您也可以新建 Python 文件，复制以下代码（需替换 `API-KEY` ）：
  
  ```python
  import requests
  import json
  
  # 配置信息
  API_URL = "https://aihub.cuc.edu.cn/console/v1/chat/completions"
  API_KEY = "这里替换成你的API-KEY"
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
                              print("\n\n助手：", end="", flush=True)
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
  ```

#### 运行脚本

1. **选择模式**  
   点击右上角小三角启动按钮启动脚本，启动后选择 `1 - 普通模式`（完整输出）或 `2 - 流式模式`（逐字输出）。您可以输入数字`1`或`2`，并按回车键确认选择。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-30-30-image.png)
   
   `普通模式` 就是在提问后将思考过程和结果**一次性提供**，您可能需要等待一小段时间才能看到生成结果。下面是 “普通模式” 的使用示例：
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-31-58-image.png)
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-32-12-image.png)
   
   `流式模式` 则是在提问后将思考过程和结果**逐字输出**，您可以立即看见人工智能的输出过程。下面是 “流式模式” 的使用示例：
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-31-10-image.png)

2. **开始对话**  
   出现 `你:` 提示后，您可以输入问题，并按回车键发送，程序自动维护对话历史。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-32-12-image.png)
   
   若您对话完成，您可以输入 “结束” 或者 “quit” 并按回车来结束程序。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-32-29-image.png)

### 四、使用 Postman 进行可视化调用

#### 步骤一：下载并解压 Postman

1. 以 Debian 12 为例，从官网 https://www.postman.com/downloads/ 下载适合版本。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-47-08-image.png)

2. 解压下载的 tar.gz 包。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-47-12-image.png)

3. 启动 Postman 。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-47-15-image.png)

#### 步骤二：配置请求参数

1. **新建 HTTP 请求**  
   点击 “File→New→HTTP”，将请求方法设为 POST 。
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-47-55-image.png)
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-47-58-image.png)

2. **设置 Headers**  
   添加两个 Key-Value 对：
   
   - `Content-Type: application/json`
   - `Authorization: Bearer 你的API-KEY`（注意 Bearer 后有空格）  
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-08-39-14-image.png)
   
   **<u>这里填写的时候请格外注意，在标签栏中选择选择 `Headers` ，千万不要填写到 `Params` 里面！</u>**

3. ```json
   {
     "model": "DeepSeek-R1-Distill-Qwen-32B",
     "messages": [
       {"role": "system", "content": "你是一个智能助手"},
       {"role": "user", "content": "你好"}
     ],
     "stream": false
   }
   ```
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-48-09-image.png)

4. 在上方的地址栏输入下面的API地址。
   
   ```url
   https://aihub.cuc.edu.cn/console/v1/chat/completions
   ```
   
   ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-48-21-image.png)

#### 步骤三：发送请求并查看结果

- 点击 “Send“ ，查看下方显示响应内容，确认操作是否正确：
  
  ![](C:\Users\VALON\AppData\Roaming\marktext\images\2025-04-15-07-48-32-image.png)
