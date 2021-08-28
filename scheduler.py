from flask import Flask, request, abort
import os

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

LINE_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
USER_ID = os.environ["USER_ID"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main():
    pushText = TextSendMessage(text="これは定期実行だ。設定されている時間に届いているかい？")
    line_bot_api.push_message(USER_ID, messages=pushText)


if __name__ == "__main__":
    main()
