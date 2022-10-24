import basic as db
import view as ui

def menu():
    going=True
    while going:
        request=['Просмотр справочника; Добавление контакта; Удаление контакта; Поиск контакта; Экспорт в файл']
        choice = ui.get_choice(request[0])
        if choice == 1:
            ui.get_look()
        elif choice == 2:
            db.get_add()
        elif choice == 3:
            db.get_remove()
        elif choice == 4:
            db.get_find()
        elif choice == 5:
            db.get_out()
        input('Нажмите Enter для продолжения')