import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'


def response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }

    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:

        return None


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def tuling_reply(msg):
    if True or msg['isAt']:
        defaultReply = 'I received: ' + msg['Text']
        reply = response(msg['Text'])

        return reply or defaultReply


# if msg['isAt']:


itchat.auto_login(hotReload=True)
itchat.run()
