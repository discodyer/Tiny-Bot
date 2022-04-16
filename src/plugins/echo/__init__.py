from nonebot.adapters.onebot.v11 import MessageEvent as QMessageEvent
from nonebot.adapters.onebot.v11 import Bot as QBot
from nonebot.adapters.onebot.v11 import Message as QMessage

from nonebot.adapters.telegram import Bot as TBot
from nonebot.adapters.telegram.event import MessageEvent as TMessageEvent
from nonebot.adapters.telegram import Message as TMessage

from nonebot import on_command

echo = on_command('echo')

@echo.handle()
async def Techo(bot: TBot, event: TMessageEvent):
    await echo.finish(TMessage(str(event.get_message())[5:]))

@echo.handle()
async def Qecho(bot: QBot, event: QMessageEvent):
    await echo.finish(QMessage(str(event.get_message())[5:]))
