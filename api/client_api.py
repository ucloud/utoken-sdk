import base_api


class ClientAction(object):
    create = 'CreateUTokenClient'
    delete = 'DeleteUTokenClient'
    update = 'UpdateUTokenClient'
    query = 'GetUTokenClient'


class ClientParam(object):
    def __init__(self, client_id="", project_id=0, business_group="", client_name="", description=""):
        if (not isinstance(client_id, str) and not isinstance(client_id, unicode)) \
            or not isinstance(project_id, int) \
            or (not isinstance(business_group, str) and not isinstance(business_group, unicode)) \
            or (not isinstance(client_name, str) and not isinstance(client_name, unicode))    \
                or (not isinstance(description, str) and not isinstance(description, unicode)):
            raise Exception("ClientParam initialize with invalid parameters")
        self._client_id = client_id.strip()
        self._project_id = project_id
        self._business_group = business_group.strip()
        self._client_name = client_name.strip()
        self._description = description.strip()

    def set(self, client_id="", project_id=0, business_group="", client_name="", description=""):
        if (not isinstance(client_id, str) and not isinstance(client_id, unicode)) \
            or not isinstance(project_id, int) \
            or (not isinstance(business_group, str) and not isinstance(business_group, unicode)) \
            or (not isinstance(client_name, str) and not isinstance(client_name, unicode))    \
                or (not isinstance(description, str) and not isinstance(description, unicode)):
            raise Exception("ClientParam set with invalid parameters")
        if client_id.strip():
            self._client_id = client_id.strip()
        if project_id:
            self._project_id = project_id
        if business_group.strip():
            self._business_group = business_group.strip()
        if client_name.strip():
            self._client_name = client_name.strip()
        if description.strip():
            self._description = description.strip()

    def get_create_param(self):
        if not self._project_id or not self._business_group or not self._client_name:
            raise Exception("invalid params to create client")
        return {
            "ProjectID":   self._project_id,
            "ClientName":  self._client_name,
            "BusinessGroup": self._business_group,
            "Description": self._description
        }

    def get_delete_param(self):
        if not self._client_id or not self._project_id :
            raise Exception("invalid params to delete client")
        return {
            "ClientID":  self._client_id,
            "ProjectID": self._project_id
        }

    def get_update_param(self):
        if not self._client_id or not self._project_id    \
                or (not self._client_name and not self._description and not self._business_group):
            raise Exception("invalid params to update client")
        return {
            "ClientID":      self._client_id,
            "ProjectID":     self._project_id,
            "ClientName":    self._client_name,
            "Description":   self._description,
            "BusinessGroup":  self._business_group
        }

    def get_query_param(self):
        if not self._project_id:
            raise Exception("invalid params to get client info")
        return {
            "ProjectID": self._project_id
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


