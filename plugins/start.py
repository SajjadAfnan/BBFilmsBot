#(©)CodeXBotz
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from translation import INSTAGRAM, SHARE_LINK, START_LOG
from helper_func import subscribed, encode, decode, get_messages
from database.sql import add_user, query_msg, full_userbase


#=====================================================================================##

WAIT_MSG = """<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM),
                      InlineKeyboardButton('Share to Friends', url= SHARE_LINK)]]
                )
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, protect_content=PROTECT_CONTENT, parse_mode = 'html', caption = caption, reply_markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM),
                      InlineKeyboardButton('Share to Friends', url= SHARE_LINK)]])
                )
                await asyncio.sleep(0.5)
                await msg.copy(chat_id=-1001770753985, caption = caption + f"\n\n" + START_LOG.format(username = None if not message.from_user.username else '@' + message.from_user.username,mention = message.from_user.mention,id = message.from_user.id))
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, protect_content=PROTECT_CONTENT, parse_mode = 'html', caption = caption, reply_markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM),
                      InlineKeyboardButton('Share to Friends', url= SHARE_LINK)]]))
                await msg.copy(chat_id=-1001770753985, caption = caption + f"\n\n" + START_LOG.format(username = None if not message.from_user.username else '@' + message.from_user.username,mention = message.from_user.mention,id = message.from_user.id))
            except:
                pass
        try:
            await message.reply_video(
            video = "https://t.me/How_To_Use_Bot/40",
            caption = f"<b>Restarting Bot</b>",
            reply_markup = InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("🟢 Restart Bot 🟢", callback_data = "series")
                       ]
                   ]
               )
            )
        except:
            pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                    [
                       InlineKeyboardButton("𝟏. Yunus Emre", callback_data = "yunusemre"),
                       InlineKeyboardButton("𝟐. Diriliş Ertuğrul", callback_data = "ertugrul"),
                    ],
                    [
                       InlineKeyboardButton("𝟑. Payitaht Abdülhamid", callback_data = "payitaht"),
                    ],
                    [
                       InlineKeyboardButton("𝟓. Uyanış: Buyuk Selcuklu", callback_data = "uyanis"),
                    ],
                    [
                       InlineKeyboardButton("𝟒. Mehmetçik Kutul Amare", callback_data = "kutulamare"),
                    ],
                    [
                       InlineKeyboardButton("𝟔. Alparslan: Buyuk Selcuklu", callback_data = "alparslan"),
                    ],
                    [
                       InlineKeyboardButton("𝟕. Barbaroslar: Akdeniz'in Kilici", callback_data = "barbaroslar"),
                    ],
                    [
                       InlineKeyboardButton('Follow Instagram 🤍', url= INSTAGRAM),
                       InlineKeyboardButton('Share to Friends', url= SHARE_LINK)
                    ]
            ]
        )
        await message.reply_photo(
            photo = "https://t.me/How_To_Use_Bot/37",
            caption = START_MSG,
            reply_markup = reply_markup,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for row in query:
            chat_id = int(row[0])
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
