import re
from requests import Session
import pytest

@pytest.mark.parametrize("style", ['abap', 'colorful', 'friendly', 'igor', 'perldoc'])
@pytest.mark.parametrize("language", ['abap', 'arrow', 'bc'])

def test_group_0(style, language):
    name='makhotka_alla'
    passw='Asdq1234514'
    session = Session()
    r1 = session.get(url='http://31.31.203.230/api-auth/login/')
    csrftokens = re.findall(r'\w+', r1.text)
    # print(r1.cookies)
    if 'value' in csrftokens:
        r2 = csrftokens[(csrftokens.index('value') + 1)]
        # print(r2)
    else:
        print('not found')

    data1=dict(username = name, password = passw, csrfmiddlewaretoken = r2, next = '/')

    r3 = session.post(url='http://31.31.203.230/api-auth/login/', data=data1) #авторизация

    assert r3.status_code == 200

    r4 = session.post(url='http://31.31.203.230/snippets/', json={
        "title": "sdf1234",
        "code": "df",
        "linenos": True,
        "language": language,
        "style": style
    },
                    headers={"X-CSRFTOKEN": r3.history[0].cookies['csrftoken']}) #создание сниппета

    logout = session.get(url= 'http://31.31.203.230/api-auth/logout/?next=/', headers={"X-CSRFTOKEN": r3.history[0].cookies['csrftoken']}) #выход

    r5 = session.post(url='http://31.31.203.230/snippets/', json={
        "title": "sdf1234",
        "code": "df",
        "linenos": True,
        "language": 'abap',
        "style": 'abap'
    }, headers={"X-CSRFTOKEN": r3.history[0].cookies['csrftoken']}) # проверка что вышли

    print('Подтверждение входа - выполненный запрос: \n', r4.text)
    print('Подтверждение выхода - тот же запрос не может выполниться: \n', r5.text)


