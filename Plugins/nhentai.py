from telethon import events
import Helper.formating_results as format
from  nhentaiapi import nhentaiapi as nh
from config import bot

class Nhentai():

    @bot.on(events.NewMessage(pattern="/nh"))
    async def event_handler_anime(event):
        if '/nh' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Hentai Manga not found Command must be used like this\n/nh <hentai code\nexample: /nh 339989',
                file='https://telegra.ph/file/ebe8484d678f49948a2a3.mp4'
            )
        elif '/nh' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = nh.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id,
                "You must open this in google chrome",
                file= f"{code}.html"
            )
