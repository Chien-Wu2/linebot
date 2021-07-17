import random

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('PL1+o8xLBxFIWv3Z2w46FNerJFE6VFTweC9Uh5rFySX2IxE2kldDZBtu+p/D6ovF73p7lVM6HZP9K/u1fJam8rV0F5B2EslaUCPu1CIo+2q/xn1inXVeH17pwH+JcHHlgyZWvKTybloaOcSCQ9V90AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6a8ab0a64495a9ecec6971e1faa9ee9c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = msg

    with open('answer.txt','r',encoding='utf8')as f:
        for line in f: 
            s = line.strip().split(',')
            keyword = s[0]
            answer = s[1]
            
            if keyword in msg:
                r = answer
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = r))

               
    x = random.randint(0,9)
    p =[]
    with open('stk.txt','r',encoding='utf8') as f:
        for line in f: 
            pac,sti = line.strip().split(',')
            p.append([pac,sti])

            sticker_message = StickerSendMessage(
            package_id='f[x][0]',
            sticker_id='[x][1]'
            )
            line_bot_api.reply_message(
            event.reply_token,
            sticker_message)


                


if __name__ == "__main__":
    app.run()
