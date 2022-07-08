import pandas as pd
from pandas.io.excel import ExcelWriter

def generate(month):
    df = pd.read_excel(f'o_{month}.xlsx',sheet_name='1')
    df['Создано'] = pd.to_datetime(df['Создано']).dt.date
    df['Создано'] = pd.to_datetime(df['Создано'])
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'Сигма Сириус.*', 'Сигма Сириус', regex= True)
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'сигма', 'Сигма', regex= True)
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'Администрация ФТ Сириус', 'Административные здания', regex= True)
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'Отель "Пульсар"', 'Пульсар', regex= True)
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'Хостел "S Hostel"', 'Склады РЖД', regex= True)
    df['Объект Фонда'] = df['Объект Фонда'].str.replace(r'Сириу-Арена', 'Сириус Арена', regex= True)
    # df = df.drop(df["~(1C.*)"].index)

    df_date = df['Создано'].unique()
    df_date = pd.DatetimeIndex(df_date)
    # print(df_date)

    df_1 = df.pivot_table(
            index='Создано', values='Статус',columns='Трекер', aggfunc='count', sort=True
        )

    df_2 = df.pivot_table(
            index='Создано', values='Статус',columns='Юридическое лицо - Заказчик', aggfunc='count', sort=True
        )

    df_3 = df.pivot_table(
            index='Создано', values='Статус',columns='Объект Фонда', aggfunc='count', sort=True
        )

    df_4 = df.pivot_table(
            index='Объект Фонда',values='Юридическое лицо - Заказчик',columns='Статус', aggfunc='count', sort=True
        )

    df_5 = df.pivot_table(
            index='Объект Фонда', values='Статус',columns='Юридическое лицо - Заказчик', aggfunc='count', sort=True
        )

    df_6 = df.pivot_table(
            index='Юридическое лицо - Заказчик',values='Объект Фонда',columns='Статус', aggfunc='count', sort=True
        )

    print(df_4.columns.values)
    df_4['Всего'] = df_4[list(df_4.columns.values)].sum(axis=1)
    df_6['Всего'] = df_6[list(df_6.columns.values)].sum(axis=1)
    # df_3.drop(columns=list(df_filter_sigma.columns.values)[1:], inplace=True)
    # print(df_3)

    with ExcelWriter(f'{month}.xlsx') as writer:
        df_1.to_excel(writer, sheet_name="Доля обращений по сервису")
        df_2.to_excel(writer, sheet_name="ЮРлицо")
        df_3.to_excel(writer, sheet_name="Доля обращений по НП")
        df_4.to_excel(writer, sheet_name="Объект-статус")
        df_5.to_excel(writer, sheet_name="ЮРлицо-объект")
        df_6.to_excel(writer, sheet_name="ЮРлицо-статус")
        
for i in ['may', 'april', 'june']:
    generate(i)