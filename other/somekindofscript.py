import requests, json

headers = {'Content-Type': 'application/json'}
def get_account_info():

    api_url = 'http://unityddl.azurewebsites.net//school/generate/SPTEST/["Tomek Marek", "Adam Staczuk", "Piotr Karolak"]'

    response = requests.get(api_url, headers=headers)

    print(response)

get_account_info()


