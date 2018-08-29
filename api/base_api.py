# -*- coding: utf-8 -*-
import copy
import ucloud
class BaseApi(object):
    """The Base api for utoken
    """

    def __init__(self, ucloud_instance, region, zone):
        self._ucloud_instance = ucloud_instance
        self._base_params = {
            'Region':    region,
            'Zone':      zone
        }

    def _check_params(self, params):
        pass

    def post(self, action, params):
        print 'base_api post'
        _params = {}
        _params.update(self._base_params)
        _params.update(params)
        print 'base_api post'
        print params
        return self._ucloud_instance.post(action, params)

