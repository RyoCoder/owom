# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic
# Ported by @levina-lab for VeezMusic

import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command

@Client.on_message(command(["asupan", f"asupan@{BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Đã xảy ra lỗi LOL...`")


@Client.on_message(command(["wibu", f"wibu@{BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Đã xảy ra lỗi LOL...`")


@Client.on_message(command(["chika", f"chika@{BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Đã xảy ra lỗi LOL...`")


@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Có gì đó không ổn...")


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Có gì đó không ổn...")


#@Client.on_message(command(["lyric", f"lyric@{BOT_USERNAME}"]))
#async def lirik(_, message):
#    try:
#        if len(message.command) < 2:
#            await message.reply_text("**Cung cấp cho một tên lời bài hát quá!**")
#            return
#        query = message.text.split(None, 1)[1]
#        rep = await message.reply_text("🔎 **Tìm kiếm lời bài hát...**")
#        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
#        result = f"{resp['data']}"
#        await rep.edit(result)
 #   except Exception:
 #       await rep.edit("**Không tìm thấy lời bài hát.** Xin vui lòng cung cấp một tên bài hát hợp lệ !")
@Client.on_message(command(["site", f"site@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**Cung cấp cho một tên lời bài hát quá!**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **Tìm kiếm lời bài hát...**")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/http-headers?q={query}").json()
        result = f"{resp['result']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Không tìm thấy lời bài hát.** Xin vui lòng cung cấp một tên bài hát hợp lệ !")
