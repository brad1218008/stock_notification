from fastapi import Request,APIRouter
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent
import os

router = APIRouter()

line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))


@router.post("/webhook")
async def webhook(request: Request):
    signature = request.headers.get('X-Line-Signature')
    body = await request.body()
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        return 'Invalid signature'

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    reply_text = f"You said: {text}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))


@handler.add(FollowEvent)
def handle_follow(event):
    user_id = event.source.user_id
    print(f"User follow! user_id: {user_id}")


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    user_id = event.source.user_id
    print(f"User leave! user_id: {user_id}")