import requests, json

header = {'Content-Type': 'application/json'}
data = json.dumps({'key_code': 'NGZY65Ekv6',
                    'key_pass': 'bk6nS'})
print (data)
#[{'teacher_name': 'Marcin Michno', 'key_code': 'M58VlQXXaK', 'key_pass': 'L8WF5'}, {'teacher_name': 'Arek Słowik', 'key_code': 'MdbaKSNK1e', 'key_pass': 'QlsU9'}]
api_url = 'http://unityddl.azurewebsites.net/login/admin'

r = requests.post(api_url,data)
print (json.loads(r.content))







#{'key_code':'lnbgSy02ge','key_pass':'ehQzC'}#School
#{"school_key":"NGZY65Ekv6","school_pass":"bk6nS"}