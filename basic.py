import view as ui
import json
import csv

def get_input(req):
    answer = []
    for i in req:
        print(f'\nВведите {i}:')
        answer.append(input())
    return answer

def get_add():
    request = ['фамилию', 'имя', 'номер телефона']
    data = get_input(request)
    with open('phonebook.csv', 'a', encoding = "cp1251") as file:
        file.writelines(
            f'{data[0]},{data[1]},{data[2]}\n')

def get_remove():
    request = ['в строку уникальные данные, содержащиеся в строке, подлежащей удалению:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    db_new = []
    with open('phonebook.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
            else:
                db_new.append(line.replace('\n', ''))
    print('По указанным параметрам подобраны строки:')
    [print(line) for line in db_remove]
    with open('phonebook.csv', 'w') as file:
        [file.writelines(f'{line}\n') for line in db_new]

def get_find():
    request = ['в строку уникальные данные для поиска:']
    data = (','.join((''.join((get_input(request)))).split(' '))).split(',')
    db_remove = []
    with open('phonebook.csv', 'r') as file:
        for line in file:
            match = True
            for key in data:
                if key not in line:
                    match = False
            if match:
                db_remove.append(line.replace('\n', ''))
    print('По указанным параметрам подобраны строки:')
    [print(line) for line in db_remove]

def get_out():
    file_name = input('Введите имя файла для экспорта данных: ')+'.csv'
    request = [
        'Все данные построчно, разделитель - пустая строка; Один контакт - одна строка. Разделители - точка с запятой']
    choice = ui.get_choice(request[0])
    if choice == 1:
        pattern = '{0}\n{1}\n{2}\n'
    elif choice == 2:
        pattern = '{0};{1};{2}\n'
    with open('phonebook.csv', 'r') as file:
        temp = [line.replace('\n','').split(',') for line in file]
    with open(file_name,'w') as output:
        [output.writelines(pattern.format(x[0],x[1],x[2]) for x in temp)]

def get_out_xml():
    reader = csv.reader(open('phonebook.csv', 'r'), delimiter=",")
    f = open('export.xml', 'w')
    f.write('<phonebook-data>' + '\n')

    for row in reader:
        f.write('\t' + '<Contact>' + '\n')
        f.write('\t' + '\t' + '<Surname>' + row[0] + '</Surname>' + '\n')
        f.write('\t' + '\t' + '<Name>' + row[1] + '</Name>' + '\n')
        f.write('\t' + '\t' + '<Phonenumber>' + row[2] + '</Phonenumber>' + '\n')
        f.write('\t' + '</Contact>' + '\n')

    f.write('</phonebook-data>')

 