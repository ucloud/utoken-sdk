import base_api


class TokenAction(object):
    create = 'CreateUTokenToken'
    update = 'UpdateUTokenToken'
    query = 'GetUTokenList'


class TokenParam(object):
    def __init__(self, client_id="", project_id=0, token_name="", update_method=0, period=0, token_id=0):
        if (not isinstance(client_id, str) and not isinstance(client_id, unicode)) \
            or not isinstance(project_id, int) \
            or (not isinstance(token_name, str) and not isinstance(token_name, unicode)) \
            or not isinstance(update_method, int) \
            or not isinstance(period, int)        \
            or not isinstance(token_id, int):
            raise Exception("Tokenparam initialize with invalid parameters")
        self._client_id = client_id
        self._project_id = project_id
        self._token_name = token_name
        self._update_method = update_method
        self._period = period
        self._token_id = token_id

    def set(self, client_id="", project_id=0, token_name="", update_method=0, period=0, token_id=0):
        if (not isinstance(client_id, str) and not isinstance(client_id, unicode)) \
            or not isinstance(project_id, int) \
            or (not isinstance(token_name, str) and not isinstance(token_name, unicode)) \
            or not isinstance(update_method, int) \
            or not isinstance(period, int)        \
            or not isinstance(token_id, int):
            raise Exception("Tokenparam set with invalid parameters")
        if client_id:
            self._client_id = client_id
        if project_id:
            self._project_id = project_id
        if token_name:
            self._token_name = token_name
        if update_method:
            self._update_method = update_method
        if period:
            self._period = period
        if token_id:
            self._token_id = token_id

    def get_create_param(self):
        if not self._project_id or not self._client_id or not self._token_name       \
                or not self._update_method or not self._period:
            raise Exception("invalid params to create token")
        return {
            "ProjectID":    self._project_id,
            "ClientID":     self._client_id,
            "TokenName":    self._token_name,
            "UpdateMethod": self._update_method,
            "Period":       self._period
        }

    def get_update_param(self):
        if not self._client_id or not self._project_id or not self._token_id or not self._update_method:
            raise Exception("invalid params to update token")
        return {
            "ClientID":      self._client_id,
            "ProjectID":     self._project_id,
            "UpdateMethod":  self._update_method,
            "TokenID":       self._token_id
        }

    def get_query_param(self):
        if not self._client_id or not self._project_id:
            raise Exception("invalid params to get token list")
        return {
            "ClientID":  self._client_id,
            "ProjectID": self._project_id
        }


class TokenApi(base_api.BaseApi):
    def __init__(self, ucloud_instance, region, zone):
        super(TokenApi, self).__init__(ucloud_instance, region=region, zone=zone)

    def create(self, token_param):
        return super(TokenApi, self).post(TokenAction.create, token_param.get_create_param())

    def update(self, token_param):
        return super(TokenApi, self).post(TokenAction.update, token_param.get_update_param())

    def get(self, token_param):
        return super(TokenApi, self).post(TokenAction.query, token_param.get_query_param())


