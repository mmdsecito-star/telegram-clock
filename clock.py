import os
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
string_session = os.environ["STRING_SESSION"]

client = TelegramClient(
    StringSession(string_session),
    api_id,
    api_hash
)

BASE_NAME = "𝘿𝙚𝙭𝙩𝙖"

async def main():
    await client.start()

    while True:
        try:
            iran_time = datetime.now(
                ZoneInfo("Asia/Tehran")
            ).strftime("%H:%M")

            await client(
                UpdateProfileRequest(
                    first_name=f"{BASE_NAME} {iran_time}"
                )
            )

            print(iran_time)

        except Exception as e:
            print(e)

        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())
