poem = '''
Погиб поэт. Невольник чести.
Пал, оклеветанный молвой.
С свинцом в груди и жаждой мести,
Поникнув гордой головой...
'''

f = open('poem.txt', 'w') #открываем файл для записи
f.write(poem) #записываем текст в файл
f.close() #закрываем файл

f = open('poem.txt') #если не указан режим, по умолчанию
                    #подразумевается режим чтения ('r'eading)

while True:
    line = f.readline()
    if len(line) == 0: #нулевая длина обозначает конец файла (E0F)
        break
    print(line, end='')

f.close()