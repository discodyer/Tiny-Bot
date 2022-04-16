from nonebot.adapters.onebot.v11 import MessageEvent as QMessageEvent
from nonebot.adapters.onebot.v11 import Bot as QBot
from nonebot.adapters.onebot.v11 import Message as QMessage


from nonebot.adapters.telegram import Bot as TBot
from nonebot.adapters.telegram.event import MessageEvent as TMessageEvent
from nonebot.adapters.telegram import Message as TMessage

from nonebot import on_command

from . import checkin

fyCheckin = on_command("fy", aliases={"防疫", "防疫签到"}, priority=5)

@fyCheckin.handle()
async def QQ_fyCheckin(bot: QBot, event: QMessageEvent):
    print('ok')
    input_str = str(event.get_message())[4:]
    print(input_str)
    str_list = input_str.split(sep=' ', maxsplit=1)
    print(str_list)
    print(len(str_list[0]))
    print(len(str_list[1]))
    if len(str_list[0]) == 11 and len(str_list[1]) == 8:
        result = checkin.auto_checkin(str_list[0], str_list[1])
        if result == True:
            message="执行成功"
        else:
            message="执行失败"
    else:
        message="失败:输入不合法,正确输入/fy [手机号] [学号]"
    await fyCheckin.finish(message)


@fyCheckin.handle()
async def TG_fyCheckin(bot: TBot, event: TMessageEvent):
    print('ok')
    input_str = str(event.get_message())[4:]
    print(input_str)
    str_list = input_str.split(sep=' ', maxsplit=1)
    print(str_list)
    print(len(str_list[0]))
    print(len(str_list[1]))
    if len(str_list[0]) == 11 and len(str_list[1]) == 8:
        result = checkin.auto_checkin(str_list[0], str_list[1])
        if result == True:
            message="执行成功"
        else:
            message="执行失败"
    else:
        message="失败:输入不合法,正确输入/fy [手机号] [学号]"
    await fyCheckin.finish(message)


# @fy.handle()
# async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
#     plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
#     if plain_text:
#         matcher.set_arg("mobile", args)  # 如果用户发送了参数则直接赋值



# @fy.got("mobile", prompt="请输入手机号+学号")
# async def handle_city(city: Message = Arg(), your_info: str = ArgPlainText("mobile")):
#     if not len(your_info) == 20:
#         await fy.reject(city.template("失败:输入不合法,正确输入/fy [手机号] [学号]"))


#     city_weather = await get_weather(your_info)
#     await fy.finish(city_weather)


# async def get_weather(your_info: str) -> str:
#     str_list = your_info.split(sep=' ', maxsplit=1)
#     result = checkin.auto_checkin(str_list[0], str_list[1])
#     if result == True:
#         return "执行成功"
#     else:
#         return "执行失败"