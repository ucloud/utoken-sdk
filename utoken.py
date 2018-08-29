import copy
from api import client_api
from api import token_api
from ucloud import ucloud
from globalvar import globalvar

class UTokenSDK(object):

    def __init__(self, public_key, private_key, region=globalvar.DEFAULT_REGION, zone=globalvar.DEFAULT_ZONE):
        self._ucloud_instance = ucloud.UCloudClient(public_key, private_key)
        self._client_instance = client_api.ClientApi(self._ucloud_instance, region, zone)
        self._token_instance = token_api.TokenApi(self._ucloud_instance, region, zone)
        self._client_params = client_api.ClientParam()
        self._token_params = token_api.TokenParam()

    def set_params(self, top_orgid, project_id, account_id):
        self._client_params.set(top_orgid=top_orgid, project_id=project_id, account_id=account_id)
        self._token_params.set(top_orgid=top_orgid, project_id=project_id, account_id=account_id)

    """ 1. client operation
    """
    def create_client(self, client_name, description=""):
        client_params = copy.deepcopy(self._client_params)
        client_params.set(client_name=client_name, description=description)
        print 'UTokenSDK create client'
        return self._client_instance.create(client_params)

    def delete_client(self, client_id):
        client_params = copy.deepcopy(self._client_params)
        client_params.set(client_id=client_id)
        return self._client_instance.delete(client_params)

    def update_client(self, client_id, client_name="", description="", new_project_id=0):
        client_params = copy.deepcopy(self._client_params)
        client_params.set(client_id=client_id, client_name=client_name,
                                description=description, new_project_id=new_project_id)
        return self._client_instance.update(client_params)

    def get_client(self):
        return self._client_instance.get(self._client_params)

    """ 2. token operation
    """
    def create_token(self, client_id, token_name, update_method, period):
        token_params = copy.deepcopy(self._token_params)
        token_params.set(client_id=client_id, token_name=token_name, update_method=update_method, period=period)
        return self._token_instance.create(token_params)

    def update_token(self, client_id, token_id, update_method):
        token_params = copy.deepcopy(self._token_params)
        token_params.set(client_id=client_id, token_id=token_id, update_method=update_method)
        return self._token_instance.update(token_params)

    def get_token_list(self, client_id):
        token_params = copy.deepcopy(self._token_params)
        token_params.set(client_id=client_id)
        return self._token_instance.get(token_params)
