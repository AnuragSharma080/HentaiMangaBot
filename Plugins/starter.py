from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern="/start"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://telegra.ph/file/0825336417b74a6c10fd7.mp4'
        )

    @bot.on(events.NewMessage(pattern="/help"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text,
            text='Hey there User kun! I am here To Provide you doujins manga easily with the doujins code! Do not get too horny while reading them oni chan!'
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Network](https://t.me/Project_Tsukiyomi/6)\nProvides you some doujins'
        )
    
