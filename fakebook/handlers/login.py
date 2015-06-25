#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from base64 import b64encode
from uuid import uuid4

from tornado.gen import coroutine
from tornado.web import asynchronous

from fakebook.handlers import BaseHandler


class LoginHandler(BaseHandler):
    @coroutine
    @asynchronous
    def get(self):
        self.application.io_loop.call_later(self.application.config.LOGIN_LATENCY / 1000.0, self.handle_login)

    def handle_login(self):
        code = b64encode(str(uuid4()))
        url = "%s?code=%s" % (self.get_argument('redirect_uri'), code)
        self.redirect(url)
        self.finish()
