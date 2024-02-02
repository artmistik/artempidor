#Імпорт потрібних модулів
from tkinter import *
from tkinter import messagebox
tk=Tk()
canvas=Canvas(tk, width=400, height=0)
tk.title('Довідничок')
canvas.pack()


#Функція натискання на кнопку
def btn1_do():
   messagebox.showinfo('Дія!',"Йди")

#Створення кнопки
btn_1 = Button(text="",
            background="green",
            foreground="white",
            font="16",              
            command = btn1_do,
            width = 10,
            height = 5
            )
btn_1.pack()

#Функція натискання на кнопку
def btn1_do():
   messagebox.showinfo('Дія!',"Йди")

def btn2_do():
   messagebox.showinfo('Дія!',"Чекай")

#Створення кнопки
btn_2 = Button(text="",
            background="yellow",
            foreground="white",
            font="16",              
            command = btn2_do,
            width = 10,
            height = 5
            )
btn_2.pack()

#Функція натискання на кнопку
def btn2_do():
   messagebox.showinfo('Дія!',"Чекай")

def btn3_do():
   messagebox.showinfo('Дія!',"Стій")

#Створення кнопки
btn_3 = Button(text="",
            background="red",
            foreground="white",
            font="16",              
            command = btn3_do,
            width = 10,
            height = 5
            )
btn_3.pack()

#Функція натискання на кнопку
def btn3_do():
   messagebox.showinfo('Дія!',"Стій")

tk.mainloop()