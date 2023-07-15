import requests
import json

class Fluida:

    def __init__(self, api_key):
        self.api_key = api_key

    ## FLUIDA API Calls
    def getContracts(self, company_id):
        res = requests.get(
            'https://api.fluida.io/api/v1/contracts/company/%s' % (company_id), 
            headers={'x-fluida-app-uuid': self.api_key}
        )
        return json.loads(res.text)['data']

    def getJustificationsByContract(self, contract_id):
        res = requests.get(
            'https://api.fluida.io/api/v1/justifications/by_contract/%s?start_date=2023-07-01&end_date=2023-08-31' % (contract_id), 
            headers={'x-fluida-app-uuid': self.api_key}
        )
        return json.loads(res.text)['data']
