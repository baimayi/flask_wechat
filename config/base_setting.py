# -*- encoding: utf-8 -*-

# SERVER_PORT = 8999
# DEBUG = False
# SQLALCHEMY_ECHO = False

# 因为win无法使用export ops_config=local
SERVER_PORT = 8999
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:000000@192.168.159.145/mysql'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'utf-8'