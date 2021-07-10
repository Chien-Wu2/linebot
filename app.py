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

line_bot_api = LineBotApi('XUGAssvIbIfQFbYG6dAWNm7AffB9/LK31jHBH09Ge8tZZqWAJFKVmrGQ2S4GfQMM73p7lVM6HZP9K/u1fJam8rV0F5B2EslaUCPu1CIo+2qnMqGiyl+C5xikZeaUZW1JRIVWmnwZ7PAYBp7yRelNiwdB04t89/1O/w1cDnyilFU=')
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
    r = '喔好喔'

    if '吃飽' in msg:
        r = '吃飽了'
    elif '米雪' in msg:
        r = '米雪好可愛'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()