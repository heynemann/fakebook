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

fakebook provides three routes: "/login", "/token" and "/userdata". The flow is:

* get a login code from "/login?redirect_uri=<your site>" using an URI that points to where you want to receive the code;
* get an acess_token from "/token?access_token=<your token>";
* get user details using the provided access token from "/userdata".
