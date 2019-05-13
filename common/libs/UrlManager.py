# -*- encoding: utf-8 -*-
import time
from config.local_setting import RELEASE_VERSION


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s" % (int(time.time())
                      ) if not RELEASE_VERSION else RELEASE_VERSION
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)
