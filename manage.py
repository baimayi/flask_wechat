#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask_script import Server
from application import app, manager
import www

# web runserver
manager.add_command("runserver", Server(
    host='0.0.0.0', port=app.config["SERVER_PORT"], use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':

    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
