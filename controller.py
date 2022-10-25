import basic as db
import view as ui
import log

def menu():
    going=True
    while going:
        request=['Просмотр справочника;Добавление контакта;Удаление контакта;Поиск контакта;Экспорт в CSV;Экспорт в XML;Выход']
        choice = ui.get_choice(request[0])
        if choice == 1:
            ui.get_look()
            log.input_write("Просмотрена телефонная книга")
            break
        elif choice == 2:
            db.get_add()
            log.input_write("Добавлен контакт")
            break
        elif choice == 3:
            db.get_remove()
            log.input_write("Удален контакт")
            break
        elif choice == 4:
            db.get_find()
            log.input_write("Выполнен поиск контакта")
            break
        elif choice == 5:
            db.get_out()
            log.input_write("Проведена выгрузка контактов во внешний файл")
            break
        elif choice == 6:
            db.get_out_xml()
            log.input_write("Проведена выгрузка контактов в XML-формат")
            break
        elif choice == 7:
            print('До новых встреч!')
            break
        