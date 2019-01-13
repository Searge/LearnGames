from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        """ id — ідентифікатор овалу
            0 — не рухатися горизонтально
            -1 — посунутися на 1px вгору
        """
        self.canvas.move(self.id, 0, -1)

tk = Tk()
tk.title("Гра")
tk.resizable(0, 0)  # вимикаємо можливість змінювати розмір вікна
tk.wm_attributes("-topmost", 1)
#  атрибути менеджжера вікон — найвище.

canvas = Canvas(tk, width=500, height=400,
                bd=0, highlightthickness=0)
#               вимикаємо контур вікн
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()  # Перемальовують
    tk.update()            # полотно
    time.sleep(0.01)

# TODO 3. Примусити м'яч стрибати
# TODO 4. Зміна початкового напряму руху мяча
