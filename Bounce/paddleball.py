from tkinter import *
import random
import time

# TODO Створити полотно

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


# TODO Створити Клас Мяча


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1)


ball = Ball(canvas, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
