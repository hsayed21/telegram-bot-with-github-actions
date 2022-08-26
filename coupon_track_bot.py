import asyncio
import nest_asyncio
from telethon import TelegramClient
from telethon.tl import functions, types
from telethon.sessions import StringSession
import requests
import datetime


# bot api
#-------------------
# to create bot and get bot_key https://core.telegram.org/bots#6-botfather
# to get chat_id https://t.me/myidbot
bot_key = "[bot_key]"
chat_id = "[chat_id]"

# telegram api
#-------------------
# to get api id and hash https://core.telegram.org/api/obtaining_api_id
api_id = [api_id]
api_hash = "[api_hash]"
# to get session_auth firstly run this block of code to display session_auth
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Generating a new one
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
"""

session_auth = "[session_auth]"

courses_channel = "[channel_here]"  ##https://t.me/coursefolder
courses = ["name_course1","name_course2"]

async def main():
    client = TelegramClient(StringSession(session_auth), api_id, api_hash)
    await client.start()
    channel = await client.get_entity(courses_channel)
    messages = client.iter_messages(channel, offset_date=datetime.date.today() , reverse=True)

    async for x in messages:
        for c in courses:
            if c.lower() in str(x.message).lower():
                print(x.message) #return message.text
                url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={x.message}"
                requests.get(url)

nest_asyncio.apply()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
