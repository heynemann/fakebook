#!/usr/bin/python
# -*- coding: utf-8 -*-

from derpconf.config import Config  # NOQA

Config.define('LOGIN_LATENCY', 100, 'Login route latency in MS. 0 to none.', 'General')
Config.define('TOKEN_LATENCY', 100, 'Token route latency in MS. 0 to none.', 'General')
Config.define('USERDATA_LATENCY', 100, 'User Data route latency in MS. 0 to none.', 'General')
