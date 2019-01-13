from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0  # 0 — не рухатися горизонтально
        self.y = -1  # -1 — посунутися на 1px вгору
        self.canvas_height = self.canvas.winfo_height()
        # функція повертає поточну висоту полотна ↑

    def draw(self):
        """ id — ідентифікатор овалу
            self.canvas.coords(self.id) ≈ [255.0, 29.0, 270.0, 44.0]
            що дорівнює [x1, y1, верхні ліві координати овалу
                         x2, y2] нижні праві координати ...
        """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:  # y1 (верхня точка м'яча) <= 0
            self.y = 1
        if pos[3] >= self.canvas_height:  # y2 (нижня точка) >= поточній висоті полотна
            self.y = -1


tk = Tk()
tk.title("Гра")
tk.resizable(0, 0)
# вимикаємо можливість змінювати розмір вікна
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
    tk.update()  # полотно
    time.sleep(0.01)

# TODO 3. Примусити м'яч стрибати
# TODO 4. Зміна початкового напряму руху мяча
