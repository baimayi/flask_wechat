# -*- encoding: utf-8 -*-
from flask import Blueprint
route_api = Blueprint('api_page', __name__)
from web.controllers.api.Member import *

@route_api.route('/')
def index():
    return "Main Api V0.2~"