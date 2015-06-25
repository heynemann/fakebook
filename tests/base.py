#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fakebook.
# https://github.com/heynemann/fakebook

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

import os
from base64 import b64encode
from uuid import uuid4

from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from cow.testing import CowTestCase

from fakebook.config import Config
from fakebook.server import FakebookServer


class TestCase(CowTestCase):
    def tearDown(self):
        self.server.application.redis.flushdb()
        super(TestCase, self).tearDown()

    def get_config(self):
        return dict(
            REDISHOST='localhost',
            REDISPORT=4448,
        )

    def get_app(self):
        app = super(TestCase, self).get_app()
        app.http_client = AsyncHTTPClient(self.io_loop)
        self.http_client = app.http_client
        return app

    @gen.coroutine
    def fetch(self, path, follow_redirects=None, **kwargs):
        """Convenience method to synchronously fetch a url.

        The given path will be appended to the local server's host and
        port.  Any additional kwargs will be passed directly to
        `.AsyncHTTPClient.fetch` (and so could be used to pass
        ``method="POST"``, ``body="..."``, etc).
        """
        req = HTTPRequest(self.get_url(path), follow_redirects=follow_redirects)
        response = yield self.http_client.fetch(req, self.stop, raise_error=False, **kwargs)
        raise gen.Return(response)

    def get_random_code(self):
        return b64encode(str(uuid4()))

    def get_server(self):
        cfg = Config(**self.get_config())
        debug = os.environ.get('DEBUG_TESTS', 'False').lower() == 'true'

        self.server = FakebookServer(config=cfg, debug=debug)
        return self.server
