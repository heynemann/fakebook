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

from fakebook.handlers import BaseHandler


class LoginHandler(BaseHandler):
    @coroutine
    def get(self):
        code = b64encode(str(uuid4()))
        url = "%s?code=%s" % (self.get_argument('redirect_uri'), code)
        self.redirect(url)
