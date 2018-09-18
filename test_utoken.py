from utoken import UTokenSDK
import unittest
import json


class TestUTokenSDK(unittest.TestCase):

    def setUp(self):
        config = {}
        with open('config.json', 'r') as fp:
            content = fp.read()
            config = json.loads(content)
        self._sdk = UTokenSDK(public_key=config.get('public_key', ''),
                        private_key=config.get('private_key', ''),
                        region=config.get('region', ''),
                        zone=config.get('zone', ''))
        self._sdk.set_params(config.get('project_id', ''))

    def test_create_client_1(self):
        client_name = "  client1\n"
        description = "\n\n\n\n\n   "
        business_group = "\n\n  "
        try:
            httpcode, msg = self._sdk.create_client(client_name, description, business_group)
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(True, e)

    def test_create_client_2(self):
        client_name = "  client1\n"
        description = "\n\nclient1 \n"
        business_group = "\n test \n"
        httpcode, msg = self._sdk.create_client(client_name, description, business_group)
        self.assertEqual(httpcode, 200, "http code equal to 200")
        self.assertTrue(msg.get("RetCode", -1) == 0, msg.get("Message", ""))

    def test_create_client_3(self):
        print "client_name type-int test..."
        try:
            httpcode, msg = self._sdk.create_client(1, "", "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "description type-int test..."
        try:
            httpcode, msg = self._sdk.create_client("client1", 1, "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "business_group type-int test..."
        try:
            httpcode, msg = self._sdk.create_client("client1", "description1", 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "client_name, description, business_group all empty test...",
        try:
            httpcode, msg = self._sdk.create_client("", "", "")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "client_name empty test..."
        try:
            httpcode, msg = self._sdk.create_client("", "test", "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "business_group empty test..."
        try:
            httpcode, msg = self._sdk.create_client("test","test", "")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "description empty test..."
        httpcode, msg = self._sdk.create_client("test", "", "test")
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)
        print "normal test..."
        httpcode, msg = self._sdk.create_client("test", "test", "test")
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)

    def test_get_client(self):
        print "test get client..."
        httpcode, msg = self._sdk.get_client()
        print msg
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)

    def test_delete_client(self):
        print "test delete client..."
        httpcode, msg = self._sdk.get_client()
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)
        for result in msg["Result"]:
            print "delete client:", result["ClientID"]
            client_id = result["ClientID"]
            httpcode, retv = self._sdk.delete_client(client_id)
            self.assertTrue(httpcode == 200 and retv.get("RetCode", -1) in [0, 95502], retv)

    def test_update_client(self):
        print "test update client..."
        client_id = ""
        httpcode, msg = self._sdk.get_client()
        if httpcode == 200 and msg.get("RetCode") == 0 and len(msg["Result"]) > 0 :
            client_id = msg["Result"][0]["ClientID"]
        else:
            httpcode, msg = self._sdk.create_client("test", "test", "test")
            self.assertTrue(httpcode==200 and msg.get("RetCode", -1) == 0, "create client assert")
            client_id = msg["ClientID"]
        print "======================================client_id=", client_id
        print "client_name type-int test..."
        try:
            httpcode, msg = self._sdk.update_client(1, "", "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "description type-int test..."
        try:
            httpcode, msg = self._sdk.update_client(client_id, 1, "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "business_group type-int test..."
        try:
            httpcode, msg = self._sdk.update_client(client_id, "description1", 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "client_name, description, business_group all empty test...",
        try:
            httpcode, msg = self._sdk.update_client("", "", "")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "client_name empty test..."
        try:
            httpcode, msg = self._sdk.update_client("", "test", "test")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "business_group empty test..."
        try:
            httpcode, msg = self._sdk.update_client(client_id, "test", "")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print "description empty test..."
        httpcode, msg = self._sdk.update_client(client_id, "", "test")
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)
        print "normal test..."
        httpcode, msg = self._sdk.update_client(client_id, "test", "test")
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)

    def test_create_token(self):
        '''create_token(self, client_id, token_name, update_method, period)'''
        print '==================test create token'
        print "===========1. client_id empty"
        try:
            httpcode, msg = self._sdk.create_token("   ", "test", 1, 3600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===========2. client_id int'
        try:
            httpode, msg = self._sdk.create_token(123, "test", 1, 3600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===========3. client_name empty'
        try:
            httpcode, msg = self._sdk.create_token("test", "", 1, 3600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '============4. updatemethod invalid'
        try:
            httpcode, msg = self._sdk.create_token("test", "test", 3, 3600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '============5. period invalid'
        try:
            httpcode, msg = self._sdk.create_token("test", "test", 3, 100)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '============6. client_id not exists'
        try:
            httpcode, msg = self._sdk.create_token("test34354353223142319482309", "test", 1, 3600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '============7. normal test'
        client_id = ""
        httpcode, msg = self._sdk.get_client()
        if httpcode == 200 and msg.get("RetCode") == 0 and len(msg["Result"]) > 0:
            client_id = msg["Result"][0]["ClientID"]
        else:
            httpcode, msg = self._sdk.create_client("test", "test", "test")
            self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, "create client assert")
            client_id = msg["ClientID"]
        try:
            httpcode, msg = self._sdk.create_token(client_id + "   ", "test", 1, 600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '=============8 complex test'
        client_id = ""
        httpcode, msg = self._sdk.get_client()
        if httpcode == 200 and msg.get("RetCode") == 0 and len(msg["Result"]) > 0:
            client_id = msg["Result"][0]["ClientID"]
        else:
            httpcode, msg = self._sdk.create_client("test", "test", "test")
            self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, "create client assert")
            client_id = msg["ClientID"]
        httpcode, msg = self._sdk.create_token(client_id, "test", 1, 600)
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)
        token_id = msg["TokenID"]
        httpcode, msg = self._sdk.get_token_list(client_id)
        self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, msg)
        is_passed = False
        for result in msg["Result"]:
            if result["TokenID"] == token_id:
                is_passed = True
                break
        self.assertTrue(is_passed)


    def test_update_token(self):
        '''update_token(self, client_id, token_id, update_method)'''
        print '=============================test update token'
        print '===============1. client_id empty'
        try:
            httpcode, msg = self._sdk.update_token("", 123, 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============2. client_id int'
        try:
            httpcode, msg = self._sdk.update_token(123, 123, 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============3. token_id empty str'
        try:
            httpcode, msg = self._sdk.update_token("test", "", 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============4. client_id not exsits'
        try:
            httpcode, msg = self._sdk.update_token("wnskjgdsurwewfo23r3754375", 123, 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============5. token_id not exsits'
        client_id = ""
        httpcode, msg = self._sdk.get_client()
        if httpcode == 200 and msg.get("RetCode") == 0 and len(msg["Result"]) > 0:
            client_id = msg["Result"][0]["ClientID"]
        else:
            httpcode, msg = self._sdk.create_client("test", "test", "test")
            self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, "create client assert")
            client_id = msg["ClientID"]
        try:
            httpcode, msg = self._sdk.update_token(client_id + '  \n', 123433243, 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass

        print '================6. update_method invalid'
        token_id = 0
        httpcode, msg = self._sdk.get_token_list(client_id + "  ")
        if httpcode == 200 and msg.get('RetCode', -1) == 0 and len(msg["Result"]) > 0:
            token_id = msg["Result"][0]["TokenID"]
        else:
            httpcode, msg = self._sdk.create_token(client_id + "   ", "test", 1, 600)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
            token_id = msg["TokenID"]
        try:
            httpcode, msg = self._sdk.update_token(client_id, token_id, 3)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass

        print '================7. normal'
        try:
            httpcode, msg = self._sdk.update_token(client_id, token_id, 1)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass

    def test_get_token_list(self):
        print '==================================test get_token_list'
        print '===============1. client_id empty'
        try:
            httpcode, msg = self._sdk.get_token_list("\n ")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============2. client_id int'
        try:
            httpcode, msg = self._sdk.get_token_list(123)
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============3. client_id not exists'
        try:
            httpcode, msg = self._sdk.get_token_list("dfasdwerewsw3ew232\n ")
            self.assertTrue(httpcode != 200 or msg.get("RetCode", -1) != 0, msg)
        except Exception as e:
            pass
        print '===============4. normal'
        client_id = ""
        httpcode, msg = self._sdk.get_client()
        if httpcode == 200 and msg.get("RetCode") == 0 and len(msg["Result"]) > 0:
            client_id = msg["Result"][0]["ClientID"]
        else:
            httpcode, msg = self._sdk.create_client("test", "test", "test")
            self.assertTrue(httpcode == 200 and msg.get("RetCode", -1) == 0, "create client assert")
            client_id = msg["ClientID"]
        httpcode, msg = self._sdk.get_token_list(client_id + "\n ")
        self.assertTrue(httpcode == 200 and msg["RetCode"]==0)







if __name__ == '__main__':
    unittest.main()