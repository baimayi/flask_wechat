# -*- encoding: utf-8 -*-


import hashlib
import base64
import random
import string
import request,json
from application import app


class MemberService():

    @staticmethod
    def geneAuthCode(member_info=None):
        m = hashlib.md5()
        str_encode = "%s-%s-%s" % (member_info.id, member_info.salt,member_info.status)
        m.update(str_encode.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))

    @staticmethod
    def getWeChatOpenId(code):
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(
        app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], cpde)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        openid = openid