# -*- coding: utf-8 -*-
"""Running Environment: Python 3.5.1"""

from urllib import request
from urllib.error import HTTPError

class API(object):
    """API class.""" # http://open.renren.com/wiki/English_version_for_API2

    def __init__(self, access_token_pool):
        """Import access_token pool"""
        self.tokens = access_token_pool

    def __getattr__(self, attr):
        return Wrapper(self, attr)

class Wrapper():
    URL = 'https://api.renren.com/v2/'

    def __init__(self, api, name):
        self.api = api
        self.name = name

    def __getattr__(self, attr):
        return Wrapper(self.api, "%s/%s" % (self.name, attr))

    def __call__(self, **kw):
        url = self.URL + self.name + encode_Params(**kw)
        return http_Request(self.api, url)

def encode_Params(**kw):
    """Return a URL-encoded string for a dictionary of paramteres."""
    s = '?'
    for k, v in kw.items():
        s = s + str(k) + '=' + str(v) + '&'
    return s.strip('&')

def http_Request(api, url0):
    while True:
        f = None
        url = url0 + "&access_token=%s" % api.tokens[0]
        try:
            f = request.urlopen(url)
            return f.read().decode('utf-8')
        except HTTPError as e:
            if error_Handling(api, e) == "Break":
                return None
        finally:
            if f:
                f.close()
            # print("token: " + self.tokens[0])

def error_Handling(api, e):
    """Extract error message"""
    message = e.read().decode('utf-8').split(':')[3].strip('\"}')
    if message == "invalid_authorization.INVALID-TOKEN":
        delete_Token(api)
    elif message == "forbidden.APP_OVER_INVOCATION_LIMIT":
        change_Token(api)
    elif message == "invalid_request.USER_NOT_EXIST" or message == "forbidden.NO_RIGHT":
        return "Break"
    else:
        print(message)
        return "Break"

def change_Token(api):
    """Change the token if it overs the limit"""
    api.tokens.append(api.tokens[0])
    api.tokens.pop(0)
    print("New-TOKEN:%s" % api.tokens[0])

def delete_Token(api):
    """Delete the token if it is invalid"""
    print("Invalid-TOKEN:%s" % api.tokens[0])
    api.tokens.pop(0)
