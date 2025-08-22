import requests

EITA_BOT_TOKEN = 'bot157749:2e2fd8ce-cfea-4e3e-b4c6-5171e7fdb817'  # replace with your Eita bot token
CHAT_ID = '10777380'                 # replace with your chat ID
text = 'hi'

url = f'https://eitaayar.ir/api/{EITA_BOT_TOKEN}/sendMessage'
params = {
    'chat_id': CHAT_ID,
    'text': text
}

try:
    response = requests.get(url, params=params, timeout=10)  # 10 seconds timeout
    print('Status Code:', response.status_code)
    print('Response:', response.json())
except requests.Timeout:
    print("Request timed out.")
except Exception as e:
    print("Request failed:", e)
