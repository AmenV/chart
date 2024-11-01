from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
import numpy as np
from plot import plot

class app():
    def main():
        global frame, cmb, path, entry_range, window, main_menu
        window = Tk()
        window.title('Построение графика')                                     #Присвоение загаловка приложению
        window.geometry('750x750')                                             #Задача размеров окна
        frame = Frame(window)
        frame.pack(side="bottom", expand=False, fill="both", ipady = 300, ipadx = 300)
        
        window.option_add("*tearOff", FALSE)
        main_menu = Menu()                                                     #Создание меню
        main_menu.add_cascade(label="path to file", command = app.add_path)
        window.config(menu = main_menu)                                        #определение меню
        lbl_func = Label(text = 'Выберите тип и степень функции').place(x = 5, y = 5)
        cmb = Combobox(values = ['a * x + b', 'a * x ** 2 + b * x + c', 'a * sin(x*b) + c', 'a * cos(x*b) + c', 'a * exp(x * b) + c'])
        cmb.place(x = 5, y = 50)
        lbl_range = Label(text = 'Введите радиус заполнения графика, в случае, если поле останется пустым, радиус будет от 1 до 100').place(x = 5, y = 100)
        lbl_range2 = Label(text = 'Радиус введите в форме x:y').place(x = 5, y = 115)
        entry_range = Entry(width = 25)
        entry_range.place(x = 5, y = 150)
        btn = Button(text = 'Построить график', command = app.Open).place(x = 260, y = 5)
        window.mainloop()
    
    def add_path():
        global path
        lbl = Label(text = 'Введите путь к файлу').place(x=5, y=400)
        path = Entry(width = 45)
        path.place(x=5,y=450)
        btn_add = Button(text = 'Запомнить путь', command = app.path_remember).place(x = 5, y = 500)
    
    def Open():
        try:
            way = path.get()
        except NameError:
            f = open('file.txt', 'r')                                          #Путь к файлу 
            way = f.read()
    
        Range = entry_range.get()
            
        x = []
        y = []
        print(way)
        df =  pd.read_excel(way)
        if df.shape[1] == 1:                                                   #Заполнение массивов данными для аппроксимации
            x.append(0)
            y.append(0)
            for i in range(df.shape[0]):
                x.append(i+1)
                df1 = np.array(df[df.columns[0]])
                y.append(df1[i])
            
        else:
            
            x, y = np.array(df[df.columns[0]]), np.array(df[df.columns[1]])
            
            print(x,y)
        choose = cmb.get()
        plot.__init__(x,y, frame, choose, Range, main_menu, window)            #Отрисовка графика
    
        
    def path_remember():
        global frame
        ans = ''
        way = path.get()
        try:
            f = open('file.txt', 'w+')                                         #Открытие файла в формате "запись"
            f.write(way)                                                       #Запись в файл строки в виде название -> *перенос строки* -> оставшийся текст
            f.close()                                                          #Закрытие файла
        except FileNotFoundError:
            f = open('file.txt', 'wb')                                         #Создание файла
            f.close()                                                          #Закрытие 
            f = open('file.txt', 'w')                                          #Открытие файла в формате "запись"
            f.write(way)                                                       #Запись в файл строки в виде название -> *перенос строки* -> оставшийся текст
            f.close()
        list = window.slaves()
        for i in list:
            i.destroy()
        frame = Frame(window)
        frame.pack(side="bottom", expand=False, fill="both", ipady = 200, ipadx = 200)

app.main()
