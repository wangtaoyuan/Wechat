# encoding=utf-8

import itchat
import requests


def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api'  # 图灵机器人API
    data = {
        'key': 'fe15f4cf351f4d2b95d601d86ef898c0',
        'info': msg,  # 发出的消息
        'userid': 'w机器人',
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    return get_response(msg['Text'])


itchat.auto_login(True)
itchat.run()
