from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn, BOT_USERNAME, CHANNEL, GROUP
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CXxlzEwABAUVhYTEYkSeUDfME8f8AAeuk_0I1DyDGAAL6BAACWVOJVdLn7ez7kDaoIAQ")
    await message.reply_text(
        f"""**Tui là là {bn} 🎵

Tui có thể phát nhạc trong cuộc gọi thoại của nhóm bạn. Được phát triển bởi [owogram](https://t.me/owogram).

Nâng cấp bot để thêm tín năng sau:**
• Thời lượng nhạc không giới hạn
• Thêm nút chọn bài
• Bảng cài đặt
• Điều khiển bằng các nút
• Phát nhạc trên kênh
• Hàng đợi không giới hạn
• Trợ lý tự động tham gia
• Tự động xóa lệnh
• Không cho thành viên bất kỳ mở nhạc
• Khóa chat, tạm khóa, và cấm thành viên
• Hoạt động mượt, linh hoạt

**Liên hệ: [Ryo Star](https://t.me/ryostar)** 🎵
        """,
        reply_markup=InlineKeyboardMarkup(
            [
               [
                    InlineKeyboardButton(
                        "🎙  Thêm tôi vào nhóm của bạn ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
               [
                    InlineKeyboardButton(
                        "💬 Nhóm", url=f"https://t.me/{CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kênh", url=f"https://t.me/{GROUP}"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bố mày con thức ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Cập nhật", url="https://t.me/owogram")
                ]
            ]
        )
   )


