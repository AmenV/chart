import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array, exp, cos, sin
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from MATH import count

class plot():
    def __init__(x,y,frame,choose, rng, main_menu, window):
        global Range, ch, Array
        Array = []
        Range = rng.replace(':','_')
        if Range == '':
            Range = 100
        ch = choose.replace(' ', '')
        ch = choose.replace('*', '-')
        array = []
        array = main(x,y, choose)                                              #Аппроксимация
        array = plot.main(array, rng, choose)                                  #Заполнение массива
        frame = plot.chart(array, frame, choose, window)                       #Отрисовка графика
        Array = count.__init__(array, frame)                                   #Просчёт мат. модели, дисперсии и тд.
        main_menu.add_cascade(label="Save", command = lambda Array = Array : plot.save(Array)) #Добавление функции меню для сохранения
        
    def main(array,rng, choose):
        x = []
        y = []
        if rng == '':
            rng = '0:100'
        a,b = rng.split(':')
        for i in range(int(a),int(b)):                                         #Заполнение массивов для отрисовки графиков в заданном радиусе
            x.append(i)
            for mapp,key in ff_dict.items():
                if choose == key:
                    y.append(mapp(i, array[0], array[1], array[2]))
        return x, y
    
    def chart(array, frame, choose, window):
        global fig, plt
        list = window.slaves()
        for i in list:
            i.destroy()
        frame = Frame(window)
        frame.pack(side="bottom", expand=False, fill="both", ipady = 300, ipadx = 300)
        fig = Figure(figsize = (6, 6), dpi = 100) 
        plt = fig.add_subplot(111) 
        plt.plot(array[0], array[1])
        plt.legend(choose)                                                     #Надпись
        canvas = FigureCanvasTkAgg(fig, master=frame)                          #Создание полотна и размещение фигуры в окне
        canvas.draw()                                                          #Отрисовка полотна
        canvas.get_tk_widget().place(x = 0, y = 0)                             #Размещение полотна
        return frame
        
        
    def save(array):                                                           #Сохранение граффика и мат данных 
        fig.savefig(f'{ch}-{Range}.png')                                       #Сохранение граффика
        ans = 'S s M m D d G g'                                                #Создание строки для записи в файл
        ans = ans.replace('S', 'Площадь под графиком :')
        ans = ans.replace('s', str(array[0]))
        ans = ans.replace('M', 'мат. ожидание :')
        ans = ans.replace('m',str(array[1]))
        ans = ans.replace('D','Дисперсия :')
        ans = ans.replace('d',str(array[2]))
        ans = ans.replace('G','средне квадратичное отклонение :')
        ans = ans.replace('g',str(array[3]))
        try:
            f = open('ans.txt', 'w+')                                          #Открытие файла в формате "запись"
            f.write(ans)                                                       #Запись в файл строки в виде название -> *перенос строки* -> оставшийся текст
            f.close()                                                          #Закрытие файла
        except FileNotFoundError:
            f = open('ans.txt', 'wb')                                          #Создание файла
            f.close()                                                          #Закрытие 
            f = open('ans.txt', 'w')                                           #Открытие файла в формате "запись"
            f.write(ans)                                                       #Запись в файл строки в виде название -> *перенос строки* -> оставшийся текст
            f.close()    



#Блок с функциями**************************************************************
def mapping_1(x,a,b,c):
    return a * x + b
    
def mapping_2(x,a,b,c):
    return a * x ** 2 + b * x + c
    
def mapping_3(x,a,b,c):
    return a * exp(x * b) + c
    
def mapping_4(x,a,b,c):
    return a * sin(x*b) + c
    
def mapping_5(x,a,b,c):
    return a * cos(x*b) + c
#******************************************************************************

ff_dict = {mapping_1: "a * x + b", mapping_2: "a * x ** 2 + b * x + c", 
           mapping_3: "a * exp(x * b) + c", mapping_4: "a * sin(x*b) + c", mapping_5: "a * cos(x*b) + c"} # словарь с функциями

def main(x,y, choose):                                                         #Аппроксимация для получения значений переменных по предоставленным данным
    for mapp, key in ff_dict.items():
        args,covar = curve_fit(mapp,x,y)
        if choose == key:
            return args