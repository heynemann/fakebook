#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>


from cow.server import Server
from cow.plugins.sync_redis_plugin import RedisPlugin

from fakebook.handlers.login import LoginHandler
from fakebook.handlers.token import TokenHandler, UserDataHandler


def main():
    FakebookServer.run()


class FakebookServer(Server):
    def __init__(self, debug=None, *args, **kw):
        super(FakebookServer, self).__init__(*args, **kw)

        self.force_debug = debug

    def initialize_app(self, *args, **kw):
        super(FakebookServer, self).initialize_app(*args, **kw)

        if self.force_debug is not None:
            self.debug = self.force_debug

    def get_handlers(self):
        handlers = [
            ('/login', LoginHandler),
            ('/token', TokenHandler),
            ('/userdata', UserDataHandler)
        ]

        return tuple(handlers)

    def get_plugins(self):
        return [
            RedisPlugin
        ]

if __name__ == '__main__':
    main()
