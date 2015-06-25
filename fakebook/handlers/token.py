#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from json import dumps
from base64 import b64encode
from uuid import uuid4
import random
from datetime import datetime

from tornado.gen import coroutine
from swnamer import NameGenerator

from fakebook.handlers import BaseHandler


class TokenHandler(BaseHandler):
    @coroutine
    def get(self):
        code = self.get_argument('code')
        token = b64encode(code + str(uuid4()))
        self.write(dumps({
            'access_token': token,
        }))


class UserDataHandler(BaseHandler):
    @coroutine
    def get(self):
        token = self.get_argument('access_token')
        fields = [field for field in self.get_argument('fields', '').split(',') if field]
        generator = NameGenerator(lowercase=True, separator=" ")

        name = generator.generate()
        user_id = b64encode(str(uuid4()))
        username = name.lower().replace(' ', '.')
        birthday = datetime(day=25, month=4, year=random.randint(1970, 2000))
        email = "%s@gmail.com" % username
        gender = random.choice(['F', 'M'])
        names = name.split()
        first_name = names[0]
        middle_name = ' '.join(names[1:-1])
        last_name = names[-1]
        relationship = random.choice(['Single', 'Married', 'Complicated'])
        verified = True

        userdata = {
            "id": user_id,
            "access_token": token,
            "birthday": birthday.strftime("%m/%d/%Y"),
            "email": email,
            "first_name": first_name,
            "gender": gender,
            "is_verified": verified,
            "last_name": last_name,
            "middle_name": middle_name,
            "relationship_status": relationship
        }

        if fields:
            data = {
                'access_token': token
            }
            for field in fields:
                data[field] = userdata[field]
            userdata = data

        self.write(dumps(userdata))
