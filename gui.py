import basic as db
import view as ui
from tkinter import*
from tkinter import messagebox

def result_find(text):
    messagebox.showinfo('Результат поиска:', text)

def save_contacts():
    data = list(list_box.get(0, END))
    for i, el in enumerate(data):
        x = el.find('.')
        data[i] = el[(x+2):].lstrip()
    write_file(data)

def read_file():
    with open('phonebook.csv', 'r', encoding='utf-8') as data:
        phone_number = data.read().split('\n')
    for i, el in enumerate(phone_number):
        phone_number[i] = el
    return phone_number

def write_file(data):
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for i, el in enumerate(data):
            if (i+1) == len(data):
                file.write(el)
            else:
                file.write(el + '\n')

def add_btn_click():
    global spisok
    box = str(surname.get() + '; ' +
            name_c.get() + '; ' +
            phone.get())
    surname.delete(0, END)
    name_c.delete(0, END)
    phone.delete(0, END)
    list_box.insert(END, box)
    save_contacts()

def delete_btn_click():
    list_box.delete(list_box.curselection())
    save_contacts()
    global spisok
    global spisok_box
    spisok = read_file()
    spisok_box = Variable(value=spisok)
    list_box.config(listvariable=spisok_box)

def find_btn_click():
    res = ''
    global spisok
    spisok = read_file()
    for el in spisok:
        if find_entry.get().lower() in el.lower():
            res += el + '\n'
    result_find(res)

window = Tk()
window.title('Телефонный справочник')
window.geometry('570x300')
spisok = read_file()
spisok_box = Variable(value=spisok)

head_label = Label(text='Добро пожаловать в телефонную книгу!')
head_label.pack()
list_frame = Frame()
list_frame.pack()
list_box = Listbox(list_frame, listvariable=spisok_box, height = 10, width = 50)
scrollbar = Scrollbar(list_frame, orient="vertical", command = list_box.yview)
list_box.config(yscrollcommand = scrollbar.set)
scrollbar.pack(side = RIGHT, fill = Y)
list_box.pack()

clik_frame = Frame()
clik_frame.pack()

contact_label = Label(clik_frame, text='Фамилия')
contact_label.grid(column=0, row=0)
numbers_label = Label(clik_frame, text='Имя')
numbers_label.grid(column=1, row=0)
change_label = Label(clik_frame, text='Номер телефона')
change_label.grid(column=2, row=0)

surname = Entry(clik_frame)
surname.grid(column=0, row=1, padx=10)
name_c = Entry(clik_frame)
name_c.grid(column=1, row=1, padx=10)
phone = Entry(clik_frame)
phone.grid(column=2, row=1, padx=10)

add_btn = Button(clik_frame, text='Добавить', command=add_btn_click)
add_btn.grid(column=3, row=1, sticky=NSEW, padx=5, pady=3)
delete_btn = Button(clik_frame, text='Удалить', command=delete_btn_click)
delete_btn.grid(column=1, row=2,sticky=NSEW, padx=5, pady=3)
find_btn = Button(clik_frame, text='Поиск', command=find_btn_click)
find_btn.grid(column=3, row=4, sticky=NSEW, padx=5, pady=3)

find_label = Label(clik_frame, text='Введите данные для поиска:')
find_label.grid(column=0, row=4, columnspan=2, sticky='e')
find_entry = Entry(clik_frame)
find_entry.grid(column=2, row=4)

window.mainloop()