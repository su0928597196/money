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
import random

app = Flask(__name__)

line_bot_api = LineBotApi('DAD1pTI6Bgzdrzc3Az2aRrKhX1UJWHW6jeqrPF8S5zOCB8bgw6MezA3DPJ0ywNvvYpsA5WeIc48LmlbrSDxY4hj47ySINwAO/OPLY0squlBS+37InADm61rfCXtNW0H1vcrtwAs7gdYRgaQuROpydQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3822d39b2ed2a8334ec048ae10714b1')


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
    sticker_message = StickerSendMessage(package_id='11537',sticker_id='52002734')
    r = '請按照順序輸入1~5'
    if msg == '謝謝':
        sticker_message = StickerSendMessage(package_id='11537',sticker_id='52002734')
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
    elif msg != '謝謝':
        if '販賣機' in msg:
            r = '您想知道甚麼?  自動販賣機功能,請輸入1; 零件介紹,請輸入2; 學習板介紹,請輸入3'
        elif '自動' in msg:
            r = '您想知道甚麼?  自動販賣機功能,請輸入1; 零件介紹,請輸入2; 學習板介紹,請輸入3'
        elif '專題' in msg:
            r = '您想知道甚麼?  專題內容請按4; 專題圖片請按5; 專題影片請按6'
        elif msg == '1':
            r = '當程式運作時,步進馬達會旋轉,使上頭的鐵絲也跟著旋轉,最後架上的商品就會掉下來'
        elif msg == '2':
            r = '步進馬達:利用程式碼能控制旋轉次數,也能用可變電阻來控制它的旋轉ˇ'
        elif msg == '3':
            r = ''
            image_message = ImageSendMessage(
            original_content_url='https://direct.nuvoton.com/207-thickbox_default/learning-board-of-nuc140-series.jpg',
            preview_image_url='https://direct.nuvoton.com/207-thickbox_default/learning-board-of-nuc140-series.jpg')
        
        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()