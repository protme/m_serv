import os
import json
import subprocess
import requests

def send_telegram_message(token, chat_id, message):
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
    telegram_payload = {
        "chat_id": chat_id,
        "text": message,
        "reply_markup": '{"inline_keyboard":[[{"text":"问题反馈❓","url":"https://t.me/yxjsjl"}]]}'
    }

    response = requests.post(telegram_url, json=telegram_payload)
    print(f"Telegram 请求状态码：{response.status_code}")
    print(f"Telegram 请求返回内容：{response.text}")

    if response.status_code != 200:
        print("发送 Telegram 消息失败")
    else:
        print("发送 Telegram 消息成功")

# 从环境变量中获取密钥
accounts_json = os.getenv('ACCOUNTS_JSON')
telegram_token = os.getenv('TELEGRAM_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

# 检查并解析 JSON 字符串
try:
    servers = json.loads(accounts_json)
except json.JSONDecodeError:
    error_message = "ACCOUNTS_JSON 参数格式错误"
    print(error_message)
    send_telegram_message(telegram_token, telegram_chat_id, error_message)
    exit(1)

# 初始化汇总消息
summary_message = "serv00-hysteria2 恢复操作结果：\n"

# 默认恢复命令
Run echo "#!/bin/bash" > sshpass.sh
echo "#!/bin/bash" > sshpass.sh
while IFS= read -r account; do
  username=$(echo "$account" | jq -r '.username')
  *** "$account" | jq -r '.password')
  ssh=$(echo "$account" | jq -r '.ssh')

  echo "echo \"Executing for $username@$ssh\"" >> sshpass.sh***0m
  echo "sshpass -p '$password' ssh -o StrictHostKeyChecking=no 'helloolk@$ssh' 'curl -s https://raw.githubusercontent.com/eooce/scripts/master/containers-shell/00-hy2.sh | PORT=10308 bash'" >> sshpass.sh***0m
  echo "sshpass -p '$password' ssh -o StrictHostKeyChecking=no 'helloook@$ssh' 'curl -s https://raw.githubusercontent.com/eooce/scripts/master/containers-shell/00-hy2.sh | PORT=46304 bash'" >> sshpass.sh***0m
done < <(jq -c '.***' accounts.json)***0m
chmod +x sshpass.sh***0m
shell: /usr/bin/bash -e {0}
##***endgroup***

# 遍历服务器列表并执行恢复操作
for server in servers:
    host = server['host']
    port = server['port']
    username = server['username']
    password = server['password']
    cron_command = server.get('cron', default_restore_command)

    print(f"连接到 {host}...")

    # 执行恢复命令（这里假设使用 SSH 连接和密码认证）
    restore_command = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no -p {port} {username}@{host} '{cron_command}'"
    try:
        output = subprocess.check_output(restore_command, shell=True, stderr=subprocess.STDOUT)
        summary_message += f"\n成功恢复 {host} 上的 hysteria2 服务：\n{output.decode('utf-8')}"
    except subprocess.CalledProcessError as e:
        summary_message += f"\n无法恢复 {host} 上的 hysteria2 服务：\n{e.output.decode('utf-8')}"

# 发送汇总消息到 Telegram
send_telegram_message(telegram_token, telegram_chat_id, summary_message)
