import os
import requests
from bs4 import BeautifulSoup

# 1. 토큰 및 url 설정
token = os.getenv('TELEGRAM_TOKEN')
#api_url = 'https://api.telegram.org'
api_url = 'https://api.hphk.io/telegram'

# 2. 사용자 ID
url = f'{api_url}/bot{token}/getUpdates'
print(url)
response = requests.get(url).json()
response.get("result")
chat_id = response.get('result')[0].get('message').get('from').get('id')

# 3. 보낼 내용 만들기

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

test1 = soup.select(".tit")
test2 = soup.select(".sale")
nation = []
sale = []
for i in test1:
    i = i.text
    i = i.strip()
    nation.append(i)
for j in test2:
    j = j.text
    sale.append(j)
text = '\n'.join(nation)

# 4. 메세지 보내기
url = f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(url)