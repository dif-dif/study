def check(text):
    text = text.lower()
    return re.sub("[ |,|.|!|?|@|']", "", text)

def reverse(text):
    return text[::-1]

forbidden = (".", ",", "!", "?", " ", "@", "'", '"')
import re


def is_palindrome(text):
    return check(text) == reverse(check(text))

print('Для выхода из программы напишите "break"')
while True:
    something = input('Введите текст: ')
    if (is_palindrome(something)):
        print('Да, это палиндром')
    else:
        print('Нет, это не палиндром')
    if something == 'break':
        break