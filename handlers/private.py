from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn, BOT_USERNAME, CHANNEL, GROUP
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIEVGFHbudhpJ6Bs7oEctD0UkeyfQqjAAKUAwACrNI5VtytqfsDUe1XIAQ")
    await message.reply_text(
        f"""**Tui là là {bn} 🎵

Tui có thể phát nhạc trong cuộc gọi thoại của nhóm bạn.

Lệnh bot:**
• /play <url YTB/File> Mở nhạc bằng link YTP or File Telegram
• /p <tên bài hát> - Phát bài hát theo yêu cầu

• /tamdung - Tạm dừng nhạc
• /tieptuc - Tiếp tục phát nhạc
• /tatnhac - Tắt nhạc, rời voice chat
• /chuyenbai - Skip / bỏ qua bài hát

• /rmd - Xóa tất cả các tệp đã tải xuống
• /clean - Xóa tất cả các tệp thô
• /ping - Check trạng thái của bot


• /taimp3 - Tải xuống file mp3 bài hát
• /timkiem - Tìm kiếm Youtube


• /fun - Tự kiểm tra
• /fun1 - Tự kiểm tra
• /wibu - Tự kiểm tra


**Liên hệ chủ bot: [Ryo Star](https://t.me/ryostar)** 🎵
        """,
        reply_markup=InlineKeyboardMarkup(
            [
               [
                    InlineKeyboardButton(
                        "🎙  Thêm tôi vào nhóm của bạn ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            #   [
            #        InlineKeyboardButton(
             #           "💬 Nhóm", url=f"https://t.me/{CHANNEL}"
             #       ),
             #       InlineKeyboardButton(
              #          "🔊 Kênh", url=f"https://t.me/{GROUP}"
              #      )
             #   ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bố mày con thức ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Cập nhật", url=f"https://t.me/{CHANNEL}")
                ]
            ]
        )
   )


