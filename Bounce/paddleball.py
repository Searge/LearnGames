from tkinter import *
import random
import time

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


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
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
        self.hit_bottom = False

    def draw(self):
        """ id — ідентифікатор овалу
            self.canvas.coords(self.id) ≈ [255.0, 29.0, 270.0, 44.0]
            що дорівнює [x1, y1, верхні ліві координати овалу
                         x2, y2] нижні праві координати ...
        """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:  # y1 (верхня точка м'яча) <= 0
            self.y = 3  # + повертаємо униз
        # if pos[3] >= self.canvas_height:  # y2 (нижня точка) >= поточній висоті полотна
        #     self.y = -3  # - повертаємо вверх
        # Перевіряємо, чи вдарився м'яч об ракетку
        if self.hit_paddle(pos) == True:
            self.y = -3
        # Перевіряємо, чи вдарився об дно екрану
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        # якщо так — жбурляємо його угору
        if pos[0] <= 0:
            self.x = 3  # -->
        if pos[2] >= self.canvas_width:
            self.x = -3  # <--

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if paddle_pos[2] <= pos[2] >= paddle_pos[0]:
            if paddle_pos[3] <= pos[3] >= paddle_pos[1]:
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        """ Додаємо рух до ракетки
            x = -2 для руху ліворуч і 2 — праворуч
        """
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # Пов'язуємо (біндимо) функції з відповідними клавішами
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        # -2 для руху ліворуч
        self.x = -2

    def turn_right(self, evt):
        # 2 — праворуч
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        """ Зупиняється, коли дістається країв вікна
        """
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, 'blue')
# paddle перед м'ячем, щоб передати цей елемент ф-ції класу
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()  # Перемальовують
    tk.update()  # полотно
    time.sleep(0.01)

# TODO 9.1 Відтермінувати початок гри
#     Додати прив'язку до події клацання мишкою
# TODO 9.2 Додати напис «Кінець гри»
# TODO 9.3 Зробити м'яч швидшим
#     Передавати прискорення від ракетки
# TODO 9.4 Записати рахунок гравця
