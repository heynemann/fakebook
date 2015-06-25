#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from tornado.testing import gen_test
from preggy import expect

from tests.base import TestCase


class LoginHandlerTestCase(TestCase):
    @gen_test
    def test_responds_with_code(self):
        response = yield self.fetch('/login?redirect_uri=http://google.com', follow_redirects=False)
        expect(response.code).to_equal(302)
        expect(response.headers['Location']).to_include('http://google.com?code=')

    @gen_test
    def test_fails_if_no_redirect_provided(self):
        response = yield self.fetch('/login', follow_redirects=False)
        expect(response.code).to_equal(400)
