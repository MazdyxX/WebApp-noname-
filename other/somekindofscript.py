import requests, json

data = {'email': 'marcin@michnoo.com', 'password': '123', 'school_id': 'ryJFmJEO3T', 'school_pass': 'JqmT1'}
headers= {''}
#[{'teacher_name': 'Marcin print (data)Michno', 'key_code': 'M58VlQXXaK', 'key_pass': 'L8WF5'}, {'teacher_name': 'Arek Słowik', 'key_code': 'MdbaKSNK1e', 'key_pass': 'QlsU9'}]
api_url = 'http://unityddl.azurewebsites.net/register/teacher'

r = requests.get('http://unityddl.azurewebsites.net/class/setTeacher/Mariusz%20Baran/tqrVysZVlV/2b')
#names = list((object['name'] for object in r.json()['teachers']))

print(r)




#{'key_code':'lnbgSy02ge','key_pass':'ehQzC'}#School
#{"school_key":"NGZY65Ekv6","school_pass":"k6nS"}b