import requests
from pprint import pprint

# get = requests.get(url='http://31.31.203.230/snippets/98/')
# delete = requests.delete(url='http://31.31.203.230/snippets/98/', auth=('makhotka_alla', 'Asdq1234514'))
# get_2 = requests.get(url='http://31.31.203.230/snippets/98/')

# pprint(get.text)
# pprint(delete.text)
# pprint(get_2.text)

uurl = 'http://31.31.203.230/snippets/131/'
uauth = ('makhotka_alla', 'Asdq1234514')
udata = {"title": "aaaaaaaaaa put IN", 
            "code": "Hnlo im put in"}

# post = requests.post(url=uurl,
#                         auth=uauth,
#                         data=udata)

put = requests.put(url=uurl,
                        auth=uauth,
                        data=udata)

print(put.text)