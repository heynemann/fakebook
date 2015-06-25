![Fakebook](https://raw.githubusercontent.com/heynemann/fakebook/master/fakebook.png)

# Introduction

fakebook is a facebook API simulator meant for test purposes.

It should behave similar to what facebook's own API does.

# Installing

It's as simple as:

    $ pip install fakebook_server

# Usage

After installing, you'll get a command called 'fakebook'. For more info, run:

    $ fakebook --help

Running fakebook is as easy as:

    $ fakebook

If you want to see output:

    $ fakebook -vvv

To specify your own configuration file (more on configuration values later):

    $ fakebook -c ./path/to/my.conf

# Routes

fakebook provides three routes: "/login", "/token" and "/me". The flow is:

* get a login code from "/login?redirect_uri=<your site>" using an URI that points to where you want to receive the code;
* get an acess_token from "/token?code=<your code>";
* get user details using the provided access token from "/me?access_token=<your access_token>".

# Configuration

By default fakebook uses a latency of 100ms in each route, but that's configurable. If you pass a configuration file to fakebook,
use the following format:

    ################################### General ####################################

    ## Login route latency in MS. 0 to none.
    ## Defaults to: 100
    LOGIN_LATENCY = 100

    ## Token route latency in MS. 0 to none.
    ## Defaults to: 100
    TOKEN_LATENCY = 100

    ## User Data route latency in MS. 0 to none.
    ## Defaults to: 100
    USERDATA_LATENCY = 100

    ################################################################################

# Contributing

Just Fork, Commit and Pull Request. Rise and Repeat.

# License

This project is MIT licensed.
