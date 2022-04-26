from requests import Session
from bs4 import BeautifulSoup

session = Session()

response_1 = session.get(url='http://31.31.203.230/api-auth/login/')

soup = BeautifulSoup(response_1.text, features="html.parser")
found = soup.find('input', {'name':'csrfmiddlewaretoken'})
print(found.attrs['value'])

login_data = dict(username='makhotka_alla',
                  password='Asdq1234514',
                  csrfmiddlewaretoken=found.attrs['value'])

response_2 = session.post(url='http://31.31.203.230/api-auth/login/', data=login_data)

response_3 = session.post(url='http://31.31.203.230/snippets/', json={
    "title": "sdf1234",
    "code": "df",
    "linenos": True,
    "language": 'abap',
    "style": 'abap'
},
                  headers={"X-CSRFTOKEN": response_2.history[0].cookies['csrftoken']})

print(response_3.text)
