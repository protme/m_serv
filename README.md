# serv00-hysteria2

## 恢复 hysteria2 服务并发送 Telegram 通知

##h2.sh是恢复 hysteria2 文件

### 1，服务器准备
1. **您的服务器需要具有 SSH 连接凭据（用户名、密码或密钥）。**
  - Telegram Bot

2. **创建一个 Telegram Bot 并获取其 API Token。**
  - 获取您的 Telegram 用户或群组的 Chat ID。
3. **GitHub Secrets**
  - 在您的 GitHub 仓库中设置以下 Secrets：
  - ACCOUNTS_JSON：包含所有服务器信息的 JSON 字符串。
  - TELEGRAM_TOKEN：您的 Telegram Bot API Token。
  - TELEGRAM_CHAT_ID：您的 Telegram Chat ID（可以是您的私人聊天或群组）。

### 2，fork本项目
1. **修改 `ACCOUNTS_JSON`**

   在 fork 后的仓库中，用户需要在项目的 Settings -> Secrets 页面添加和配置 `ACCOUNTS_JSON`。

   ```json
   [
       {
           "host": "example1.com",
           "port": 22,
           "username": "user1",
           "password": "password1",
           "cron": "cd ~/domains/$USER.serv00.net/vless && ./check_vless.sh"
       },
       {
           "host": "example2.com",
           "port": 22,
           "username": "user2",
           "password": "password2"
           // 没有cron参数，使用默认命令
       },
       {
           "host": "example3.com",
           "port": 22,
           "username": "user3",
           "password": "password2"
           "uuid": "97f19d62-1345-486a-b6d9-4196d9703548"
           "server_port": "1100"
       }
   ]

   ```

2. **设置 Telegram Secrets**

   用户需要设置并配置他们自己的 Telegram Bot API Token 和 Chat ID 作为 Secrets：
    - `TELEGRAM_TOKEN`：他们的 Telegram Bot API Token。
    - `TELEGRAM_CHAT_ID`：他们的 Telegram Chat ID。

3. **提交修改**

   用户需要将修改后的文件提交到他们 fork 的仓库中，GitHub Actions 将根据定时计划开始运行监控任务。

### 运行和监控

- GitHub Actions 将按照设定的计划（每20分钟一次）运行 `check_vless.yml` 中定义的任务。
- 每次执行将检查服务器 hysteria2 进程的状态，根据需要执行恢复操作，并将结果通过 Telegram 发送通知。

### 注意事项

- 确保在 `ACCOUNTS_JSON` 中正确配置每台服务器的信息，包括主机名、端口、用户名和密码。
- 定期检查 GitHub Actions 的执行结果和 Telegram 的通知，确保服务器状态的监控和恢复工作正常进行。

