import requests

url = 'http://31.31.203.230/api-auth/login/'
# uauth = ('makhotka_alla', 'Asdq1234514')
# udata = {}

# post = requests.post(url=url_1, auth=uauth, data=udata)


user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# Создаем сессию и указываем ему наш user-agent
session = requests.Session()
r = session.get(url, headers = {
    'User-Agent': user_agent_val
})

# Указываем referer. Иногда , если не указать , то приводит к ошибкам. 
session.headers.update({'Referer':url})

#Хотя , мы ранее указывали наш user-agent и запрос удачно прошел и вернул 
# нам нужный ответ, но user-agent изменился на тот , который был 
# по умолчанию. И поэтому мы обновляем его.
session.headers.update({'User-Agent':user_agent_val})

# Получаем значение _xsrf из cookies
_xsrf = session.cookies.get('_xsrf')

# Осуществляем вход с помощью метода POST с указанием необходимых данных 
post_request = session.post(url, {
     'backUrl': 'http://31.31.203.230/',
     'username': 'makhotka_alla',
     'password': 'Asdq1234514',
     '_xsrf':_xsrf,
     'remember':'yes',
})

#Вход успешно воспроизведен и мы сохраняем страницу в html файл
with open("enter_success.html","w",encoding="utf-8") as f:
    f.write(post_request.text)