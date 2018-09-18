# -*- coding: utf-8 -*-
import copy
import ucloud
class BaseApi(object):
    """The Base api for utoken
    """

    def __init__(self, ucloud_instance, region="", zone=""):
        if (not isinstance(region, str) and not isinstance(region, unicode)) \
            or (not isinstance(zone, str) and not isinstance(zone, unicode)) \
                or not region or not zone:
            raise Exception("BaseApi initialize with invalid paramters")
        self._ucloud_instance = ucloud_instance
        self._base_params = {
            'Region':    region.strip(),
            'Zone':      zone.strip()
        }

    def _check_params(self, params):
        pass

    def post(self, action, params):
        if not isinstance(params, dict):
            raise Exception("BaseApi post with invalid params, not dict")
        print 'base_api post'
        _params = {}
        _params.update(self._base_params)
        _params.update(params)
        print 'base_api post'
        print params
        return self._ucloud_instance.post(action, params)

