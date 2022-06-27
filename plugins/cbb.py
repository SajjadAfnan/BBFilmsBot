#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG, BARBAROSLAR2, ALPARSLAN2, START_MSG
from translation import INSTAGRAM, SHARE_LINK, UYANIS, ERTUGRUL720, ERTUGRUL360, KUTUL_AMARE, PAYITAHT, PAYITAHT1, PAYITAHT2, PAYITAHT3, PAYITAHT4, PAYITAHT5, PAYITAHT, ALPARSLAN, BARBAROSLAR, BARBAROSLAR1, ALPARSLAN1, YUNUS_EMRE, YUNUS_EMRE1, YUNUS_EMRE2
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    demovideo = "https://t.me/How_To_Use_Bot/39"
    if data == "series":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/37",
            caption = START_MSG,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                       InlineKeyboardButton("Yunus Emre", callback_data = "yunusemre"),
                    ],
                    [
                       InlineKeyboardButton("Diriliş Ertuğrul", callback_data = "ertugrul"),
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
        
        
    elif data == "alparslan":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/46",
            caption = ALPARSLAN,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🐺 Season 1 🐺', callback_data = "alparslan1"),
                    ],
                    [
                        InlineKeyboardButton("🐺 Season 2 🐺", callback_data = "alparslan2"),
                    ],
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "barbaroslar":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/47",
            caption = BARBAROSLAR,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('⚓ Season 1 ⚓', callback_data = "alparslan1"),
                    ],
                    [
                        InlineKeyboardButton("⚓ Season 2 ⚓", callback_data = "alparslan2"),
                    ],
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "yunusemre":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/48",
            caption = YUNUS_EMRE,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🕌 Season 1 🕌', callback_data = "yunusemre1"),
                    ],
                    [
                        InlineKeyboardButton("🕌 Season 2 🕌", callback_data = "yunusemre2"),
                    ],
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "ertugrul":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/15",
            caption = f"<b>[BB] Dirilis Ertugrul\nWith English subtitle ✅\nAll 360p and 720p Quality (SD, HD)🔥</b>",
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💡 720p HD (45 mins) 💡', callback_data = "ertugrul720p"),
                    ],
                    [
                        InlineKeyboardButton("💡 360p SD (2.5 Hrs) 💡", callback_data = "ertugrul360p"),
                    ],
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/13",
            caption = PAYITAHT,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💡 Season 𝟏 💡", callback_data = "payitaht1"),
                        InlineKeyboardButton("💡 Season 𝟐 💡", callback_data = "payitaht2")
                    ],
                    [
                        InlineKeyboardButton("💡 Season 𝟑 💡", callback_data = "payitaht3"),
                        InlineKeyboardButton("💡 Season 𝟒 💡", callback_data = "payitaht4")
                    ],
                    [
                        InlineKeyboardButton("💡 Season 𝟓 💡", callback_data = "payitaht5")
                    ],
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "uyanis":
        await query.message.reply_video(
            video = demovideo,
            caption = UYANIS.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "series"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "yunusemre1":
        await query.message.reply_video(
            video = demovideo,
            caption = YUNUS_EMRE1.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "yunusemre"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "yunusemre2":
        await query.message.reply_video(
            video = demovideo,
            caption = YUNUS_EMRE2.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "yunusemre"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "alparslan1":
        await query.message.reply_video(
            video = demovideo,
            caption = ALPARSLAN1.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "alparslan"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass
        
    elif data == "alparslan2":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/46",
            caption = ALPARSLAN2.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "alparslan"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass
        
    elif data == "kutulamare":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/20",
            caption = KUTUL_AMARE.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⏪ Back", callback_data = "series"),
                            InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "barbaroslar1":
        await query.message.reply_video(
            video = demovideo,
            caption = BARBAROSLAR1.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "barbaroslar"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass
        
    elif data == "barbaroslar2":
        await query.message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/47",
            caption = BARBAROSLAR2.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "barbaroslar"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass
        
    elif data == "ertugrul360p":
        await query.message.reply_video(
            video = demovideo,
            caption = ERTUGRUL360.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                     [
                        InlineKeyboardButton("⏪ Back", callback_data = "ertugrul"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "ertugrul720p":
        await query.message.reply_video(
            video = demovideo,
            caption = ERTUGRUL720.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("⏪ Back", callback_data = "ertugrul"),
                       InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
               ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht1":
        await query.message.reply_video(
            video = demovideo,
            caption = PAYITAHT1.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "payitaht"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht2":
        await query.message.reply_video(
            video = demovideo,
            caption = PAYITAHT2.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "payitaht"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht3":
        await query.message.reply_video(
            video = demovideo,
            caption = PAYITAHT3.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "payitaht"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht4":
        await query.message.reply_video(
            video = demovideo,
            caption = PAYITAHT4.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "payitaht"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
                    ]
                ]
            )
        )
        try:
            await query.message.delete()
        except:
            pass

    elif data == "payitaht5":
        await query.message.reply_video(
            video = demovideo,
            caption = PAYITAHT5.format(botusername = client.username),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⏪ Back", callback_data = "payitaht"),
                        InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM)
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
