import pandas as pd
from pandas.io.excel import ExcelWriter

df = pd.read_excel('C:/Users/Алла/Documents/github/study/exel/testing.xlsx',sheet_name='2022-05')
df['Создано'] = pd.to_datetime(df['Создано']).dt.date
df['Создано'] = pd.to_datetime(df['Создано'])

df_date = df['Создано'].unique()
df_date = pd.DatetimeIndex(df_date)
print(df_date)
df_1 = df.pivot_table(
        index='Создано', values='Статус',columns='Трекер', aggfunc='count', sort=True
        
    )
# df_1.to_excel('C:/Users/Алла/Documents/github/study/exel/result.xlsx', sheet_name='Доля обращений по сервису')


df_2 = df.pivot_table(
        index='Создано', values='Статус',columns='Юридическое лицо - Заказчик', aggfunc='count', sort=True
        
    )
# df_2.to_excel('C:/Users/Алла/Documents/github/study/exel/result.xlsx', sheet_name='ЮРлицо')

df_3 = df.pivot_table(
        index='Создано', values='Статус',columns='Объект Фонда', aggfunc='count', sort=True
        
    )

with ExcelWriter('C:/Users/Алла/Documents/github/study/exel/result.xlsx') as writer:
    df_1.to_excel(writer, sheet_name="Доля обращений по сервису")
    df_2.to_excel(writer, sheet_name="ЮРлицо")
    df_3.to_excel(writer, sheet_name="Доля обращений по НП")