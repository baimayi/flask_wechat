# -*- encoding: utf-8 -*-

# 实际部署不需要
from flask import Blueprint,send_from_directory
from application import app

root_static = Blueprint('static', __name__)

@root_static.route('/<path:filename>')
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)