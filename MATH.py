from math import *
import numpy as np
from tkinter import *

class count():                      
    def __init__(array, frame):                                                 
        x = array[0]
        y = array[1]
        array = count.main(x,y)                                                #просчёт мат. ожидания, дисперсии, площади и тд
        count.show(array, frame)                                               #вывод значений на экран
        return array
        
    def main(x,y):                                                             #просчёт
        S = sum(y) / sum(x)
        M = np.mean(y)
        D = np.var(y)
        G = sqrt(D)
        return S,M,D,G
    
    def show(array, frame):                                                    #вывод значений в виде текстовых строк
        lbl_s = Label(frame, text = 'Площадь под графиком :').place(x = 600, y = 350)
        lbl_S = Label(frame, text = array[0]).place(x = 600, y = 375)
        lbl_m = Label(frame, text = 'мат. ожидание :').place(x = 600, y = 400)
        lbl_M = Label(frame, text = array[1]).place(x = 600, y = 425)
        lbl_d = Label(frame, text = 'Дисперсия :').place(x = 600, y = 450)
        lbl_D = Label(frame, text = array[2]).place(x = 600, y = 475)
        lbl_g = Label(frame, text = 'средне квадратичное отклонение :', font = ('Times New Roman', 10)).place(x = 600, y = 500)
        lbl_G = Label(frame, text = array[3]).place(x = 600, y = 525)