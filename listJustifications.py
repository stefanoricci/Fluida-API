from dotenv import dotenv_values
from fluida import Fluida

def main():
    secrets = dotenv_values('.env')
    api_key = secrets['API_KEY']
    fluida = Fluida(api_key)
    company_id = secrets['COMPANY_ID']

    contracts = fluida.getContracts(company_id)
    for contract in contracts:
        print(contract['firstname'], ' ', contract['lastname'], ' - ', contract['id'])
        justifications = fluida.getJustificationsByContract(contract['id'])
        for justification in justifications:
            print('  ', justification['type_name'], '(', justification['status'], ') from:', justification['from_date'], justification['from_time'], ' to:', justification['to_date'], justification['to_time'], ' durata:', justification['time'])


if __name__ == '__main__':
    main()
