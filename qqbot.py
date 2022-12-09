# -*- coding: utf-8 -*-

#import os
from chatgpt.api import ChatGPT
import botpy
from botpy import logging
from botpy.types.message import Reference
from botpy.message import Message
# from botpy.ext.cog_yaml import read

# test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml")) 在config.yaml中获取配置
test_config = {'appid': "",#你机器人的 appid在https://bot.q.qq.com/wiki/develop/api/#%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E 中说明
               'token': ""}#你机器人的token在 https://bot.q.qq.com/wiki/develop/api/#%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E 中说明
chatgpttoken='' # chatgpttoken是在https://chat.openai.com/chat中cookie名为__Secure-next-auth.session-token获取的
_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        # 使用chatgpt回复[24:]是为了过滤@机器人的内容
        _log.info(message.content)
        response = chat.send_message(message.content[24:])
        # 构造消息发送请求数据对象
        message_reference = Reference(message_id=message.id)
        # 通过api发送回复消息
        await self.api.post_message(channel_id=message.channel_id, content=str(response.content), msg_id=message.id,message_reference=message_reference, )
        _log.info(response.content)


if __name__ == "__main__":
    chat = ChatGPT(session_token=(chatgpttoken))
    chat.authenticate()
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
