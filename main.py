#Імпорт потрібних модулів
from tkinter import *
from tkinter import messagebox

tk=Tk()
canvas=Canvas(tk, width=400, height=0)
tk.title('Довідничок')
canvas.pack()

#Функція натискання на кнопку
def btn1_translate():
    messagebox.showinfo('Переклад!',"Dog")

#Створення кнопки
btn_1 = Button(text="Пес", background="black", foreground="white", font="16", command = btn1_translate)
btn_1.pack(fill=BOTH)

#Функція натискання на кнопку
def btn2_translate():
    messagebox.showinfo('Переклад!',"Cat")

#Створення кнопки
btn_2 = Button(text="Кіт", background="black", foreground="white", font="16", command = btn2_translate)
btn_2.pack(fill=BOTH)

#Функція натискання на кнопку
def btn3_translate():
    messagebox.showinfo('Переклад!',"Elephant")

#Створення кнопки
btn_3 = Button(text="Слон", background="black", foreground="white", font="16", command = btn3_translate)
btn_3.pack(fill=BOTH)

#Функція натискання на кнопку
def btn4_translate():
    messagebox.showinfo('Переклад!',"Sheep")

#Створення кнопки
btn_4 = Button(text="Овечка", background="black", foreground="white", font="16", command = btn4_translate)
btn_4.pack(fill=BOTH)

#Функція натискання на кнопку
def btn5_translate():
    messagebox.showinfo('Переклад!',"Bird")

#Створення кнопки
btn_5 = Button(text="Пташка", background="black", foreground="white", font="16", command = btn5_translate)
btn_5.pack(fill=BOTH)

#Функція натискання на кнопку
def btn6_translate():
    messagebox.showinfo('Переклад!',"Fish")

#Створення кнопки
btn_6 = Button(text="Риба", background="black", foreground="white", font="16", command = btn6_translate)
btn_6.pack(fill=BOTH)

#Функція натискання на кнопку
def btn7_translate():
    messagebox.showinfo('Переклад!',"Flower")

#Створення кнопки
btn_7 = Button(text="Квітка", background="black", foreground="white", font="16", command = btn7_translate)
btn_7.pack(fill=BOTH)

#Функція натискання на кнопку
def btn8_translate():
    messagebox.showinfo('Переклад!',"Tree")

#Створення кнопки
btn_8 = Button(text="Дерево", background="black", foreground="white", font="16", command = btn8_translate)
btn_8.pack(fill=BOTH)


tk.mainloop()