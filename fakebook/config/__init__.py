#!/usr/bin/python
# -*- coding: utf-8 -*-

from derpconf.config import Config  # NOQA

Config.define(
    'CUSTOM_USERS',
    [],
    'List of users that Fakebook will return data for. If empty, random users will be used.',
    'General'
)

Config.define('REDISHOST', '127.0.0.1', 'Redis host to store user data', 'Redis')
Config.define('REDISPORT', 4444, 'Redis port to store user data', 'Redis')
Config.define('REDISPASS', '', 'Redis pass to store user data', 'Redis')

Config.define('LOGIN_LATENCY', 100, 'Login route latency in MS. 0 to none.', 'General')
Config.define('TOKEN_LATENCY', 100, 'Token route latency in MS. 0 to none.', 'General')
Config.define('USERDATA_LATENCY', 100, 'User Data route latency in MS. 0 to none.', 'General')
