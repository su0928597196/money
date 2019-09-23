from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('uNz4WmN6Ekhi32V+6397AVeQE03bSJU8k4RQ4FV9t6ZwDWYywABuNmT1255mwMSmYpsA5WeIc48LmlbrSDxY4hj47ySINwAO/OPLY0squlAOketT4DqfmS7zofY80u6rxFKCbdsO5biFey/2E7/OVAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dab6186a76822a5207cb032d59caa752')


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
    
    if msg == '安靜':
        n = 1
    elif msg == '說話':
        n = 0
    r = '媽媽說好的獎學金呢'
    if n != 1:
        if msg in ['不', '沒有', '想太多']:
            r = '說話不算話,週日我不去了'
        elif msg in ['好', '好啦', '會給你']:
            r = '好,下次我會幫忙顧婆婆的'
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    elif n == 1:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='好喔!'))




if __name__ == "__main__":
    app.run()