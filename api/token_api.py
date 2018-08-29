import base_api


class TokenAction(object):
    create = 'CreateUTokenToken'
    update = 'UpdateUTokenToken'
    query = 'GetUTokenList'


class TokenParam(object):
    def __init__(self, client_id=0, top_orgid=0, project_id=0, account_id=0, token_name="", update_method=0, period=0, token_id=0):
        self._client_id = client_id
        self._top_orgid = top_orgid
        self._project_id = project_id
        self._account_id = account_id
        self._token_name = token_name
        self._update_method = update_method
        self._period = period
        self._token_id = token_id

    def set(self, client_id=0, top_orgid=0, project_id=0, new_project_id=0, account_id=0, token_name="", update_method=0, period=0, token_id=0):
        if client_id:
            self._client_id = client_id
        if top_orgid:
            self._top_orgid = top_orgid
        if project_id:
            self._project_id = project_id
        if new_project_id:
            self._new_project_id = new_project_id
        if account_id:
            self._account_id = account_id
        if token_name:
            self._token_name = token_name
        if update_method:
            self._update_method = update_method
        if period:
            self._period = period
        if token_id:
            self._token_id = token_id


    def get_create_param(self):
        if not isinstance(self._top_orgid, int) or not self._top_orgid             \
            or not isinstance(self._project_id, int) or not self._project_id       \
            or not isinstance(self._account_id, int) or not self._account_id       \
            or not isinstance(self._client_id, int) or not self._client_id         \
            or not isinstance(self._token_name, str) or not self._token_name       \
            or not isinstance(self._update_method, int) or not self._update_method \
                or not isinstance(self._period, int) or not self._period:
            raise Exception("invalid params to create token")
        return {
            "TopOrgID":     self._top_orgid,
            "ProjectID":    self._project_id,
            "AccountID":    self._account_id,
            "ClientID":     self._client_id,
            "TokenName":    self._token_name,
            "UpdateMethod": self._update_method,
            "Period":       self._period
        }

    def get_update_param(self):
        if not isinstance(self._client_id, int) or not self._client_id                \
            or not isinstance(self._top_orgid, int) or not self._top_orgid            \
            or not isinstance(self._project_id, int) or not self._project_id          \
            or not isinstance(self._account_id, int) or not self._account_id          \
            or not isinstance(self._token_id, int) or not self._account_id            \
                or not isinstance(self._update_method, int) or not self._update_method:
            raise Exception("invalid params to update token")
        return {
            "ClientID":      self._client_id,
            "TopOrgID":      self._top_orgid,
            "ProjectID":     self._project_id,
            "AccountID":     self._account_id,
            "UpdateMethod":  self._update_method,
            "TokenID":       self._token_id
        }

    def get_query_param(self):
        if not isinstance(self._client_id, int) or not self._client_id       \
            or not isinstance(self._top_orgid, int) or not self._top_orgid   \
            or not isinstance(self._account_id, int) or not self._account_id \
                or not isinstance(self._project_id, int) or not self._project_id:
            raise Exception("invalid params to get token list")
        return {
            "ClientID":  self._client_id,
            "TopOrgID":  self._top_orgid,
            "ProjectID": self._project_id,
            "AccountID": self._account_id
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


