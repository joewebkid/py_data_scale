
import requests
import json

class apiMongoConnect:
    ''' Description '''
    def req(method_name="find",method_type="POST",add_data=False):
        ''' Description '''
        url = "https://data.mongodb-api.com/app/data-byttc/endpoint/data/beta/action/find"
        payload = json.dumps({
            "collection": "TestCollection",
            "database": "Cluster0",
            "dataSource": "Cluster0",
            # "document": {
            #   "status": "close",
            #   "text": "test"
            # }
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'UKywE2kBHQZDFJFtH2A7lv709pAMo9PG2gHOcj7hCt8zu3ba9C6w7Igjk8zDr7Lq'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response