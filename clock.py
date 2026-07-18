import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_id = 27954319
api_hash = "1a0399fc583eb656f13a7ad684674e2e"

client = TelegramClient("clock_session", api_id, api_hash)

BASE_NAME = "𝑫𝒆𝒙𝒕𝒂"

async def main():
    await client.start()

    while True:
        now = datetime.now().strftime("%H:%M")

        await client(UpdateProfileRequest(
            first_name=f"{BASE_NAME}  {now}"
        ))

        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())