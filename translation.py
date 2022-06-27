import os
import logging
from logging.handlers import RotatingFileHandler

INSTAGRAM = """https://instagram.com/BB_Films_Updates"""

SHARE_LINK = """https://t.me/share/url?url=instagram.com%2FBB_Films_Updates%0A%0AFollow%20the%20above%20Instagram%20page%20to%20get%20all%20official%20Updates%20about%20Barbaroslar%20Akdeniz%27in%20Kilici%20%26%20Alparslan%20B%C3%BCy%C3%BCk%20Sel%C3%A7uklu%0A%0AIf%20the%20current%20bot%20gets%20copyright%2C%20then%20new%20bot%20link%20will%20publish%20on%20the%20above%20Instagram%20page%20Bio%20%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%0A%0Ainstagram.com%2FBB_Films_Updates%0Ainstagram.com%2FBB_Films_Updates%0Ainstagram.com%2FBB_Films_Updates"""

START_LOG = """🟢 <b>{mention} ({username})
#id{id}  [<code>{id}</code>]</b>"""


YUNUS_EMRE = """<b>[BB] Yunus Emre
English Subtitle
All Qualities Available ✅
Select the Season Below 👇</b>"""


YUNUS_EMRE1 = """<b>[BB] Yunus Emre

Season: 1
Episodes: 22

English Subtitle
All Qualities Available ✅

Coming Soon...</b>"""


YUNUS_EMRE2 = """<b>[BB] Yunus Emre

Season 2
Episodes: 23

English Subtitle
All Qualities Available ✅

Coming Soon...</b>"""


ALPARSLAN = """<b>[BB] Alparslan: Büyük Selçuklu

English Subtitle
All Qualities Available ✅

Select the Season Below 👇</b>"""


BARBAROSLAR = """<b>[BB] Barbaroslar: Akdeniz'in Kılıcı</b>
<i>(Barbaros: Sword of the Mediterranean)</i>

<b>With English subtitle ✅
All Qualities Available ✅

Select the Season Below 👇</b>"""


ERTUGRUL720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTM2OTk2NTE2NTM5MzA2NjAtMzgzNTgyMjg2NTAwOTAyOA'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟏 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4Mzc4MjUzODI4MTkwMDQtMzk1NTk3MzkzMzYwNzU4OA'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟐 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5NTY5NzUxOTI1MTI1NzYtNDA2MjEwNzM3NzUzNjMxNg'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟑 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwODMxMzM4MTQ1NDEwNjQtNDE3NDI0ODM3NDg5NDk3Mg'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟒 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxOTAyNjg1MTczNzQ3ODAtNDI5MTM5NTY2Njc3ODU2OA'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟓 ⚔</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

ERTUGRUL360 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅
In 360p SD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTY4MTg1NzMxNDI5NjgyOC03MDc4OTAwNDU4MjY1MTY'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟏 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTcwODg5MTMwNDczMTUwNC03NDM5MzUzNjY0MDYwODQ'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟐 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc0NDkzNjYyNTMxMTA3Mi03NzQ5NzQzOTI0NjA3MTI'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟑 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc3NTk3NTY1MTM2NTcwMC04MDYwMTM0MTg1MTUzNDA'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟒 ⚔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTgwNzAxNDY3NzQyMDMyOC04MzYwNTExODU2NjQ5ODA'>⚔ 𝗦𝗲𝗮𝘀𝗼𝗻 𝟓 ⚔</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

KUTUL_AMARE = """<b>[BB] Mehmetçik Kut'ül Amare
Season 1 | Episode 01-19
[BB] Mehmetçik Kut'ül Zafer

Season 2 | Episode 20-34
With English Subtitle ✅

Quality: 360p ✅</b>

<code>Season 1</code>
<b>https://t.me/{botusername}?start=Z2V0LTEzMzk2ODQ0MTQ4NzM5NDQtMTM3MjcyNTk1ODczODU0OA</b>

<code>Season 2</code>
<b>https://t.me/{botusername}?start=Z2V0LTEzNzM3MjcyMTc2NDM1MzYtMTM4OTc0NzM2MDEyMzM0NA</b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

PAYITAHT = """<b>[BB] Payitaht Abdülhamid
English Subtitle
Total No. of Season: 5
Total No. of Episodes: 154
Select the Season Below 👇</b>"""

PAYITAHT1 = """<b>Step - 𝟏 »»» Click On Any Episode
Step - 𝟐 »»» Press 𝗦𝘁𝗮𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻
[BB] Payitaht Abdülhamid
Season 𝟏 ✅
English subtitle</b>

<a href='https://t.me/{botusername}?start=Z2V0LTIyMTY3ODcyMTU2NDM0MzItMjIzMzgwODYxNzAyODIyOA'>🌟 𝟯𝟲𝟬𝗽 𝗦𝗗 🌟</a>

<a href='https://t.me/{botusername}?start=Z2V0LTIzMzk5NDIwNjA5NTY5NTYtMjM1Njk2MzQ2MjM0MTc1Mg'>🌟 𝟳𝟮𝟬𝗽 𝗛𝗗 🌟</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

PAYITAHT2 = """<b>Step - 𝟏 »»» Click On Any Episode
Step - 𝟐 »»» Press 𝗦𝘁𝗮𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻
[BB] Payitaht Abdülhamid
Season 𝟐 ✅
English subtitle

<a href='https://t.me/{botusername}?start=Z2V0LTIyMzQ4MDk4NzU5MzMyMTYtMjI3MTg1NjQ1NTQxNzc3Mg'>🌟 𝟯𝟲𝟬𝗽 𝗦𝗗 🌟</a>

<a href='https://t.me/{botusername}?start=Z2V0LTIzNTc5NjQ3MjEyNDY3NDAtMjM5NjAxMjU1OTYzNjI4NA'>🌟 𝟳𝟮𝟬𝗽 𝗛𝗗 🌟</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

PAYITAHT3 = """<b>Step - 𝟏 »»» Click On Any Episode
Step - 𝟐 »»» Press 𝗦𝘁𝗮𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻
[BB] Payitaht Abdülhamid
Season 𝟑 ✅
English subtitle

<a href='https://t.me/{botusername}?start=Z2V0LTIyNzI4NTc3MTQzMjI3NjAtMjMwNjkwMDUxNzA5MjM1Mg'>🌟 𝟯𝟲𝟬𝗽 𝗦𝗗 🌟</a>

<a href='https://t.me/{botusername}?start=Z2V0LTIzOTcwMTM4MTg1NDEyNzItMjQzMzA1OTEzOTEyMDg0MA'>🌟 𝟳𝟮𝟬𝗽 𝗛𝗗 🌟</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


PAYITAHT4 = """<b>Step - 𝟏 »»» Click On Any Episode
Step - 𝟐 »»» Press 𝗦𝘁𝗮𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻
[BB] Payitaht Abdülhamid
Season 𝟒 ✅
English subtitle

<a href='https://t.me/{botusername}?start=Z2V0LTIzMDc5MDE3NzU5OTczNDAtMjMzODk0MDgwMjA1MTk2OA'>🌟 𝟯𝟲𝟬𝗽 𝗦𝗗 🌟</a>

<a href='https://t.me/{botusername}?start=Z2V0LTI0MzQwNjAzOTgwMjU4MjgtMjQ3MzEwOTQ5NTMyMDM2MA'>🌟 𝟳𝟮𝟬𝗽 𝗛𝗗 🌟</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


PAYITAHT5 = """<b>Step - 𝟏 »»» Click On Any Episode
Step - 𝟐 »»» Press 𝗦𝘁𝗮𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻
[BB] Payitaht Abdülhamid
Season 𝟓 ✅
English subtitle

<a href='https://t.me/{botusername}?start=Z2V0LTk5MjI0NzU3NDg0MzEwOC0xMTkxNDk4MDk2OTM1NzIw'>🌟 𝗦𝗲𝗮𝘀𝗼𝗻 𝟱 🌟</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


ALPARSLAN1 = """<b>[BB] Alparslan: Büyük Selçuklu
With English subtitle ✅

Season: 1
Total Episodes: 27

<a href='https://t.me/{botusername}?start=Z2V0LTE3MTgxNjAyODA5NTk0MDgtMTcyMzE2NjU3NTQ4NDM0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE3NDYxOTU1MzAyOTkwNzItMTc1MTIwMTgyNDgyNDAxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE4MDUyNjk4MDU2OTMzNjQtMTgxMDI3NjEwMDIxODMwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE4NjIzNDE1NjMyNzc2ODAtMTg3MDM1MTYzNDUxNzU4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE5Mjk0MjU5MDk5MTE4NzYtMTkzNzQzNTk4MTE1MTc4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTI1MTAxNTYwNzQ4MDQ5MTYtMjUxODE2NjE0NjA0NDgyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTI2MTkyOTMyOTU0NDg2MDgtMjYyNzMwMzM2NjY4ODUxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTI2ODczNzg5MDA5ODc3OTItMjY5MjM4NTE5NTUxMjczMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTM1Njg0ODY3MzczNzcyMzItMzU3MzQ5MzAzMTkwMjE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTM2ODU2MzQwMjkyNjA4MjgtMzY5MTY0MTU4MjY5MDc1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ0MDA1MzI4ODc0MjIyNjAtNDQwNTUzOTE4MTk0NzIwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ1ODk3NzA4MjA0NjQ5OTItNDU5NDc3NzExNDk4OTkzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ2NzA4NzI3OTE3NjkwMjAtNDY3Mjg3NTMwOTU3ODk5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ3Mjg5NDU4MDgyNTgzMjQtNDczMTk0OTU4NDk3MzI4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ3NzQwMDI0NTg5ODI3ODQtNDc3NzAwNjIzNTY5Nzc0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ4MDIwMzc3MDgzMjI0NDgtNDgwNjA0Mjc0Mzk0MjQwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ4NDgwOTU2MTc5NTE4OTYtNDg1MTA5OTM5NDY2Njg2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ4ODgxNDU5NzQxNTE0MTYtNDg5MTE0OTc1MDg2NjM4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ5NTIyMjY1NDQwNzA2NDgtNDk1NTIzMDMyMDc4NTYxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ5NzIyNTE3MjIxNzA0MDgtNDk3NTI1NTQ5ODg4NTM3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUwMjQzMTcxODUyMjk3ODQtNTAyNzMyMDk2MTk0NDc0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUwMzkzMzYwNjg4MDQ2MDQtNTA0MjMzOTg0NTUxOTU2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUwNzAzNzUwOTQ4NTkyMzItNTA3MzM3ODg3MTU3NDE5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUxMjI0NDA1NTc5MTg2MDgtNTEyNjQ0NTU5MzUzODU2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUxNDg0NzMyODk0NDgyOTYtNTE1MDQ3NTgwNzI1ODI3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUxNjI0OTA5MTQxMTgxMjgtNTE2NTQ5NDY5MDgzMzA5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTUyMDE1NDAwMTE0MTI2NjAtNTIwNDU0Mzc4ODEyNzYyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕 Season Finale</a></b

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


BARBAROSLAR1 = """<b>[BB] Barbaroslar: Akdeniz'in Kılıcı</b>
<i>(Barbaros: Sword of the Mediterranean)</i>
<b>With English subtitle ✅

Season: 1
Total Episodes: 32

<a href='https://t.me/{botusername}?start=Z2V0LTE3ODIyNDA4NTA4Nzg2NC0xODMyMzAzNzk2MTI4MDQ'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE5MDIzOTE5MTk0NzcyMC0xOTUyNDU0ODY0NzI2NjA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEyMTc1MzA4Mjg0NjU0MDgtMTIyNzU0MzQxNzUxNTI4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEzMTk2NTkyMzY3NzQxODQtMTMyOTY3MTgyNTgyNDA2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE1MjQ5MTczMTIyOTY3MjQtMTUzMzkyODY0MjQ0MTYxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE1NjU5Njg5Mjc0MDEyMzItMTU3MDk3NTIyMTkyNjE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE2NTYwODIyMjg4NTAxNTItMTY2MTA4ODUyMzM3NTA5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE3MzMxNzkxNjQ1MzQyMjgtMTczODE4NTQ1OTA1OTE2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE3NjMyMTY5MzE2ODM4NjgtMTc2ODIyMzIyNjIwODgwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTE4NDEzMTUxMjYyNzI5MzItMTg0NjMyMTQyMDc5Nzg3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTE4OTYzODQzNjYwNDcyNzItMTkwNjM5Njk1NTA5NzE1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTIyMDU3NzMzNjc2ODg1NjQtMjIxMzc4MzQzODkyODQ2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTI1MzgxOTEzMjQxNDQ1ODAtMjU0NjIwMTM5NTM4NDQ4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTI2NjkzNTYyNDA2OTgwMDgtMjY3NDM2MjUzNTIyMjk0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTI3MTI0MTAzNzM2MTI0OTItMjcxODQxNzkyNzA0MjQyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTM2MzU1NzEwODQwMTE0MjgtMzY0MDU3NzM3ODUzNjM2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQzNDU0NjM2NDc2NDc5MjAtNDM1MDQ2OTk0MjE3Mjg2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ1MDc2Njc1OTAyNTU5NzYtNDUxMjY3Mzg4NDc4MDkxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ2MDE3ODU5MjczMjQ4NDgtNDYwNjc5MjIyMTg0OTc4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ2NzQ4Nzc4MjczODg5NzItNDY3Njg4MDM0NTE5ODk0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ3Mzg5NTgzOTczMDgyMDQtNDc0MTk2MjE3NDAyMzE2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ3OTMwMjYzNzgxNzc1NTYtNDc5NjAzMDE1NDg5MjUyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ4MjEwNjE2Mjc1MTcyMjAtNDgyNjA2NzkyMjA0MjE2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTQ5MzgyMDg5MTk0MDA4MTYtNDk0MTIxMjY5NjExNTc4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTQ5NjMyNDAzOTIwMjU1MTYtNDk2NjI0NDE2ODc0MDQ4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUwMDMyOTA3NDgyMjUwMzYtNTAwNjI5NDUyNDk0MDAwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUwMTkzMTA4OTA3MDQ4NDQtNTAyMjMxNDY2NzQxOTgwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUwNTUzNTYyMTEyODQ0MTItNTA1ODM1OTk4Nzk5OTM3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUwODczOTY0OTYyNDQwMjgtNTA5MDQwMDI3Mjk1ODk5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUxMzY0NTgxODI1ODg0NDAtNTEzODQ2MDcwMDM5ODQxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTUxODQ1MTg2MTAwMjc4NjQtNTE4NzUyMjM4Njc0MjgyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>

<a href='https://t.me/{botusername}?start=Z2V0LTUxNzg1MTEwNTY1OTc5MzYtNTE4MTUxNDgzMzMxMjkwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐 Season Finale</a></b

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


UYANIS = """<b>[BB] Uyanış: Büyük Selçuklu
With English subtitle ✅
Total Episodes: 34

<a href='https://t.me/{botusername}?start=Z2V0LTUyNTY2MDkyNTExODcwMDAtNTI2MDYxNDI4NjgwNjk1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTUyNjI2MTY4MDQ2MTY5MjgtNTI2NjYyMTg0MDIzNjg4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUyNjg2MjQzNTgwNDY4NTYtNTI3MzYzMDY1MjU3MTc5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTUyODE2NDA3MjM4MTE3MDAtNTI4NjY0NzAxODMzNjY0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUyODg2NDk1MzYxNDY2MTYtNTI5MzY1NTgzMDY3MTU1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTUyOTU2NTgzNDg0ODE1MzItNTMwMDY2NDY0MzAwNjQ3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzMDM2Njg0MTk3MjE0MzYtNTMwODY3NDcxNDI0NjM3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTUzMTE2Nzg0OTA5NjEzNDAtNTMxNjY4NDc4NTQ4NjI4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzMTg2ODczMDMyOTYyNTYtNTMyMzY5MzU5NzgyMTE5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTUzMjU2OTYxMTU2MzExNzItNTMzMDcwMjQxMDE1NjExMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzMzI3MDQ5Mjc5NjYwODgtNTMzNzcxMTIyMjQ5MTAyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUzMzk3MTM3NDAzMDEwMDQtNTM0NDcyMDAzNDgyNTk0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzNDY3MjI1NTI2MzU5MjAtNTM1MTcyODg0NzE2MDg2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUzNTU3MzM4ODI3ODA4MTItNTM2MDc0MDE3NzMwNTc1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzNjI3NDI2OTUxMTU3MjgtNTM2Nzc0ODk4OTY0MDY2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUzNjk3NTE1MDc0NTA2NDQtNTM3NDc1NzgwMTk3NTU4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzNzY3NjAzMTk3ODU1NjAtNTM4MTc2NjYxNDMxMDUwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUzODM3NjkxMzIxMjA0NzYtNTM4ODc3NTQyNjY0NTQxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUzOTA3Nzc5NDQ0NTUzOTItNTM5NTc4NDIzODk4MDMzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTUzOTc3ODY3NTY3OTAzMDgtNTQwMjc5MzA1MTMxNTI0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTU0MDQ3OTU1NjkxMjUyMjQtNTQwOTgwMTg2MzY1MDE2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0MTE4MDQzODE0NjAxNDAtNTQxNjgxMDY3NTk4NTA4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTU0MTg4MTMxOTM3OTUwNTYtNTQyMzgxOTQ4ODMxOTk5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0OTc5MTI2NDcyODkxMDgtNTUwMjkxODk0MTgxNDA0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a>  
    
<a href='https://t.me/{botusername}?start=Z2V0LTU0MjU4MjIwMDYxMjk5NzItNTQzMDgyODMwMDY1NDkxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0MzI4MzA4MTg0NjQ4ODgtNTQzNzgzNzExMjk4OTgyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a>  
 
<a href='https://t.me/{botusername}?start=Z2V0LTU0Mzk4Mzk2MzA3OTk4MDQtNTQ0NDg0NTkyNTMyNDc0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0NDY4NDg0NDMxMzQ3MjAtNTQ1MTg1NDczNzY1OTY2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU0NTM4NTcyNTU0Njk2MzYtNTQ1ODg2MzU0OTk5NDU3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0NjA4NjYwNjc4MDQ1NTItNTQ2NTg3MjM2MjMyOTQ5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTU0Njc4NzQ4ODAxMzk0NjgtNTQ3Mjg4MTE3NDY2NDQwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU0NzQ4ODM2OTI0NzQzODQtNTQ3OTg4OTk4Njk5OTMyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a>    
    
<a href='https://t.me/{botusername}?start=Z2V0LTUwNzAzNzUwOTQ4NTkyMzItNTA3MzM3ODg3MTU3NDE5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU0ODQ4OTYyODE1MjQyNjQtNTQ4ODkwMTMxNzE0NDIxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""
