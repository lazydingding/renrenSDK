# -*- coding: utf-8 -*-
"""Running Environment: Python 3.5.1"""

from urllib import request
from urllib.error import HTTPError

class API(object):
    """API class.""" # http://open.renren.com/wiki/English_version_for_API2
    URL = 'https://api.renren.com/v2/'

    def __init__(self, access_token_pool):
        """Import access_token pool"""
        self.tokens = access_token_pool

    def __change_Token(self):
        """Change the token if it overs the limit"""
        self.tokens.append(self.tokens[0])
        self.tokens.pop(0)
        print("New-TOKEN:%s" % self.tokens[0])

    def __delete_Token(self):
        """Delete the token if it is invalid"""
        print("Invalid-TOKEN:%s" % self.tokens[0])
        self.tokens.pop(0)

    def __error_Handling(self, e):
        """Extract error message"""
        message = e.read().decode('utf-8').split(':')[3].strip('\"}')
        if message == "invalid_authorization.INVALID-TOKEN":
            self.__delete_Token()
        elif message == "forbidden.APP_OVER_INVOCATION_LIMIT":
            self.__change_Token()
        elif message == "invalid_request.USER_NOT_EXIST" or message == "forbidden.NO_RIGHT":
            return "Break"
        else:
            print(message)
            return "Break"

    def __http_Request(self, url0):
        while True:
            f = None
            url = url0 + "&access_token=%s" % self.tokens[0]
            try:
                f = request.urlopen(url)
                return f.read().decode('utf-8')
            except HTTPError as e:
                if self.__error_Handling(e) == "Break":
                    return None
            finally:
                if f:
                    f.close()
                # print("token: " + self.tokens[0])

    def friend_list(self, userId, pageSize=10000):
        """Obtain a user's friend ID list"""
        url = self.URL + "friend/list?userId=%s&pageSize=%s" % (userId, pageSize)
        return self.__http_Request(url)

    def profile(self, userId):
        """Get the user's home information, including a variety of statistical data."""
        url = self.URL + "profile/get?userId=%s" % (userId)
        return self.__http_Request(url)
