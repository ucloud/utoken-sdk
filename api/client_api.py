import base_api


class ClientAction(object):
    create = 'CreateUTokenClient'
    delete = 'DeleteUTokenClient'
    update = 'UpdateUTokenClient'
    query = 'GetUTokenClient'


class ClientParam(object):
    def __init__(self, client_id=0, top_orgid=0, project_id=0, new_project_id=0, account_id=0, client_name="", description=""):
        self._client_id = client_id
        self._top_orgid = top_orgid
        self._project_id = project_id
        self._new_project_id = new_project_id
        self._account_id = account_id
        self._client_name = client_name
        self._description = description

    def set(self, client_id=0, top_orgid=0, project_id=0, new_project_id=0, account_id=0, client_name="", description=""):
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
        if client_name:
            self._client_name = client_name
        if description:
            self._description = description


    def get_create_param(self):
        if not isinstance(self._top_orgid, int) or not self._top_orgid       \
            or not isinstance(self._project_id, int) or not self._project_id \
            or not isinstance(self._account_id, int) or not self._account_id \
                or not isinstance(self._client_name, str) or not self._client_name:
            raise Exception("invalid params to create client")
        return {
            "TopOrgID":    self._top_orgid,
            "ProjectID":   self._project_id,
            "AccountID":   self._account_id,
            "ClientName":  self._client_name,
            "Description": self._description
        }

    def get_delete_param(self):
        if not isinstance(self._client_id, int) or not self._client_id       \
            or not isinstance(self._account_id, int) or not self._account_id \
            or not isinstance(self._top_orgid, int) or not self._top_orgid   \
                or not isinstance(self._project_id, int) or not self._project_id :
            raise Exception("invalid params to delete client")
        return {
            "ClientID":  self._client_id,
            "AccountID": self._account_id,
            "TopOrgID":  self._top_orgid,
            "ProjectID": self._project_id
        }

    def get_update_param(self):
        if not isinstance(self._client_id, int) or not self._client_id                \
            or not isinstance(self._top_orgid, int) or not self._top_orgid            \
            or not isinstance(self._project_id, int) or not self._project_id          \
            or not isinstance(self._account_id, int) or not self._account_id          \
            or not isinstance(self._client_name, str)                                 \
            or not isinstance(self._description, str)                                 \
            or not isinstance(self._new_project_id, int)                              \
                or (not self._client_name and not self._description and not self._new_project_id):
            raise Exception("invalid params to update client")
        return {
            "ClientID":      self._client_id,
            "TopOrgID":      self._top_orgid,
            "ProjectID":     self._project_id,
            "AccountID":     self._account_id,
            "ClientName":    self._client_name,
            "Description":   self._description,
            "NewProjectID":  self._new_project_id
        }

    def get_query_param(self):
        if not isinstance(self._top_orgid, int) or not self._top_orgid        \
                or not isinstance(self._project_id, int) or not self._project_id:
            raise Exception("invalid params to get client info")
        return {
            "TopOrgID": self._top_orgid,
            "ProjectID": self._project_id,
            "AccountID": self._account_id
        }


class ClientApi(base_api.BaseApi):
    def __init__(self, ucloud_instance, region, zone):
        super(ClientApi, self).__init__(ucloud_instance, region=region, zone=zone)

    def create(self, client_param):
        print 'client_api create'
        return super(ClientApi, self).post(ClientAction.create, client_param.get_create_param())

    def delete(self, client_param):
        print 'client_api delete'
        return super(ClientApi, self).post(ClientAction.delete, client_param.get_delete_param())

    def update(self, client_param):
        return super(ClientApi, self).post(ClientAction.update, client_param.get_update_param())

    def get(self, client_param):
        return super(ClientApi, self).post(ClientAction.query, client_param.get_query_param())


