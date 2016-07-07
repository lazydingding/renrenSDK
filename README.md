# Renren Python3 SDK

This SDK is a stand-alone Python script which provides

* API calling wrapper

for [人人网 renren.com](http://www.renren.com)

This SDK is designed for researchers to obtain social network data from renren.com (a typical undirected network). In this case, only Reading Interfaces will be taken into consideration by this SDK.

Developed and maintained by [Luping Yu](https://github.com/lazydingding). Please feel free to report bugs and
your suggestions at [here](https://github.com/lazydingding/renren_sdk).

## Installation

You can install the SDK via pip.

```
pip install renrensdk
```

## Get Access Token
Renren OAuth2.0 currently supports Bearer Access Token. Bearer access token does not require the signature of the request. Besides, this kind of access token valid for one month.

There are two methods to get access token.
### Recommended Approach ###
Step 1- Register Application: Register your open platform application: [Register Application](http://app.renren.com/developers/newapp).

Step 2- Get Access Token: Visit [Renren Dev Tools](http://dev.renren.com/tools) to obtain access token

### Standard Approach (OAuth2 authentication) ###
The document about OAuth2.0 authorization process could be found at [OAuth2.0](http://open.renren.com/wiki/English_version_for_OAuth2.0).

### API Rate Limits
The rate limit for each application is **150 requests / 1-hour window**. To upgrade this rate-limit, developers need to register plenty of applications to obtain enough access tokens. We suggest developers import an "access token pool" when initializing the API instance. This SDK will change token automatically when it overs the limit.

We also found that the average time consume for each API calling is about 1s. In this case, **25 tokens** (3750 requests / 1-hour window) are enough to make sure the API requests will continuous running.

## Initialize API instance

After getting your access token(s), you can create the API instance now:

```python
from renren import API

access_token_pool = ["token1", "token2", ..., "tokenN"]

api = API(access_token_pool)
```

## How to call a particular API (API 2.0)

The APIs are listed at [Renren API2 Documentation]
(http://open.renren.com/wiki/English_version_for_API2).
You can call an API using the APIClient's.  Remove "/v2/" and replace "/" with ".".  For example,

```python
print (api.profile.get(userId="383202003"))
print (api.friend.list(userId="383202003", pageSize=10000))
```
