# -*- encoding: utf-8 -*-

# SERVER_PORT = 8999
# DEBUG = False
# SQLALCHEMY_ECHO = False
# AUTH_COOKIE_NAME = "mooc_food"
## 过滤url
# IGNORE_URLS = [
#     "^/user/login"
# ]
# IGNORE_CHECK_LOGIN_URLS = [
#     "^/static",
#     "^/favicon.ico"
# ]
# PAGE_SIZE = 50
# PAGE_DISPLAY = 10
# STATUS_MAPPING = {
#   "1":"正常",
#    "0": "已删除"
# }
# MINA_APP = {
#   'appid':'',
#   'appkey':''
# }


# 因为win无法使用export ops_config=local
SERVER_PORT = 8999
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:000000@192.168.159.145/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'utf-8'
AUTH_COOKIE_NAME = "mooc_food"

## 过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]
PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
  "1":"正常",
   "0":"已删除"
}