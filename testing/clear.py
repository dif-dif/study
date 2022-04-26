import requests
from pprint import pprint

login = 'makhotka_alla'
password = "Asdq1234514"

pages = []
for page in range(1, 5):
    know = requests.get(url=f'http://31.31.203.230/users/?page={page}')
    results = know.json()['results']
    for user_data in results:
        if user_data['username'] == login:
            pages = user_data['snippets']
    
authent = (login, password)

for i in pages:
    url_temp = i
    delete = requests.delete(url=url_temp, auth=authent)
    print(delete.status_code)