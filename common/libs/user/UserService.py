# -*- encoding: utf-8 -*-

import hashlib
import base64
import random
import string


class UserService():

    @staticmethod
    def geneAuthCode(user_info):
        m = hashlib.md5()
        str_encode = "%s-%s-%s-%s" % (user_info.uid, user_info.login_name,
                                      user_info.login_pwd, user_info.login_salt)
        m.update(str_encode.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        str_encode = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str_encode.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))