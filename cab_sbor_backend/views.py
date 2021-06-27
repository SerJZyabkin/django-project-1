import os

from django.shortcuts import render
from .models import NewsEntry, ProductGroupEntry, Product, TableDefinition
# Create your views here.
from os import getcwd
import pandas
import numpy as np
from django.db import models

def index(request):
    news_entries = NewsEntry.objects.all()
    links_out = ProductGroupEntry.objects.all()
    # link1 = ProductGroupEntry()
    # link1.name = 'Коаксиальные разъемы типа SMA'
    # link1.description = 'НУЖНЫ КАРТИНКИ! И ОПИСАНИЕ!'
    # link1.extra_text = 'И краткое описание'
    # link1.image = 'about-01.jpg'
    #
    # link2 = ProductGroupEntry()
    # link2.name = 'Коаксиальные разъемы типа N'
    # link2.description = 'Разверутое описание'
    # link2.extra_text = 'Описание краткое'
    # link2.image = 'about-02.jpg'

    # links_out = [link1, link2]
    links_out[0].url = "{% url 'baseurl/products' %}"

    return render(request, "index.html", {'news_entries': news_entries, 'links_out': links_out})




def products(request):
    print('\n\n', request, '\n\n\n')
    params = [[['Волновое сопротивление:'], ['50 Ом']],
              [['Рабочий диапазон частот:'], ['0–18 ГГц;']],
              [['Максимальный КСВН:'], ['1,1–1,35']],
              [['Экранное затухание:'], ['(100–f ) дБ для соединителей с полужестким кабелем и не более ','–60 дБ для соединителей с гибким кабелем,\n где (f — частота, ГГц)']],
              [['Высокочастотные потери:'],['0,07√f, дБ']],
              [['Сопротивление изоляции:'], ['более 5000 МОм']],
              [['Рабочее напряжение:'], ['335 В']],
              [['Напряжение пробоя:'], ['не менее 750 В']],
              [['Сопротивление центрального контакта:'], ['3 мОм']],
              [['Сопротивление наружнего контакта:'], ['2,5 мОм']],
              [['Рекомендуемый момент затяжки накидной гайки вилки:'], ['50–140 Н•см']],
              [['Гарантированное количество соединений и рассоединений:'], ['500']],
              [['Диапазон рабочих температур:'], ['–65…+165 °C.']],
              ]
    headers = ['Наименование', 'Интерфейс', 'Рабочий диапазон, КСВН', 'Применяемые кабели', 'Монтаж тела',
               'Монтаж пина', 'Материал/покрытие']
    modifications = [['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка', 'Латунь/никель'],

                     ['СР-132-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,32мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-132-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,32мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],
                     ['СР-113-SMAв', 'Вилка прямая', '3 ГГц, КСВН не более 1,25', '1,13мм', 'Обжим', 'Пайка',
                      'Латунь/никель'],

                     ]

    full_data = []

    sheet_names = ['1', '2', '3', '4', '5']
    table_idents = ['product_table_1', 'product_table_2', 'product_table_3', 'product_table_4', 'product_table_5']

    print('\n\n\nllalala', os.getcwd(), '\n\n\n')

    for sn in range(len(sheet_names)):
        dfs = pandas.read_excel(os.getcwd() + '/docs/1.xlsx', sheet_name=sheet_names[sn], engine='openpyxl')
        column_names = dfs.columns.ravel()
        single_table = []
        for id_col in range(len(column_names)):
            single_table += [dfs[column_names[id_col]].tolist()]
        single_table = np.array(single_table).T.tolist()
        table_class = TableDefinition()
        table_class.ident = table_idents[sn]
        table_class.column_names = headers
        table_class.content = single_table
        full_data += [table_class]

    items = [] # Product.objects.filter(id=1)

    buttons = [] # Product.objects.all()
    # print('\n\ntest', type(buttons[0].label),type(buttons), '\n\n')
    # # buttons[0].update(label='test')
    # print('\n\ntest', buttons[0].label, '\n\n')
    return render(request, "products.html", {'params': params, 'headers': headers, 'full_data': full_data,
                                             'modifications': single_table, 'buttons': buttons},)