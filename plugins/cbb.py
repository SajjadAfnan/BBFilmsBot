#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from translation import INSTAGRAM, SHARE_LINK, UYANIS, ERTUGRUL720, ERTUGRUL360, KUTUL_AMARE, PAYITAHT, PAYITAHT1, PAYITAHT2, PAYITAHT3, PAYITAHT4, PAYITAHT5, PAYITAHT, BARBAROSLAR1, ALPARSLAN1
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    demovideo = "https://t.me/How_To_Use_Bot/39"
    if data == "series":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/37",
            caption = START1,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                       InlineKeyboardButton("Diriliş Ertuğrul ", callback_data = "ertugrul"),
                    ],
                    [
                       InlineKeyboardButton("Payitaht Abdülhamid", callback_data = "payitaht"),
                    ],
                    [
                       InlineKeyboardButton("Mehmetçik Kutul Amare", callback_data = "kutulamare"),
                    ],
                    [
                       InlineKeyboardButton("Uyanış: Buyuk Selcuklu", callback_data = "uyanis"),
                    ],
                    [
                       InlineKeyboardButton("Alparslan: Buyuk Selcuklu", callback_data = "alparslan"),
                    ],
                    [
                       InlineKeyboardButton("Barbaroslar: Akdeniz'in Kilici", callback_data = "barbaroslar"),
                    ],
                    [
                       InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM),
                       InlineKeyboardButton('Share to Friends', url= SHARE_LINK)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass
        
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
