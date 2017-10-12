import requests, json

data = {'key_code':'NGZY65Ekv6','key_pass':'bk6nS'}
headers= {''}
#[{'teacher_name': 'Marcin print (data)Michno', 'key_code': 'M58VlQXXaK', 'key_pass': 'L8WF5'}, {'teacher_name': 'Arek Słowik', 'key_code': 'MdbaKSNK1e', 'key_pass': 'QlsU9'}]
api_url = 'http://unityddl.azurewebsites.net/login/teacher'

r = requests.post('http://unityddl.azurewebsites.net/login/admin', data )
print("done")
print(r.json())






#{'key_code':'lnbgSy02ge','key_pass':'ehQzC'}#School
#{"school_key":"NGZY65Ekv6","school_pass":"bk6nS"}