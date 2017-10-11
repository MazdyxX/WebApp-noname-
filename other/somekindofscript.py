import requests, json

headers = {'Content-Type': 'application/json'}
def get_account_info():

    api_url = 'http://unityddl.azurewebsites.net//school/generate/SPTEST/["Tomek Marek", "Adam Staczuk", "Piotr Karolak"]'

    response = requests.get(api_url, headers=headers)

    print(response)

get_account_info()

#[{"teacher_name":"Tomek Marek","key_code":"MxA49CxyJu","key_pass":"A1eBB"},
# {"teacher_name":"Adam Staczuk","key_code":"mnumWrqSDZ","key_pass":"H3zCP"},{"teacher_name":"Piotr Karolak","key_code":"gQDkWAYtVw","key_pass":"eN3SO"}]
#testmichnoV10