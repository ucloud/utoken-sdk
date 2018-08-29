# -*- coding: utf-8 -*-
import hashlib
import json
import requests
from globalvar import globalvar


class UCloudClient(object):

    def __init__(self, public_key, private_key):
        self._base_url = globalvar.DEFAULT_API_URL
        if not public_key or not private_key:
            raise Exception('public_key, private_key cannot be empty')
        self._params = {
            'PublicKey': public_key,
        }
        self._private_key = private_key

    def _verify_ac(self, params):
        items = params.items()
        items.sort()
        params_str = ""
        for key, value in items:
            params_str += str(key) + str(value)
        params_str += self._private_key
        hash_new = hashlib.sha1()
        hash_new.update(params_str)
        hash_value = hash_new.hexdigest()
        return hash_value

    def post(self, action, params):
        _params = dict(self._params, **params)
        _params['Action'] = action
        _params['Signature'] = self._verify_ac(_params)
        url = self._base_url + '?Action=' + action
        print url
        print _params
        r = requests.post(self._base_url, data=json.dumps(_params), timeout=10, verify=True, headers={'Content-Type':'application/json'})
        print r.text
        print r.content

        return r.status_code, json.loads(r.text)


