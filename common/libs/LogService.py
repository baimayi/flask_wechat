# -*- encoding: utf-8 -*-
from common.models.log.AppAccessLog import AppAccessLog
from common.models.log.AppErrorLog import AppErrorLog
from flask import request, g
import json
from common.libs.Helper import getCurrentDate
from application import app, db


class LogService():

    @staticmethod
    def addAccessLog():
        target = AppAccessLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.ip = request.remote_addr
        target.query_params = json.dumps(request.values.to_dict())
        if 'current_user' in g and g.current_user is not None:
            target.uid = g.current_user.uid
        target.ua = request.headers.get("User-Agent")
        target.create_time = getCurrentDate()

        db.session.add(target)
        db.session.commit()
        return True

    @staticmethod
    def addErrorLog(content):
        target = AppErrorLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.query_params = json.dumps(request.values.to_dict())
        target.content = content
        target.create_time = getCurrentDate()

        db.session.add(target)
        db.session.commit()
