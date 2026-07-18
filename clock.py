import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# Railway Variables
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

# اسم شما
BASE_NAME = "𝘿𝙚𝙭𝙩𝙖"

# ساخت سشن
client = TelegramClient("clock_session", api_id, api_hash)

async def main():
    await client.start()

    print("Clock Started...")

    while True:
        try:
            # ساعت ایران
            now = datetime.now(ZoneInfo("Asia/Tehran")).strftime("%H:%M")

            await client(
                UpdateProfileRequest(
                    first_name=f"{BASE_NAME} {now}"
                )
            )

            print(f"Updated: {now}")

        except Exception as e:
            print("Error:", e)

        # هر ۶۰ ثانیه
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())
