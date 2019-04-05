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
import os
import random

app = Flask(__name__)

# LINE Access Token
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# LINE Channel Secret
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    you = ['fuck', 'thank', 'kill', 'nice to meet']
    shit = ['holy', 'bull', 'oh']
    circle = ['円周率', 'えんしゅうりつ', 'エンシュウリツ', 'π']
    michael = 'マイケル'
    under_michael = ['ジャクソン', 'ジョーダン', 'サンデル',
                     'シェンカー', 'オーウェン', '富岡', '1枚、2枚、３マイケル']
    nenshu = '私の年収'
    keiba = '競馬予想'
    keiba_kekka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    reply_commic = ['うしおととら', 'からくりサーカス', 'エルフェンリート',
                    '最終兵器彼女', 'ジョジョの二部', 'GANTZ', 'バジリスク']
    reply_movie = ['メメント', 'ファイトクラブ', 'ハングオーバー', 'ララランド', 'デッドプール', 'SEVEN']

    event_text = event.message.text

    if event_text in you:
        text = 'you!'
    elif event_text in shit:
        text = 'shit!'
    elif event_text in circle:
        text = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'
    elif event_text in michael:
        text = random.choice(under_michael)
    elif event_text in nenshu:
        text = '低すぎ'
    elif event_text in keiba:
        text = str(random.choice(keiba_kekka)) + '番の馬が一着です。'
    elif 0 <= event_text.find('漫画') or 0 <= event_text.find('マンガ'):
        text = 'おすすめの漫画は ' + random.choice(reply_commic) + ' です。'
        elif 0 <= event_text.find('映画')
        text = 'おすすめの映画は ' + random.choice(reply_movie) + ' です。'
    elif list(event_text)[-1] in ['?', '？']:
        text = 'すみません。よくわかりません。'
    else:
        text = event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text))


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
