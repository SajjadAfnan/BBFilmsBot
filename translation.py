import os
import logging
from logging.handlers import RotatingFileHandler

INSTAGRAM = """https://instagram.com/BB_Films_Updates"""

SHARE_LINK = """https://t.me/share/url?url=instagram.com%2FBB_Films_Updates%0A%0AFollow%20the%20above%20Instagram%20page%20to%20get%20all%20official%20Updates%20about%20Barbaroslar%20Akdeniz%27in%20Kilici%20%26%20Alparslan%20B%C3%BCy%C3%BCk%20Sel%C3%A7uklu%0A%0AIf%20the%20current%20bot%20gets%20copyright%2C%20then%20new%20bot%20link%20will%20publish%20on%20the%20above%20Instagram%20page%20Bio%20%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%0A%0Ainstagram.com%2FBB_Films_Updates%0Ainstagram.com%2FBB_Films_Updates%0Ainstagram.com%2FBB_Films_Updates"""

START_LOG = """🟢 <b>{mention} ({username})
#id{id}  [<code>{id}</code>]</b>"""


OSMAN = """<b>[BB] Kurulus Osman
English Subtitle

Select the Season Below 👇</b>"""

OSMAN1 = """<b>[BB] Kuruluş Osman
English subtitle ✅

Season: 1
Total Episodes: 27

<a href='https://t.me/{botusername}?start=Z2V0LTYxNzk3Njk5NjE1ODU5MzYtNjE4MDc3MTIyMDQ5MDkyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYxODI3NzM3MzgzMDA5MDAtNjE4Mzc3NDk5NzIwNTg4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxODU3Nzc1MTUwMTU4NjQtNjE4Njc3ODc3MzkyMDg1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYxODg3ODEyOTE3MzA4MjgtNjE4OTc4MjU1MDYzNTgxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxOTE3ODUwNjg0NDU3OTItNjE5Mjc4NjMyNzM1MDc4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYxOTQ3ODg4NDUxNjA3NTYtNjE5NTc5MDEwNDA2NTc0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxOTc3OTI2MjE4NzU3MjAtNjE5ODc5Mzg4MDc4MDcwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyMDA3OTYzOTg1OTA2ODQtNjIwMTc5NzY1NzQ5NTY3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMDM4MDAxNzUzMDU2NDgtNjIwNDgwMTQzNDIxMDYzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyMDY4MDM5NTIwMjA2MTItNjIwNzgwNTIxMDkyNTYwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMDk4MDc3Mjg3MzU1NzYtNjIxMDgwODk4NzY0MDU2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyMTI4MTE1MDU0NTA1NDAtNjIxMzgxMjc2NDM1NTUyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMTU4MTUyODIxNjU1MDQtNjIxNjgxNjU0MTA3MDQ5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyMTg4MTkwNTg4ODA0NjgtNjIxOTgyMDMxNzc4NTQ1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMjE4MjI4MzU1OTU0MzItNjIyMjgyNDA5NDUwMDQyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyMjQ4MjY2MTIzMTAzOTYtNjIyNTgyNzg3MTIxNTM4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMjc4MzAzODkwMjUzNjAtNjIyODgzMTY0NzkzMDM0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyMzA4MzQxNjU3NDAzMjQtNjIzMTgzNTQyNDY0NTMxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMzM4Mzc5NDI0NTUyODgtNjIzNDgzOTIwMTM2MDI3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyMzY4NDE3MTkxNzAyNTItNjIzNzg0Mjk3ODA3NTI0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyMzk4NDU0OTU4ODUyMTYtNjI0MDg0Njc1NDc5MDIwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyNDI4NDkyNzI2MDAxODAtNjI0Mzg1MDUzMTUwNTE2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyNDU4NTMwNDkzMTUxNDQtNjI0Njg1NDMwODIyMDEzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyNDg4NTY4MjYwMzAxMDgtNjI0OTg1ODA4NDkzNTA5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyNTE4NjA2MDI3NDUwNzItNjI1Mjg2MTg2MTY1MDA2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYyNTQ4NjQzNzk0NjAwMzYtNjI1NTg2NTYzODM2NTAyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTYyNTc4NjgxNTYxNzUwMDAtNjI1ODg2OTQxNTA3OTk4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""

OSMAN2 = """<b>[BB] Kuruluş Osman
English subtitle ✅

Season: 2
Total Episodes: 37

<a href='https://t.me/{botusername}?start=Z2V0LTYyNjE4NzMxOTE3OTQ5NTItNjI2Mzg3NTcwOTYwNDkyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyNjU4NzgyMjc0MTQ5MDQtNjI2Nzg4MDc0NTIyNDg4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyNjk4ODMyNjMwMzQ4NTYtNjI3MTg4NTc4MDg0NDgzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyNzM4ODgyOTg2NTQ4MDgtNjI3NTg5MDgxNjQ2NDc4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyNzc4OTMzMzQyNzQ3NjAtNjI3OTg5NTg1MjA4NDczNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyODE4OTgzNjk4OTQ3MTItNjI4MzkwMDg4NzcwNDY4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyODU5MDM0MDU1MTQ2NjQtNjI4NzkwNTkyMzMyNDY0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyODg5MDcxODIyMjk2MjgtNjI5MDkwOTcwMDAzOTYwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYyOTI5MTIyMTc4NDk1ODAtNjI5NDkxNDczNTY1OTU1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYyOTY5MTcyNTM0Njk1MzItNjI5ODkxOTc3MTI3OTUwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzMDA5MjIyODkwODk0ODQtNjMwMjkyNDgwNjg5OTQ2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzMDQ5MjczMjQ3MDk0MzYtNjMwNjkyOTg0MjUxOTQxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzMDg5MzIzNjAzMjkzODgtNjMxMDkzNDg3ODEzOTM2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzMTI5MzczOTU5NDkzNDAtNjMxNDkzOTkxMzc1OTMxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzMTY5NDI0MzE1NjkyOTItNjMxODk0NDk0OTM3OTI2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzMjA5NDc0NjcxODkyNDQtNjMyMjk0OTk4NDk5OTIyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzMjQ5NTI1MDI4MDkxOTYtNjMyNjk1NTAyMDYxOTE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzMjg5NTc1Mzg0MjkxNDgtNjMzMDk2MDA1NjIzOTEyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzMzI5NjI1NzQwNDkxMDAtNjMzNDk2NTA5MTg1OTA3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzMzY5Njc2MDk2NjkwNTItNjMzODk3MDEyNzQ3OTAyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzNDA5NzI2NDUyODkwMDQtNjM0Mjk3NTE2MzA5ODk4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzNDQ5Nzc2ODA5MDg5NTYtNjM0Njk4MDE5ODcxODkzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzNDg5ODI3MTY1Mjg5MDgtNjM1MDk4NTIzNDMzODg4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzNTI5ODc3NTIxNDg4NjAtNjM1NDk5MDI2OTk1ODgzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzNTY5OTI3ODc3Njg4MTItNjM1ODk5NTMwNTU3ODc4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzNjA5OTc4MjMzODg3NjQtNjM2MzAwMDM0MTE5ODc0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzNjUwMDI4NTkwMDg3MTYtNjM2NzAwNTM3NjgxODY5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzNjkwMDc4OTQ2Mjg2NjgtNjM3MTAxMDQxMjQzODY0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzNzMwMTI5MzAyNDg2MjAtNjM3NTAxNTQ0ODA1ODU5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzNzcwMTc5NjU4Njg1NzItNjM3OTAyMDQ4MzY3ODU0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTYzODEwMjMwMDE0ODg1MjQtNjM4MzAyNTUxOTI5ODUwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzODUwMjgwMzcxMDg0NzYtNjM4NzAzMDU1NDkxODQ1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzODkwMzMwNzI3Mjg0MjgtNjM5MTAzNTU5MDUzODQwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYzOTMwMzgxMDgzNDgzODAtNjM5NTA0MDYyNjE1ODM1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYzOTcwNDMxNDM5NjgzMzItNjM5OTA0NTY2MTc3ODMwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY0MDEwNDgxNzk1ODgyODQtNjQwMzA1MDY5NzM5ODI2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0MDUwNTMyMTUyMDgyMzYtNjQwNzA1NTczMzAxODIxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟕 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

OSMAN3 = """<b>[BB] Kuruluş Osman
English subtitle ✅

Season: 3
Total Episodes: 34

<a href='https://t.me/{botusername}?start=Z2V0LTY0MDkwNTgyNTA4MjgxODgtNjQxMjA2MjAyNzU0MzE1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY0MTQwNjQ1NDUzNTMxMjgtNjQxNzA2ODMyMjA2ODA5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0MTkwNzA4Mzk4NzgwNjgtNjQyMjA3NDYxNjU5MzAzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY0MjQwNzcxMzQ0MDMwMDgtNjQyNzA4MDkxMTExNzk3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0MjkwODM0Mjg5Mjc5NDgtNjQzMjA4NzIwNTY0MjkxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY0MzQwODk3MjM0NTI4ODgtNjQzNzA5MzUwMDE2Nzg1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0MzkwOTYwMTc5Nzc4MjgtNjQ0MjA5OTc5NDY5Mjc5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY0NDQxMDIzMTI1MDI3NjgtNjQ0NzEwNjA4OTIxNzczMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0NDkxMDg2MDcwMjc3MDgtNjQ1MjExMjM4Mzc0MjY3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY0NTQxMTQ5MDE1NTI2NDgtNjQ1NzExODY3ODI2NzYxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0NTkxMjExOTYwNzc1ODgtNjQ2MjEyNDk3Mjc5MjU1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY0NjQxMjc0OTA2MDI1MjgtNjQ2NzEzMTI2NzMxNzQ5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0NjkxMzM3ODUxMjc0NjgtNjQ3MjEzNzU2MTg0MjQzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY0NzQxNDAwNzk2NTI0MDgtNjQ3NzE0Mzg1NjM2NzM3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0NzkxNDYzNzQxNzczNDgtNjQ4MjE1MDE1MDg5MjMxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY0ODQxNTI2Njg3MDIyODgtNjQ4NzE1NjQ0NTQxNzI1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0ODkxNTg5NjMyMjcyMjgtNjQ5MjE2MjczOTk0MjE5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY0OTQxNjUyNTc3NTIxNjgtNjQ5NzE2OTAzNDQ2NzEzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY0OTkxNzE1NTIyNzcxMDgtNjUwMjE3NTMyODk5MjA3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1MDQxNzc4NDY4MDIwNDgtNjUwNzE4MTYyMzUxNzAxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1MDkxODQxNDEzMjY5ODgtNjUxMjE4NzkxODA0MTk1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1MTQxOTA0MzU4NTE5MjgtNjUxNzE5NDIxMjU2Njg5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1MTkxOTY3MzAzNzY4NjgtNjUyMjIwMDUwNzA5MTgzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1MjQyMDMwMjQ5MDE4MDgtNjUyNzIwNjgwMTYxNjc3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1MjkyMDkzMTk0MjY3NDgtNjUzMjIxMzA5NjE0MTcxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1MzQyMTU2MTM5NTE2ODgtNjUzNzIxOTM5MDY2NjY1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1MzkyMjE5MDg0NzY2MjgtNjU0MjIyNTY4NTE5MTU5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1NDQyMjgyMDMwMDE1NjgtNjU0NzIzMTk3OTcxNjUzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1NDkyMzQ0OTc1MjY1MDgtNjU1MjIzODI3NDI0MTQ3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1NTQyNDA3OTIwNTE0NDgtNjU1NzI0NDU2ODc2NjQxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTY1NTkyNDcwODY1NzYzODgtNjU2MjI1MDg2MzI5MTM1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY1NjQyNTMzODExMDEzMjgtNjU2NzI1NzE1NzgxNjI5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY1NjkyNTk2NzU2MjYyNjgtNjU3MjI2MzQ1MjM0MTIzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>

<a href='https://t.me/{botusername}?start=Z2V0LTY1NzQyNjU5NzAxNTEyMDgtNjU3NzI2OTc0Njg2NjE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""

DESTAN = """<b>[BB] Destan
English Subtitle

Select the Season Below 👇</b>"""

DESTAN1 = """<b>[BB] Destan
English subtitle ✅

Season: 1
Total Episodes: 27

<a href='https://t.me/{botusername}?start=Z2V0LTY1OTUyOTI0MDcxNTU5NTYtNjYwMDI5ODcwMTY4MDg5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY2MDIzMDEyMTk0OTA4NzItNjYwNzMwNzUxNDAxNTgxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2MDkzMTAwMzE4MjU3ODgtNjYxNDMxNjMyNjM1MDcyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY2MTYzMTg4NDQxNjA3MDQtNjYyMTMyNTEzODY4NTY0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2MjMzMjc2NTY0OTU2MjAtNjYyNjMzMTQzMzIxMDU4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY2MjgzMzM5NTEwMjA1NjAtNjYzMTMzNzcyNzczNTUyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2MzMzNDAyNDU1NDU1MDAtNjYzNjM0NDAyMjI2MDQ2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY2MzgzNDY1NDAwNzA0NDAtNjY0MTM1MDMxNjc4NTQwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2NDMzNTI4MzQ1OTUzODAtNjY0NjM1NjYxMTMxMDM0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY2NDgzNTkxMjkxMjAzMjAtNjY1MTM2MjkwNTgzNTI4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2NTMzNjU0MjM2NDUyNjAtNjY1NjM2OTIwMDM2MDIyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY2NTgzNzE3MTgxNzAyMDAtNjY2MTM3NTQ5NDg4NTE2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2NjMzNzgwMTI2OTUxNDAtNjY2NjM4MTc4OTQxMDEwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY2NjgzODQzMDcyMjAwODAtNjY3MTM4ODA4MzkzNTA0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2NzMzOTA2MDE3NDUwMjAtNjY3NjM5NDM3ODQ1OTk4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY2NzgzOTY4OTYyNjk5NjAtNjY4MTQwMDY3Mjk4NDkyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2ODM0MDMxOTA3OTQ5MDAtNjY4NjQwNjk2NzUwOTg2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY2ODg0MDk0ODUzMTk4NDAtNjY5MTQxMzI2MjAzNDgwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY2OTM0MTU3Nzk4NDQ3ODAtNjY5NjQxOTU1NjU1OTc0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY2OTg0MjIwNzQzNjk3MjAtNjcwMTQyNTg1MTA4NDY4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3MDM0MjgzNjg4OTQ2NjAtNjcwNjQzMjE0NTYwOTYyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY3MDg0MzQ2NjM0MTk2MDAtNjcxMTQzODQ0MDEzNDU2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3MTM0NDA5NTc5NDQ1NDAtNjcxNjQ0NDczNDY1OTUwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY3MTg0NDcyNTI0Njk0ODAtNjcyMTQ1MTAyOTE4NDQ0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3MjM0NTM1NDY5OTQ0MjAtNjcyNjQ1NzMyMzcwOTM4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY3Mjg0NTk4NDE1MTkzNjAtNjczMTQ2MzYxODIzNDMyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTY3MzM0NjYxMzYwNDQzMDAtNjczNjQ2OTkxMjc1OTI2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""

YUNUS_EMRE = """<b>[BB] Yunus Emre

Select the Button Below 👇</b>"""


EN_YUNUS_EMRE = """<b>[BB] Yunus Emre

English Subtitle ✅

Select the Button Below 👇</b>"""


UR_YUNUS_EMRE = """<b>[[BB] راہےعشق (Yunus Emre)

ہندی/اردو ڈب 

 👇 یہاں سے سیزن منتخب کریں۔</b>"""


UR_YUNUS_EMRE1 = """<b>[BB] Yunus Emre

Season: 1
Episodes: 22

<a href='https://t.me/{botusername}?start=Z2V0LTY3NTA0ODc1Mzc0MjkwOTYtNjc1MzQ5MTMxNDE0NDA2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY3NTU0OTM4MzE5NTQwMzYtNjc1ODQ5NzYwODY2OTAwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3NjA1MDAxMjY0Nzg5NzYtNjc2MzUwMzkwMzE5Mzk0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY3NjU1MDY0MjEwMDM5MTYtNjc2ODUxMDE5NzcxODg4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3NzA1MTI3MTU1Mjg4NTYtNjc3MzUxNjQ5MjI0MzgyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY3NzU1MTkwMTAwNTM3OTYtNjc3ODUyMjc4Njc2ODc2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3ODA1MjUzMDQ1Nzg3MzYtNjc4MzUyOTA4MTI5MzcwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY3ODU1MzE1OTkxMDM2NzYtNjc4ODUzNTM3NTgxODY0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY3OTA1Mzc4OTM2Mjg2MTYtNjc5MzU0MTY3MDM0MzU4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY3OTU1NDQxODgxNTM1NTYtNjc5ODU0Nzk2NDg2ODUyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4MDA1NTA0ODI2Nzg0OTYtNjgwMzU1NDI1OTM5MzQ2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY4MDU1NTY3NzcyMDM0MzYtNjgwODU2MDU1MzkxODQwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4MTA1NjMwNzE3MjgzNzYtNjgxMzU2Njg0ODQ0MzM0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY4MTU1NjkzNjYyNTMzMTYtNjgxODU3MzE0Mjk2ODI4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4MjA1NzU2NjA3NzgyNTYtNjgyMzU3OTQzNzQ5MzIyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY4MjU1ODE5NTUzMDMxOTYtNjgyODU4NTczMjAxODE2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4MzA1ODgyNDk4MjgxMzYtNjgzMzU5MjAyNjU0MzEwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY4MzU1OTQ1NDQzNTMwNzYtNjgzODU5ODMyMTA2ODA0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4NDA2MDA4Mzg4NzgwMTYtNjg0MzYwNDYxNTU5Mjk4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY4NDU2MDcxMzM0MDI5NTYtNjg0ODYxMDkxMDExNzkyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4NTA2MTM0Mjc5Mjc4OTYtNjg1NDYxODQ2MzU0Nzg0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>

<a href='https://t.me/{botusername}?start=Z2V0LTY4NTY2MjA5ODEzNTc4MjQtNjg1OTYyNDc1ODA3Mjc4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""


UR_YUNUS_EMRE2 = """<b>[BB] Yunus Emre

Season: 2
Episodes: 39

<a href='https://t.me/{botusername}?start=Z2V0LTY4NzA2Mzg2MDYwMjc2NTYtNjg3MzY0MjM4Mjc0MjYyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY4NzU2NDQ5MDA1NTI1OTYtNjg3OTY0OTkzNjE3MjU0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4ODE2NTI0NTM5ODI1MjQtNjg4NDY1NjIzMDY5NzQ4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY4ODY2NTg3NDg1MDc0NjQtNjg4OTY2MjUyNTIyMjQyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY4OTE2NjUwNDMwMzI0MDQtNjg5NDY2ODgxOTc0NzM2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY4OTY2NzEzMzc1NTczNDQtNjg5OTY3NTExNDI3MjMwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5MDE2Nzc2MzIwODIyODQtNjkwNDY4MTQwODc5NzI0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY5MDY2ODM5MjY2MDcyMjQtNjkwOTY4NzcwMzMyMjE4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5MTE2OTAyMjExMzIxNjQtNjkxNDY5Mzk5Nzg0NzEyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTY5MTY2OTY1MTU2NTcxMDQtNjkxOTcwMDI5MjM3MjA2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5MjE3MDI4MTAxODIwNDQtNjkyNDcwNjU4Njg5NzAwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5MjY3MDkxMDQ3MDY5ODQtNjkyOTcxMjg4MTQyMTk0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5MzE3MTUzOTkyMzE5MjQtNjkzNDcxOTE3NTk0Njg4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5MzY3MjE2OTM3NTY4NjQtNjkzOTcyNTQ3MDQ3MTgyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5NDE3Mjc5ODgyODE4MDQtNjk0NDczMTc2NDk5Njc2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5NDY3MzQyODI4MDY3NDQtNjk0OTczODA1OTUyMTcwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5NTE3NDA1NzczMzE2ODQtNjk1NDc0NDM1NDA0NjY0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5NTY3NDY4NzE4NTY2MjQtNjk1OTc1MDY0ODU3MTU4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5NjE3NTMxNjYzODE1NjQtNjk2NDc1Njk0MzA5NjUyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5NjY3NTk0NjA5MDY1MDQtNjk2OTc2MzIzNzYyMTQ2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5NzE3NjU3NTU0MzE0NDQtNjk3NDc2OTUzMjE0NjQwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5NzY3NzIwNDk5NTYzODQtNjk3OTc3NTgyNjY3MTM0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5ODE3NzgzNDQ0ODEzMjQtNjk4NDc4MjEyMTE5NjI4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5ODY3ODQ2MzkwMDYyNjQtNjk4OTc4ODQxNTcyMTIyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTY5OTE3OTA5MzM1MzEyMDQtNjk5NDc5NDcxMDI0NjE2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTY5OTY3OTcyMjgwNTYxNDQtNjk5OTgwMTAwNDc3MTEwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwMDE4MDM1MjI1ODEwODQtNzAwNDgwNzI5OTI5NjA0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwMDY4MDk4MTcxMDYwMjQtNzAwOTgxMzU5MzgyMDk4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwMTE4MTYxMTE2MzA5NjQtNzAxNDgxOTg4ODM0NTkyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwMTY4MjI0MDYxNTU5MDQtNzAxOTgyNjE4Mjg3MDg2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTcwMjE4Mjg3MDA2ODA4NDQtNzAyNDgzMjQ3NzM5NTgwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwMjg4Mzc1MTMwMTU3NjAtNzAzMjg0MjU0ODYzNTcxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwMzQ4NDUwNjY0NDU2ODgtNzAzNzg0ODg0MzE2MDY1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwMzk4NTEzNjA5NzA2MjgtNzA0Mjg1NTEzNzY4NTU5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwNDQ4NTc2NTU0OTU1NjgtNzA0Nzg2MTQzMjIxMDUzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwNDk4NjM5NTAwMjA1MDgtNzA1Mjg2NzcyNjczNTQ3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwNTQ4NzAyNDQ1NDU0NDgtNzA1Nzg3NDAyMTI2MDQxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTcwNTk4NzY1MzkwNzAzODgtNzA2Mjg4MDMxNTc4NTM1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTcwNjQ4ODI4MzM1OTUzMjgtNzA2Nzg4NjYxMDMxMDI5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟗 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a>

🛑 اوپر کے لنک پر کلک کرنے کے بعد نیچے START بٹن دبائیں 🛑</b>
                              👇👇👇👇👇"""


EN_YUNUS_EMRE1 = """<b>[BB] Yunus Emre

Season: 1
Episodes: 22

English Subtitle
All Qualities Available ✅

<a href='https://t.me/{botusername}?start=Z2V0LTU5MTI0MzM4MzM5NTQxNDAtNTkxNTQzNzYxMDY2OTEwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU5MTc0NDAxMjg0NzkwODAtNTkyMDQ0MzkwNTE5NDA0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5MjI0NDY0MjMwMDQwMjAtNTkyNTQ1MDE5OTcxODk4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU5Mjc0NTI3MTc1Mjg5NjAtNTkzMDQ1NjQ5NDI0MzkyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5MzY0NjQwNDc2NzM4NTItNTkzOTQ2NzgyNDM4ODgxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU5NDE0NzAzNDIxOTg3OTItNTk0NDQ3NDExODkxMzc1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5NDY0NzY2MzY3MjM3MzItNTk0OTQ4MDQxMzQzODY5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU5NTE0ODI5MzEyNDg2NzItNTk1NDQ4NjcwNzk2MzYzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5NTY0ODkyMjU3NzM2MTItNTk1OTQ5MzAwMjQ4ODU3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU5NjE0OTU1MjAyOTg1NTItNTk2NDQ5OTI5NzAxMzUxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5NjY1MDE4MTQ4MjM0OTItNTk2OTUwNTU5MTUzODQ1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU5NzE1MDgxMDkzNDg0MzItNTk3NDUxMTg4NjA2MzM5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5NzY1MTQ0MDM4NzMzNzItNTk3OTUxODE4MDU4ODMzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU5ODE1MjA2OTgzOTgzMTItNTk4NDUyNDQ3NTExMzI3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5ODY1MjY5OTI5MjMyNTItNTk4OTUzMDc2OTYzODIxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU5OTE1MzMyODc0NDgxOTItNTk5NDUzNzA2NDE2MzE1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU5OTY1Mzk1ODE5NzMxMzItNTk5OTU0MzM1ODY4ODA5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYwMDE1NDU4NzY0OTgwNzItNjAwNDU0OTY1MzIxMzAzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwMDY1NTIxNzEwMjMwMTItNjAwOTU1NTk0NzczNzk3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYwMTE1NTg0NjU1NDc5NTItNjAxNDU2MjI0MjI2MjkxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwMTY1NjQ3NjAwNzI4OTItNjAxOTU2ODUzNjc4Nzg1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>

<a href='https://t.me/{botusername}?start=Z2V0LTYwMjE1NzEwNTQ1OTc4MzItNjAyNDU3NDgzMTMxMjc5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""


EN_YUNUS_EMRE2 = """<b>[BB] Yunus Emre

Season 2
Episodes: 23

English Subtitle
All Qualities Available ✅

<a href='https://t.me/{botusername}?start=Z2V0LTYwMzU1ODg2NzkyNjc2NjQtNjAzODU5MjQ1NTk4MjYyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYwNDA1OTQ5NzM3OTI2MDQtNjA0MzU5ODc1MDUwNzU2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwNDU2MDEyNjgzMTc1NDQtNjA0ODYwNTA0NTAzMjUwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYwNTA2MDc1NjI4NDI0ODQtNjA1MzYxMTMzOTU1NzQ0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwNTU2MTM4NTczNjc0MjQtNjA1ODYxNzYzNDA4MjM4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYwNjA2MjAxNTE4OTIzNjQtNjA2MzYyMzkyODYwNzMyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwNzA2MzI3NDA5NDIyNDQtNjA3MzYzNjUxNzY1NzIwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYwNzU2MzkwMzU0NjcxODQtNjA3ODY0MjgxMjE4MjE0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwODA2NDUzMjk5OTIxMjQtNjA4MzY0OTEwNjcwNzA4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTYwODU2NTE2MjQ1MTcwNjQtNjA4ODY1NTQwMTIzMjAyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYwOTA2NTc5MTkwNDIwMDQtNjA5MzY2MTY5NTc1Njk2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYwOTU2NjQyMTM1NjY5NDQtNjA5ODY2Nzk5MDI4MTkwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxMDA2NzA1MDgwOTE4ODQtNjEwMzY3NDI4NDgwNjg0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYxMDU2NzY4MDI2MTY4MjQtNjEwODY4MDU3OTMzMTc4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxMTA2ODMwOTcxNDE3NjQtNjExMzY4Njg3Mzg1NjcyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYxMTU2ODkzOTE2NjY3MDQtNjExODY5MzE2ODM4MTY2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxMjA2OTU2ODYxOTE2NDQtNjEyMzY5OTQ2MjkwNjYwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYxMjU3MDE5ODA3MTY1ODQtNjEyODcwNTc1NzQzMTU0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxMzA3MDgyNzUyNDE1MjQtNjEzMzcxMjA1MTk1NjQ4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTYxMzU3MTQ1Njk3NjY0NjQtNjEzODcxODM0NjQ4MTQyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTYxNDA3MjA4NjQyOTE0MDQtNjE0MzcyNDY0MTAwNjM2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>

<a href='https://t.me/{botusername}?start=Z2V0LTYxNDU3MjcxNTg4MTYzNDQtNjE1NTczOTc0Nzg2NjIyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""


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

𝗦𝗲𝗮𝘀𝗼𝗻 - 1

<a href='https://t.me/{botusername}?start=Z2V0LTY4MTg1NzMxNDI5NjgyOC02OTA4Njg2NDQ0NDE3MjA=='>📺 𝗕ö𝗹ü𝗺 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTY5MTg2OTkwMzM0NjcwOC03MDA4ODEyMzM0OTE2MDA=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTcwMTg4MjQ5MjM5NjU4OC03MDY4ODg3ODY5MjE1Mjg=='>📺 𝗕ö𝗹ü𝗺 𝟐𝟏 - 𝟐𝟔</a>

𝗦𝗲𝗮𝘀𝗼𝗻 - 𝟐

<a href='https://t.me/{botusername}?start=Z2V0LTcwODg5MTMwNDczMTUwNC03MTE4OTUwODE0NDY0Njg=='>📺 𝗕ö𝗹ü𝗺 𝟐𝟕 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTcxMjg5NjM0MDM1MTQ1Ni03MjE5MDc2NzA0OTYzNDg=='>📺 𝗕ö𝗹ü𝗺 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTcyMjkwODkyOTQwMTMzNi03MzE5MjAyNTk1NDYyMjg=='>📺 𝗕ö𝗹ü𝗺 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTczMjkyMTUxODQ1MTIxNi03MzY5MjY1NTQwNzExNjg=='>📺 𝗕ö𝗹ü𝗺 𝟓𝟏 - 𝟓𝟓</a>

<a href='https://t.me/{botusername}?start=Z2V0LTczNzkyNzgxMjk3NjE1Ni03NDI5MzQxMDc1MDEwOTY=='>📺 𝗕ö𝗹ü𝗺 𝟓𝟔 - 𝟔𝟏</a>

𝗦𝗲𝗮𝘀𝗼𝗻 - 𝟑

<a href='https://t.me/{botusername}?start=Z2V0LTc0NDkzNjYyNTMxMTA3Mi03NTI5NDY2OTY1NTA5NzY=='>📺 𝗕ö𝗹ü𝗺 𝟔𝟐 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc1Mzk0Nzk1NTQ1NTk2NC03NjI5NTkyODU2MDA4NTY=='>📺 𝗕ö𝗹ü𝗺 𝟕𝟏 - 𝟖𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc2Mzk2MDU0NDUwNTg0NC03Njc5NjU1ODAxMjU3OTY=='>📺 𝗕ö𝗹ü𝗺 𝟖𝟏 - 𝟖𝟓</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc2ODk2NjgzOTAzMDc4NC03NzM5NzMxMzM1NTU3MjQ=='>📺 𝗕ö𝗹ü𝗺 𝟖𝟔 - 𝟗𝟏</a>

𝗦𝗲𝗮𝘀𝗼𝗻 - 𝟒

<a href='https://t.me/{botusername}?start=Z2V0LTc3NTk3NTY1MTM2NTcwMC03ODM5ODU3MjI2MDU2MDQ=='>📺 𝗕ö𝗹ü𝗺 𝟗𝟐 - 𝟏𝟎𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc4NDk4Njk4MTUxMDU5Mi03OTM5OTgzMTE2NTU0ODQ=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟎𝟏 - 𝟏𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTc5NDk5OTU3MDU2MDQ3Mi03OTkwMDQ2MDYxODA0MjQ=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟏𝟏 - 𝟏𝟏𝟓</a>

<a href='https://t.me/{botusername}?start=Z2V0LTgwMDAwNTg2NTA4NTQxMi04MDUwMTIxNTk2MTAzNTI=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟏𝟔  - 𝟏𝟐𝟏</a>

𝗦𝗲𝗮𝘀𝗼𝗻 - 𝟓

<a href='https://t.me/{botusername}?start=Z2V0LTgwNzAxNDY3NzQyMDMyOC04MTUwMjQ3NDg2NjAyMzI=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟐𝟐  - 𝟏𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTgxNjAyNjAwNzU2NTIyMC04MjUwMzczMzc3MTAxMTI=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟑𝟏  - 𝟏𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTgyNjAzODU5NjYxNTEwMC04MzUwNDk5MjY3NTk5OTI=='>📺 𝗕ö𝗹ü𝗺 𝟏𝟒𝟏 - 𝟏𝟓𝟎</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


EN_ERTUGRUL1_720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅

Season 1
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTM2OTk2NTE2NTM5MzA2NjAtMzcwODY2Mjk4NDA3NTU1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM3MDk2NjQyNDI5ODA1NDAtMzcxODY3NTU3MzEyNTQzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM3MTk2NzY4MzIwMzA0MjAtMzcyODY4ODE2MjE3NTMxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM3Mjk2ODk0MjEwODAzMDAtMzczODcwMDc1MTIyNTE5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM3Nzk3NTIzNjYzMjk3MDAtMzc4ODc2MzY5NjQ3NDU5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM3ODk3NjQ5NTUzNzk1ODAtMzc5ODc3NjI4NTUyNDQ3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓𝟏 - 𝟔𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4MTk4MDI3MjI1MjkyMjAtMzgyODgxNDA1MjY3NDExMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔𝟏 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4Mjk4MTUzMTE1NzkxMDAtMzgzNDgyMTYwNjEwNDA0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕𝟏 - 𝟕𝟔</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


EN_ERTUGRUL2_720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅

Season 2
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTM4Mzc4MjUzODI4MTkwMDQtMzg0NjgzNjcxMjk2Mzg5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4NDc4Mzc5NzE4Njg4ODQtMzg1Njg0OTMwMjAxMzc3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4NTc4NTA1NjA5MTg3NjQtMzg2Njg2MTg5MTA2MzY1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4Njc4NjMxNDk5Njg2NDQtMzg3Njg3NDQ4MDExMzUzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4Nzc4NzU3MzkwMTg1MjQtMzg4Njg4NzA2OTE2MzQxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4ODc4ODgzMjgwNjg0MDQtMzg5Njg5OTY1ODIxMzI5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓𝟏 - 𝟔𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM4OTc5MDA5MTcxMTgyODQtMzkwNjkxMjI0NzI2MzE3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔𝟏 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5MDc5MTM1MDYxNjgxNjQtMzkxNjkyNDgzNjMxMzA1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕𝟏 - 𝟖𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5MjM5MzM2NDg2NDc5NzItMzkzMjk0NDk3ODc5Mjg2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖𝟏 - 𝟗𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5MzM5NDYyMzc2OTc4NTItMzk0Mjk1NzU2Nzg0Mjc0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗𝟏 - 𝟏𝟎𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5NDM5NTg4MjY3NDc3MzItMzk0NTk2MTM0NDU1NzcwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎𝟏 - 𝟏𝟎𝟑</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


EN_ERTUGRUL3_720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅

Season 3
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTM5NTY5NzUxOTI1MTI1NzYtMzk2NTk4NjUyMjY1NzQ2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5NjY5ODc3ODE1NjI0NTYtMzk3NTk5OTExMTcwNzM0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5NzcwMDAzNzA2MTIzMzYtMzk5MDAxNjczNjM3NzE4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTM5OTEwMTc5OTUyODIxNjgtNDAwMDAyOTMyNTQyNzA2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwMDEwMzA1ODQzMzIwNDgtNDAyMDA1NDUwMzUyNjgyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwMjEwNTU3NjI0MzE4MDgtNDAzMDA2NzA5MjU3NjcwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓𝟏 - 𝟔𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwMzEwNjgzNTE0ODE2ODgtNDA0MDA3OTY4MTYyNjU4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔𝟏 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwNDEwODA5NDA1MzE1NjgtNDA1MDA5MjI3MDY3NjQ2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕𝟏 - 𝟖𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwNTEwOTM1Mjk1ODE0NDgtNDA1NTA5ODU2NTIwMTQwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖𝟏 - 𝟖𝟓</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwNTYwOTk4MjQxMDYzODgtNDA2MTEwNjExODYzMTMyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖𝟔 - 𝟗𝟏</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


EN_ERTUGRUL4_720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅

Season 4
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTQwODMxMzM4MTQ1NDEwNjQtNDA5MjE0NTE0NDY4NTk1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQwOTMxNDY0MDM1OTA5NDQtNDEwMjE1NzczMzczNTgzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxMDMxNTg5OTI2NDA4MjQtNDExMjE3MDMyMjc4NTcxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxMTMxNzE1ODE2OTA3MDQtNDEyMjE4MjkxMTgzNTU5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxMjMxODQxNzA3NDA1ODQtNDEzMjE5NTUwMDg4NTQ3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxMzMxOTY3NTk3OTA0NjQtNDE0MjIwODA4OTkzNTM1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓𝟏 - 𝟔𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxNDMyMDkzNDg4NDAzNDQtNDE1MjIyMDY3ODk4NTIzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔𝟏 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxNTMyMjE5Mzc4OTAyMjQtNDE2MjIzMzI2ODAzNTExNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕𝟏 - 𝟖𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQxNjMyMzQ1MjY5NDAxMDQtNDE3MjI0NTg1NzA4NDk5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖𝟏 - 𝟗𝟎</a>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


EN_ERTUGRUL5_720 = """<b>[BB] Diriliş Ertuğrul
With English subtitle ✅

Season 5
In 720p HD Quality ⭐️</b>

<a href='https://t.me/{botusername}?start=Z2V0LTQxOTEyNjk3NzYyNzk3NjgtNDIwMDI4MTEwNjQyNDY2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏 - 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyMDEyODIzNjUzMjk2NDgtNDIxMDI5MzY5NTQ3NDU0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏 - 𝟐𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyMTEyOTQ5NTQzNzk1MjgtNDIyMDMwNjI4NDUyNDQyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏 - 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyMjEzMDc1NDM0Mjk0MDgtNDI0MTMzMjcyMTUyOTE2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 - 𝟒𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyNDIzMzM5ODA0MzQxNTYtNDI1MTM0NTMxMDU3OTA0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒𝟏 - 𝟓𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyNTIzNDY1Njk0ODQwMzYtNDI2MTM1Nzg5OTYyODkyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓𝟏 - 𝟔𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyNjIzNTkxNTg1MzM5MTYtNDI3MTM3MDQ4ODY3ODgwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔𝟏 - 𝟕𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyNzIzNzE3NDc1ODM3OTYtNDI4MTM4MzA3NzcyODY4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕𝟏 - 𝟖𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTQyODIzODQzMzY2MzM2NzYtNDI4OTM5MzE0ODk2ODU5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖𝟏 - 𝟖𝟖</a>

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

PAYITAHT1 = """<b>[BB] Payitaht Abdülhamid 
With English subtitle ✅

Season: 1
Total Episodes: 17

<a href='https://t.me/{botusername}?start=Z2V0LTU1MTQ5MzQwNDg2NzM5MDQtNTUxNTkzNTMwNzU3ODg5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1MTc5Mzc4MjUzODg4NjgtNTUxODkzOTA4NDI5Mzg1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1MjA5NDE2MDIxMDM4MzItNTUyMTk0Mjg2MTAwODgyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1MjM5NDUzNzg4MTg3OTYtNTUyNDk0NjYzNzcyMzc4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1MjY5NDkxNTU1MzM3NjAtNTUyNzk1MDQxNDQzODc0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1Mjk5NTI5MzIyNDg3MjQtNTUzMDk1NDE5MTE1MzcxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1MzI5NTY3MDg5NjM2ODgtNTUzMzk1Nzk2Nzg2ODY3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1MzU5NjA0ODU2Nzg2NTItNTUzNjk2MTc0NDU4MzY0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1NDA5NjY3ODAyMDM1OTItNTU0MTk2ODAzOTEwODU4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1NDM5NzA1NTY5MTg1NTYtNTU0NDk3MTgxNTgyMzU0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1NDY5NzQzMzM2MzM1MjAtNTU0Nzk3NTU5MjUzODUwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU1NDk5NzgxMTAzNDg0ODQtNTU1MDk3OTM2OTI1MzQ3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1NTI5ODE4ODcwNjM0NDgtNTU1Mzk4MzE0NTk2ODQzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU1NTU5ODU2NjM3Nzg0MTItNTU1Njk4NjkyMjY4MzQwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1NTg5ODk0NDA0OTMzNzYtNTU1OTk5MDY5OTM5ODM2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU1NjE5OTMyMTcyMDgzNDAtNTU2Mjk5NDQ3NjExMzMyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU1NjQ5OTY5OTM5MjMzMDQtNTU2NTk5ODI1MjgyODI5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>


🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

PAYITAHT2 = """<b>[BB] Payitaht Abdülhamid 
With English subtitle ✅

Season: 2
Total Episodes: 37

<a href='https://t.me/{botusername}?start=Z2V0LTU1NjgwMDA3NzA2MzgyNjgtNTU2OTAwMjAyOTU0MzI1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1NzEwMDQ1NDczNTMyMzItNTU3MjAwNTgwNjI1ODIyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU1NzQwMDgzMjQwNjgxOTYtNTU3NTAwOTU4Mjk3MzE4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1NzcwMTIxMDA3ODMxNjAtNTU3ODAxMzM1OTY4ODE0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU1ODAwMTU4Nzc0OTgxMjQtNTU4MTAxNzEzNjQwMzExMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1ODMwMTk2NTQyMTMwODgtNTU4NDAyMDkxMzExODA3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU1ODYwMjM0MzA5MjgwNTItNTU4NzAyNDY4OTgzMzA0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1ODkwMjcyMDc2NDMwMTYtNTU5MDAyODQ2NjU0ODAwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU1OTIwMzA5ODQzNTc5ODAtNTU5MzAzMjI0MzI2Mjk2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU1OTUwMzQ3NjEwNzI5NDQtNTU5NjAzNjAxOTk3NzkzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU1OTgwMzg1Mzc3ODc5MDgtNTU5OTAzOTc5NjY5Mjg5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MDEwNDIzMTQ1MDI4NzItNTYwMjA0MzU3MzQwNzg2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MDQwNDYwOTEyMTc4MzYtNTYwNTA0NzM1MDEyMjgyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MDcwNDk4Njc5MzI4MDAtNTYwODA1MTEyNjgzNzc4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MTAwNTM2NDQ2NDc3NjQtNTYxMTA1NDkwMzU1Mjc1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MTMwNTc0MjEzNjI3MjgtNTYxNDA1ODY4MDI2NzcxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MTYwNjExOTgwNzc2OTItNTYxNzA2MjQ1Njk4MjY4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MTkwNjQ5NzQ3OTI2NTYtNTYyMDA2NjIzMzY5NzY0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MjIwNjg3NTE1MDc2MjAtNTYyMzA3MDAxMDQxMjYwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MjUwNzI1MjgyMjI1ODQtNTYyNjA3Mzc4NzEyNzU3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MjgwNzYzMDQ5Mzc1NDgtNTYyOTA3NzU2Mzg0MjUzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MzEwODAwODE2NTI1MTItNTYzMjA4MTM0MDU1NzUwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2MzQwODM4NTgzNjc0NzYtNTYzNTA4NTExNzI3MjQ2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2MzcwODc2MzUwODI0NDAtNTYzODA4ODg5Mzk4NzQyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NDAwOTE0MTE3OTc0MDQtNTY0MTA5MjY3MDcwMjM5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NDMwOTUxODg1MTIzNjgtNTY0NDA5NjQ0NzQxNzM1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NDYwOTg5NjUyMjczMzItNTY0NzEwMDIyNDEzMjMyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NDkxMDI3NDE5NDIyOTYtNTY1MDEwNDAwMDg0NzI4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NTIxMDY1MTg2NTcyNjAtNTY1MzEwNzc3NzU2MjI0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NTUxMTAyOTUzNzIyMjQtNTY1NjExMTU1NDI3NzIxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU2NTgxMTQwNzIwODcxODgtNTY1OTExNTMzMDk5MjE3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NjExMTc4NDg4MDIxNTItNTY2MjExOTEwNzcwNzE0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NjQxMjE2MjU1MTcxMTYtNTY2NTEyMjg4NDQyMjEwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NjcxMjU0MDIyMzIwODAtNTY2ODEyNjY2MTEzNzA2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NzAxMjkxNzg5NDcwNDQtNTY3MTEzMDQzNzg1MjAzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU2NzMxMzI5NTU2NjIwMDgtNTY3NDEzNDIxNDU2Njk5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2NzYxMzY3MzIzNzY5NzItNTY3NzEzNzk5MTI4MTk2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟕 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""

PAYITAHT3 = """<b>[BB] Payitaht Abdülhamid 
With English subtitle ✅

Season: 3
Total Episodes: 34

<a href='https://t.me/{botusername}?start=Z2V0LTU2NzkxNDA1MDkwOTE5MzYtNTY4MDE0MTc2Nzk5NjkyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU2ODIxNDQyODU4MDY5MDAtNTY4MzE0NTU0NDcxMTg4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2ODUxNDgwNjI1MjE4NjQtNTY4NjE0OTMyMTQyNjg1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU2ODgxNTE4MzkyMzY4MjgtNTY4OTE1MzA5ODE0MTgxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2OTExNTU2MTU5NTE3OTItNTY5MjE1Njg3NDg1Njc4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU2OTQxNTkzOTI2NjY3NTYtNTY5NTE2MDY1MTU3MTc0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU2OTcxNjMxNjkzODE3MjAtNTY5ODE2NDQyODI4NjcwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU3MDAxNjY5NDYwOTY2ODQtNTcwMjE2OTQ2MzkwNjY2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MDQxNzE5ODE3MTY2MzYtNTcwNTE3MzI0MDYyMTYyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU3MDcxNzU3NTg0MzE2MDAtNTcwODE3NzAxNzMzNjU4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MTAxNzk1MzUxNDY1NjQtNTcxMTE4MDc5NDA1MTU1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3MTMxODMzMTE4NjE1MjgtNTcxNDE4NDU3MDc2NjUxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MTYxODcwODg1NzY0OTItNTcxNzE4ODM0NzQ4MTQ4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3MTkxOTA4NjUyOTE0NTYtNTcyMDE5MjEyNDE5NjQ0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MjIxOTQ2NDIwMDY0MjAtNTcyMzE5NTkwMDkxMTQwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3MjUxOTg0MTg3MjEzODQtNTcyNjE5OTY3NzYyNjM3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MjgyMDIxOTU0MzYzNDgtNTcyOTIwMzQ1NDM0MTMzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3MzEyMDU5NzIxNTEzMTItNTczMjIwNzIzMTA1NjMwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3MzQyMDk3NDg4NjYyNzYtNTczNTIxMTAwNzc3MTI2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3MzcyMTM1MjU1ODEyNDAtNTczODIxNDc4NDQ4NjIyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NDAyMTczMDIyOTYyMDQtNTc0MTIxODU2MTIwMTE5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NDMyMjEwNzkwMTExNjgtNTc0NDIyMjMzNzkxNjE1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NDYyMjQ4NTU3MjYxMzItNTc0NzIyNjExNDYzMTEyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NDkyMjg2MzI0NDEwOTYtNTc1MDIyOTg5MTM0NjA4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NTIyMzI0MDkxNTYwNjAtNTc1MzIzMzY2ODA2MTA0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NTUyMzYxODU4NzEwMjQtNTc1NjIzNzQ0NDc3NjAxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NTgyMzk5NjI1ODU5ODgtNTc1OTI0MTIyMTQ5MDk3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NjEyNDM3MzkzMDA5NTItNTc2MjI0NDk5ODIwNTk0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NjQyNDc1MTYwMTU5MTYtNTc2NTI0ODc3NDkyMDkwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NjcyNTEyOTI3MzA4ODAtNTc2ODI1MjU1MTYzNTg2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU3NzAyNTUwNjk0NDU4NDQtNTc3MTI1NjMyODM1MDgzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU3NzMyNTg4NDYxNjA4MDgtNTc3NDI2MDEwNTA2NTc5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3NzYyNjI2MjI4NzU3NzItNTc3NzI2Mzg4MTc4MDc2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU3NzkyNjYzOTk1OTA3MzYtNTc4MDI2NzY1ODQ5NTcyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


PAYITAHT4 = """<b>[BB] Payitaht Abdülhamid 
With English subtitle ✅

Season: 4
Total Episodes: 31

<a href='https://t.me/{botusername}?start=Z2V0LTU3ODMyNzE0MzUyMTA2ODgtNTc4NDI3MjY5NDExNTY3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU3ODkyNzg5ODg2NDA2MTYtNTc5MDI4MDI0NzU0NTYwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3OTIyODI3NjUzNTU1ODAtNTc5MzI4NDAyNDI2MDU2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU3OTUyODY1NDIwNzA1NDQtNTc5NjI4NzgwMDk3NTUzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU3OTgyOTAzMTg3ODU1MDgtNTc5OTI5MTU3NzY5MDQ5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU4MDEyOTQwOTU1MDA0NzItNTgwMjI5NTM1NDQwNTQ2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MDQyOTc4NzIyMTU0MzYtNTgwNTI5OTEzMTEyMDQyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU4MDczMDE2NDg5MzA0MDAtNTgwODMwMjkwNzgzNTM4OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MTAzMDU0MjU2NDUzNjQtNTgxMTMwNjY4NDU1MDM1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTU4MTMzMDkyMDIzNjAzMjgtNTgxNDMxMDQ2MTI2NTMxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MTYzMTI5NzkwNzUyOTItNTgxNzMxNDIzNzk4MDI4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4MTkzMTY3NTU3OTAyNTYtNTgyMDMxODAxNDY5NTI0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MjIzMjA1MzI1MDUyMjAtNTgyMzMyMTc5MTQxMDIwOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4MjUzMjQzMDkyMjAxODQtNTgyNjMyNTU2ODEyNTE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MjgzMjgwODU5MzUxNDgtNTgyOTMyOTM0NDg0MDEzNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4MzEzMzE4NjI2NTAxMTItNTgzMjMzMzEyMTU1NTEwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4MzQzMzU2MzkzNjUwNzYtNTgzNTMzNjg5ODI3MDA2NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4MzczMzk0MTYwODAwNDAtNTgzODM0MDY3NDk4NTAyOA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NDAzNDMxOTI3OTUwMDQtNTg0MTM0NDQ1MTY5OTk5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NDMzNDY5Njk1MDk5NjgtNTg0NDM0ODIyODQxNDk1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NDYzNTA3NDYyMjQ5MzItNTg0NzM1MjAwNTEyOTkyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NDkzNTQ1MjI5Mzk4OTYtNTg1MDM1NTc4MTg0NDg4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NTIzNTgyOTk2NTQ4NjAtNTg1MzM1OTU1ODU1OTg0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NTUzNjIwNzYzNjk4MjQtNTg1NjM2MzMzNTI3NDgxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NTgzNjU4NTMwODQ3ODgtNTg1OTM2NzExMTk4OTc3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NjEzNjk2Mjk3OTk3NTItNTg2MjM3MDg4ODcwNDc0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NjQzNzM0MDY1MTQ3MTYtNTg2NTM3NDY2NTQxOTcwNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NjczNzcxODMyMjk2ODAtNTg2ODM3ODQ0MjEzNDY2OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTU4NzAzODA5NTk5NDQ2NDQtNTg3MTM4MjIxODg0OTYzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTU4NzMzODQ3MzY2NTk2MDgtNTg3NDM4NTk5NTU2NDU5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTU4NzYzODg1MTMzNzQ1NzItNTg3NzM4OTc3MjI3OTU2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑
                              👇👇👇👇👇"""


PAYITAHT5 = """<b>[BB] Payitaht Abdülhamid 
With English subtitle ✅

Season: 5
Total Episodes: 35

<a href='https://t.me/{botusername}?start=Z2V0LTk5MjI0NzU3NDg0MzEwOC05OTgyNTUxMjgyNzMwMzY'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEwMDEyNTg5MDQ5ODgwMDAtMTAwNTI2Mzk0MDYwNzk1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwMDcyNjY0NTg0MTc5MjgtMTAxMDI3MDIzNTEzMjg5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEwMTIyNzI3NTI5NDI4NjgtMTAxNTI3NjUyOTY1NzgzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwMTcyNzkwNDc0Njc4MDgtMTAyMTI4NDA4MzA4Nzc2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟓</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEwMjMyODY2MDA4OTc3MzYtMTAyNTI4OTExODcwNzcxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwMjcyOTE2MzY1MTc2ODgtMTAzMDI5NTQxMzIzMjY1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟕</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEwMzUzMDE3MDc3NTc1OTItMTAzOTMwNjc0MzM3NzU0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwNDEzMDkyNjExODc1MjAtMTA0NDMxMzAzNzkwMjQ4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟗</a>        <a href='https://t.me/{botusername}?start=Z2V0LTEwNDYzMTU1NTU3MTI0NjAtMTA1MDMyMDU5MTMzMjQxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟎 </a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwNTIzMjMxMDkxNDIzODgtMTA1NTMyNjg4NTg1NzM1Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTEwNTczMjk0MDM2NjczMjgtMTA2MDMzMzE4MDM4MjI5Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwNjIzMzU2OTgxOTIyNjgtMTA2NTMzOTQ3NDkwNzIzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTEwNjczNDE5OTI3MTcyMDgtMTA3MDM0NTc2OTQzMjE3Mg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwNzIzNDgyODcyNDIxNDgtMTA3NTM1MjA2Mzk1NzExMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTEwNzczNTQ1ODE3NjcwODgtMTA4MTM1OTYxNzM4NzA0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwODMzNjIxMzUxOTcwMTYtMTA4NjM2NTkxMTkxMTk4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTEwODgzNjg0Mjk3MjE5NTYtMTA5MTM3MjIwNjQzNjkyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTEwOTMzNzQ3MjQyNDY4OTYtMTA5NzM3OTc1OTg2Njg0OA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟏𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTEwOTkzODIyNzc2NzY4MjQtMTEwMzM4NzMxMzI5Njc3Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟎</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExMDUzODk4MzExMDY3NTItMTEwODM5MzYwNzgyMTcxNg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExMTAzOTYxMjU2MzE2OTItMTExMzM5OTkwMjM0NjY1Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExMTU0MDI0MjAxNTY2MzItMTExODQwNjE5Njg3MTU5Ng'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExMjA0MDg3MTQ2ODE1NzItMTEyNDQxMzc1MDMwMTUyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExMzY0Mjg4NTcxNjEzODAtMTEzOTQzMjYzMzg3NjM0NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟓</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExNDE0MzUxNTE2ODYzMjAtMTE0NDQzODkyODQwMTI4NA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟔</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExNDY0NDE0NDYyMTEyNjAtMTE1MDQ0NjQ4MTgzMTIxMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExNTI0NDg5OTk2NDExODgtMTE1NjQ1NDAzNTI2MTE0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟖</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExNTg0NTY1NTMwNzExMTYtMTE2MTQ2MDMyOTc4NjA4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟗</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExNjM0NjI4NDc1OTYwNTYtMTE2NjQ2NjYyNDMxMTAyMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟎</a>

<a href='https://t.me/{botusername}?start=Z2V0LTExNjg0NjkxNDIxMjA5OTYtMTE3MTQ3MjkxODgzNTk2MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟏</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExNzM0NzU0MzY2NDU5MzYtMTE3NjQ3OTIxMzM2MDkwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExNzg0ODE3MzExNzA4NzYtMTE4MTQ4NTUwNzg4NTg0MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟑</a>      <a href='https://t.me/{botusername}?start=Z2V0LTExODM0ODgwMjU2OTU4MTYtMTE4NjQ5MTgwMjQxMDc4MA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒</a> 
 
<a href='https://t.me/{botusername}?start=Z2V0LTExODg0OTQzMjAyMjA3NTYtMTE5MDQ5NjgzODAzMDczMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟓 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

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

<a href='https://t.me/{botusername}?start=Z2V0LTUyMDE1NDAwMTE0MTI2NjAtNTIwNDU0Mzc4ODEyNzYyNA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟐𝟕 Season Finale</a></b>

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

<a href='https://t.me/{botusername}?start=Z2V0LTUxNzg1MTEwNTY1OTc5MzYtNTE4MTUxNDgzMzMxMjkwMA'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟐 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

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

<a href='https://t.me/{botusername}?start=Z2V0LTU0OTA5MDM4MzQ5NTQxOTItNTQ5NTkxMDEyOTQ3OTEzMg'>📺 𝗘𝗽𝗶𝘀𝗼𝗱𝗲 𝟑𝟒 (𝐅𝐢𝐧𝐚𝐥 𝐄𝐩𝐢𝐬𝐨𝐝𝐞)</a></b>

🛑 <i>After clicking above link</i> <b>press START BUTTON</b> <i>Below</i> 🛑   
                              👇👇👇👇👇"""
