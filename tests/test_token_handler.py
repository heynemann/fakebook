#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from json import loads

from tornado.testing import gen_test
from preggy import expect

from tests.base import TestCase


class TokenHandlerTestCase(TestCase):
    @gen_test
    def test_responds_with_code(self):
        response = yield self.fetch('/token?code=%s' % self.get_random_code())
        expect(response.code).to_equal(200)

        obj = loads(response.body)
        expect(obj).to_include('access_token')
        expect(obj['access_token']).not_to_be_empty()

    @gen_test
    def test_fails_if_no_code_provided(self):
        response = yield self.fetch('/token')
        expect(response.code).to_equal(400)
