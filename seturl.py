import os

token = os.getenv('TELEGRAM_TOKEN')
option = int(input('''
원하는 환경을 입력하세요.
1 : c9
2 : heroku
'''))
if option == 1:
    webhook_url = f'https://python-email-ado119.c9users.io/{token}'
elif option == 2:
    webhook_url = f'https://telegram-bot-ado119.herokuapp.com/{token}'

#api_url = 'https://api.telegram.org'
api_url = 'https://api.hphk.io/telegram'

url = f'{api_url}/bot{token}/setWebhook?url={webhook_url}'

print(url)