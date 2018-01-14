#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: inputs.py
#      DESCRIPTION: preparing of raw data about fencers
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.03
# VERSIONS HISTORY: 2018-01-11 (0.01) - base logic of reading to lists,
#                                       transfering to list of objects
#                   2018-01-13 (0.02) - fencer ID was added as unique attribute (key)
#                   2018-01-14 (0.03) - check of list in table format
#-------------------------------------------------------------------------------------

#импорт базовых модулей
import csv, sys, locale
from prettytable import PrettyTable

#импорт внутренних модулей
from fencer import Fencer

#Проверяем локаль
print(sys.getdefaultencoding())
print(locale.getpreferredencoding())

input_file = "test-list.csv"
index = []

#Читаем в списки
with open(input_file, "r", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        row.extend([0, 0, 0, 0])
        print(row) #Проверочный вывод на экран консоли, удалить при сборке билда
        #генерация объектов в список
        index.append(Fencer(*row))

'''
Эту часть при сборке билда удалить
'''
#Проверка списка
print('\n',index,'\n')

#Проверка атрибутов объектов
table = PrettyTable(['ID', 'name', 'club', 'wins', 'defeats', 'hits_got', 'hits_given'])
for fencer in index:
    table.add_row([fencer.ID,fencer.name,fencer.club,fencer.wins,fencer.defeats,fencer.hits_got,fencer.hits_given])
print(table)
