# -*- coding: utf-8 -*-
import hashlib
import json
import requests
#import sys
#sys.path.append("../")
from globalvar import globalvar


class UCloudClient(object):

    def __init__(self, public_key, private_key):
        self._base_url = globalvar.DEFAULT_API_URL.strip()
        if (not isinstance(public_key, str) and not isinstance(public_key, unicode)) \
                or (not isinstance(private_key, str) and not isinstance(private_key, unicode)) \
            or not public_key.strip() or not private_key.strip():
            raise Exception('UCloudClient initialize fail with invalid public_key or private_key')
        self._params = {
            'PublicKey': public_key.strip(),
        }
        self._private_key = private_key.strip()

    def _verify_ac(self, params):
        items = params.items()
        items.sort()
        params_str = ""
        for key, value in items:
            params_str += str(key) + str(value)
        print params_str
        params_str += self._private_key
        hash_new = hashlib.sha1()
        hash_new.update(params_str)
        hash_value = hash_new.hexdigest()
        return hash_value

    def post(self, action, params):
        if (not isinstance(action, str) and not isinstance(action, unicode)) \
                or not isinstance(params, dict):
            raise Exception("UCloudClient post with invalid paramters")
        _params = dict(self._params, **params)
        _params['Action'] = action.strip()
        _params['Signature'] = self._verify_ac(_params)
        url = self._base_url + '?Action=' + action.strip()
        print url
        print _params
        r = requests.post(self._base_url, data=json.dumps(_params), timeout=10, verify=True, headers={'Content-Type':'application/json'})
        print r.text
        if r.status_code != 200:
            return r.status_code, r.text
        return r.status_code, json.loads(r.text)

    def get(self, action, params):
        if (not isinstance(action, str) and not isinstance(action, unicode)) \
                or not isinstance(params, dict):
            raise Exception("UCloudClient post with invalid paramters")
        _params = dict(self._params, **params)
        _params['Action'] = action.strip()
        _params['Signature'] = self._verify_ac(_params)
        r = requests.get(self._base_url, params=_params, timeout=10, verify=True)
        if r.status_code != 200:
            return r.status_code, r.text
        return r.status_code, json.loads(r.text)


if __name__ == '__main__':

    params = {
        "Token": "dfakqw234uejriwejrow",
        "Region": "pre",
        "Zone": "pre",
        "Number": 123456,
    }

    public_key = ""
    private_key = ""
    client = UCloudClient(public_key, private_key)
    print client.post("GetUAIServiceTokenInfo", params)
    '''client.get("GetUAIServiceTokenInfo", params)'''
