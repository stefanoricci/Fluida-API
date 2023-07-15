from dotenv import dotenv_values
import requests
import json

secrets = dotenv_values('.env')
company_id = secrets['COMPANY_ID']
api_key = secrets['API_KEY']

jsonContracts = requests.get('https://api.fluida.io/api/v1/contracts/company/%s' % (company_id), headers={'x-fluida-app-uuid': api_key})

# print (r.jsonContracts)

# parse contracts
contracts = json.loads(jsonContracts.text)['data']

# print(contracts)
for contract in contracts:
    print(contract['firstname'], ' ', contract['lastname'], ' - ', contract['id'])

    jsonJustifications = requests.get(
        'https://api.fluida.io/api/v1/justifications/by_contract/%s?start_date=2023-07-01&end_date=2023-08-31' % (contract['id']), 
        headers={'x-fluida-app-uuid': api_key}
    )
    # print (jsonJustifications.text)
    justifications = json.loads(jsonJustifications.text)['data']

    for justification in justifications:
        print('  ', justification['type_name'], '(', justification['status'], ') from:', justification['from_date'], justification['from_time'], ' to:', justification['to_date'], justification['to_time'], ' durata:', justification['time'])




