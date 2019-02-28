import os
import pprint
import random
from flask import Flask, request
import requests

token = os.getenv('TELEGRAM_TOKEN')
#api_url = 'https://api.telegram.org'
api_url = 'https://api.hphk.io/telegram'

webhook_url = f'https://python-email-ado119.c9users.io/{token}'
url = f'{api_url}/bot{token}/setWebhook?url={webhook_url}'
print(url)

app = Flask(__name__)
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 요청
    req = request.get_json()
    pprint.pprint(req)
    
    # 2. 처리 (text는 메시지, reply 답장 메시기)
    if req.get('message') is not None:
        reply = '수행할 수 없는 명령어 입니다.'
        text = req.get('message').get('text')
        if "로또" in text or 'lotto' in text:
            reply = sorted(random.sample(range(1,46), 6))        
        elif '/번역 ' == text[0:4]:
            naver_id = os.getenv("NAVER_ID")
            naver_secret = os.getenv("NAVER_SECRET") 
            url = 'https://openapi.naver.com/v1/papago/n2mt'
            headers = {'X-Naver-Client-Id': naver_id, 'X-Naver-Client-Secret': naver_secret}
            response = requests.post(url, headers=headers, data={'source': 'ko', 'target':'en', 'text':text[4:]}).json()
            translated = response.get('message').get('result').get('translatedText')
            reply = f'번역결과 입니다. \n{translated}'
        
            
    # 3. 답장
        chat_id = req.get('message').get('from').get('id')
        send_url = f'{api_url}/bot{token}/sendMEssage?chat_id={chat_id}&text={reply}'
        requests.get(send_url)
        
    return '', 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    