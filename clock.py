import os
import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# اطلاعات را از Environment Variables می‌خواند
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

# اسمی که می‌خواهی قبل از ساعت نمایش داده شود
BASE_NAME = "Mr Dexta"

client = TelegramClient("clock_session", api_id, api_hash)

async def main():
    await client.start()

    print("Clock started...")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        try:
            await client(
                UpdateProfileRequest(
                    first_name=f"{BASE_NAME} 🕒 {current_time}"
                )
            )

            print(f"Updated: {current_time}")

        except Exception as e:
            print(e)

        # هر 60 ثانیه یکبار
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())
