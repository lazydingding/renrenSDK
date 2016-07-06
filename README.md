# Renren Python3 SDK

This SDK is a stand-alone Python script which provides

* API calling wrapper

for http://www.renren.com (renren.com 人人网)

This SDK is designed for researchers to obtain social network data from renren.com (a typical undirected network). In this case the only Reading Interfaces will be taken into consideration.

Developed and maintained by Luping Yu. Please feel free to report bugs and
your suggestions at [here](https://github.com/lazydingding/renren_sdk).

## Installation

You can install the SDK via pip.

```
pip install renrensdk
```

## Get Access Token

### Recommended Approach ###
Step 1- Register Application: Register your open platform Application: [Register Application](http://app.renren.com/developers/newapp).

Step 2- Get Access Token: Visit [Renren Dev Tools](http://dev.renren.com/tools) to obtain access token

### Standard Approach (OAuth2 authentication) ###
The document about OAuth2.0 authorization process could be found at [OAuth2.0](http://open.renren.com/wiki/English_version_for_OAuth2.0).

After getting Access Token, you can call the REST API using Access Token. For more information, please visit [API interface using instruction](http://open.renren.com/wiki/English_version_for_API2).

## Initialize API instance

After setting up your Access Token, you can create the API instance now:

```python
from renren import API

access_token = [token1, token2, ...]

api = API(access_token)
```

## How to call a particular API (API 2.0)

The APIs are listed at [Renren API2 Documentation]
(http://open.renren.com/wiki/English_version_for_API2).
You can call an API using the APIClient's.  Remove "/v2/" and replace "/" with ".".  For example,

```python
print (api.profile.get(userId="383202003"))
print (api.friend.list(userId="383202003", pageSize=10000))
```
