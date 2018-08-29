import sys
import getopt
import json
import utoken

options = ["cmd=", "client_name=", "description=", "client_id=", "new_project_id=",
           "token_name=", "update_method=", "period=", "token_id="]
cmd_options = ["create_client", "delete_client", "update_client", "get_client",
               "create_token", "update_token", "get_token"]

def print_result(type, res):
    print '#'*20, '  {}  '.format(type), '#'*20
    print res
    print '#'*60

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print 'python {} --cmd {} [optional]'.format(sys.argv[0], options)
        print 'optional options:'
        for opt in options:
            print '--{}'.format(opt)
        sys.exit()
    opts, args = getopt.getopt(sys.argv[1:], "hi:o", options)
    params = {}
    for name, value in opts:
        if name == "--cmd":
            params["cmd"] = value
        elif name == "--client_name":
            params["client_name"] = value
        elif name == "--description":
            params["description"] = value
        elif name == "--client_id":
            params["client_id"] = int(value)
        elif name == "--new_project_id":
            params["new_project_id"] = int(value)
        elif name == "--token_name":
            params["token_name"] = value
        elif name == "--update_method":
            params["update_method"] = int(value)
        elif name == "--period":
            params["period"] = int(value)
        elif name == "--token_id":
            params["token_id"] = int(value)

    config = {}
    with open('config.json', 'r') as fp:
        content = fp.read()
        config = json.loads(content)
    sdk = utoken.UTokenSDK(public_key=config.get('public_key', ''),
                           private_key=config.get('private_key', ''),
                           region=config.get('region', ''),
                           zone=config.get('zone', ''))
    print 'example set_params'
    sdk.set_params(config.get('top_org_id', ''), config.get('project_id', ''), config.get('account_id', ''))

    if params["cmd"] == "create_client":
        res = sdk.create_client(params["client_name"], params.get("description", ""))
    elif params["cmd"] == "delete_client":
        res = sdk.delete_client(params["client_id"])
    elif params["cmd"] == "update_client":
        res = sdk.update_client(params["client_id"], params.get("client_name",""), params.get("description", ""), params.get("new_project_id", 0))
    elif params["cmd"] == "get_client":
        res = sdk.get_client()
    elif params["cmd"] == "create_token":
        res = sdk.create_token(params["client_id"], params["token_name"], params["update_method"], params["period"])
    elif params["cmd"] == "update_token":
        res = sdk.update_token(params["client_id"], params["token_id"], params["update_method"])
    elif params["cmd"] == "get_token":
        res = sdk.get_token_list(params["client_id"])
    print_result(params["cmd"], res)
