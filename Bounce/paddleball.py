from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        """ Змінюємо початковий напрямок руху (кут)
            створивши список і перемішуючи його.
        """
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  # будь-яке число від -3 до 3
        self.y = -3  # -3 — прискорюємо рух м'яча
        self.canvas_height = self.canvas.winfo_height()
        # функція повертає поточну висоту полотна ↑
        self.canvas_width = self.canvas.winfo_width()
        #                      ... ширина полотна

    def draw(self):
        """ id — ідентифікатор овалу
            self.canvas.coords(self.id) ≈ [255.0, 29.0, 270.0, 44.0]
            що дорівнює [x1, y1, верхні ліві координати овалу
                         x2, y2] нижні праві координати ...
        """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:  # y1 (верхня точка м'яча) <= 0
            self.y = 3   # + повертаємо униз
        if pos[3] >= self.canvas_height:  # y2 (нижня точка) >= поточній висоті полотна
            self.y = -3  # - повертаємо вверх
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


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

# TODO 5. Додати ракетку
# TODO 6. Урохомити ракетку
# TODO 7. Визначення моменту, коли м'яч вдаряється в ракетку
# TODO 8. Додавання елементу випадковості

# TODO 9.1 Відтермінувати початок гри
#     Додати прив'язку до події клацання мишкою
# TODO 9.2 Додати напис «Кінець гри»
# TODO 9.3 Зробити м'яч швидшим
#     Передавати прискорення від ракетки
# TODO 9.4 Записати рахунок гравця

