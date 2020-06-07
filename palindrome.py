#-*- coding: utf-8 -*-#
# by ALLORI

#Импорт модулей
from tkinter import *
from tkinter import filedialog as fd

#Функция отвечающая за открытие файла с записью полученного текста в глобальную переменную
def insertText():
    global read
    file_name = fd.askopenfilename()
    f = open(file_name, encoding = 'utf-8')
    read = f.read()
    read = read.lower()
    text.insert(1.0, read)
    f.close()
    return read

#Функция отвечающая за сохранение обработанного текста в новый файл
def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

#Функция по поиску палиндромов (слов перевертышей)
def search():
    slovo = read.split()
    text.delete(1.0, END)
    palindroms = ''
    for sl in slovo:
        if len(sl) >= 2:
            sl.lower()
            if sl == sl[::-1]:
                palindroms = palindroms + sl + ', '
    palindroms = palindroms[0:-2]
    text.insert(1.0, palindroms.upper())

#Основной код программы отвечающий за создание элементов интерфейса
root = Tk()
root.title("Палиндром by ALLORI v1.0")
text = Text(width=100, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Поиск перевертышей", command=search)
b3.grid(row=1, column=1, sticky=E)

root.mainloop()
