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
from preggy import create_assertions

from tests.base import TestCase


@create_assertions
def to_be_one_of(topic, expected):
    '''Asserts that `topic > expected`.'''
    return topic in expected


class UserDataHandlerTestCase(TestCase):
    @gen_test
    def test_responds_with_userdata(self):
        response = yield self.fetch('/userdata?access_token=%s' % self.get_random_code())
        expect(response.code).to_equal(200)

        obj = loads(response.body)
        expect(obj).to_include('id')
        expect(obj['id']).not_to_be_empty()

        expect(obj).to_include("birthday")
        expect(obj["birthday"]).not_to_be_empty()

        expect(obj).to_include("email")
        expect(obj["email"]).not_to_be_empty()

        expect(obj).to_include("first_name")
        expect(obj).to_include("middle_name")
        expect(obj).to_include("last_name")

        expect(obj["first_name"]).not_to_be_empty()
        expect(obj["middle_name"]).not_to_be_empty()
        expect(obj["last_name"]).not_to_be_empty()

        expect(obj).to_include("gender")
        expect(obj['gender']).to_be_one_of(['M', 'F'])

        expect(obj).to_include("is_verified")
        expect(obj['is_verified']).to_be_true()

        expect(obj).to_include("relationship_status")
        expect(obj['relationship_status']).to_be_one_of(['Single', 'Married', 'Complicated'])
