import os
import requests


naver_id = os.getenv("NAVER_ID")
naver_secret = os.getenv("NAVER_SECRET") 
url = 'https://openapi.naver.com/v1/papago/n2mt'
text = '안녕하세요'
headers = {'X-Naver-Client-Id': naver_id, 'X-Naver-Client-Secret': naver_secret}

response = requests.post(url, headers=headers, data={'source': 'ko', 'target':'en', 'text':text}).json()
res=response.get('message').get('result').get('translatedText')
print(res)