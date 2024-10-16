import pyrogram
import asyncio
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton

app = Client(
    "My first bot",
    api_id=9070207,
    api_hash= "efbc8ed2f725b47e045e899b5b58cb95",
    bot_token= "6740629779:AAEccQswCAwbjoBESHObnB1HjtsrjMlEJ5k"
)

START_MESSAGE="Hey, Welcome to L-FLIX Subscription Bot"
START_MESSAGE_BUTTONS=[
    [
        InlineKeyboardButton('L-FLIX MAIN', url="https://t.me/katandika2022"), # 1st row 1st button
        InlineKeyboardButton('L-FLIX GROUP', url="https://t.me/katandika2023") # 1st row 2nd button
    
    ],
    [
        InlineKeyboardButton('L-FLIX MOVIES', url="https://t.me/+5iSSwsd5gRNiMjg0"), # 1st row 1st button
        InlineKeyboardButton('L-FLIX SERIES LIST', url="https://t.me/lflix_series_list") # 1st row 2nd button
    
    ]
]

@app.on_message(filters.command('start')&filters.private)
def start (bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        text = text,
        reply_markup =reply_markup,
        disable_web_page_preview = True
    )




app.run()
