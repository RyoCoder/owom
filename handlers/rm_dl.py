# function to remove the downloaded files

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "rmdownloads", "cleardownloads"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **Đã xóa tất cả các tệp đã tải xuống**")
    else:
        await message.reply_text("❌ **Không có tệp nào được tải xuống**")
        
@Client.on_message(command(["clean", "wipe", "rmr"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **Đã xóa tất cả các tệp thô**")
    else:
        await message.reply_text("❌ **Không có tệp thô**")
        
