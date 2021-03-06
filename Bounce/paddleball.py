import tkinter as tk
import random
import time

size = 600

half_size = size / 2                # 300
one_fourth = size / 4               # 200
three_fourth = size - one_fourth    # 400
one_sixtieth = size / 60            # 10
one_tenth = size / 10               # 60

colors = ('#068587', '#46B29D', '#4FB99F',
          '#F0CA4D', '#E37B40', '#DE5B49')

root = tk.Tk()
root.title("Гра")
root.resizable(0, 0)
# вимикаємо можливість змінювати розмір вікна
root.wm_attributes("-topmost", 1)
#  атрибути менеджжера вікон — найвище.
canvas = tk.Canvas(root, width=500, height=400,
                   bd=0, highlightthickness=0)
#               вимикаємо контур вікн
canvas.pack()
root.update()


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
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
        # if pos[3] >= self.canvas_height:  # y2 (нижня точка)
        #                                       >= поточній висоті полотна
        #     self.y = -3  # - повертаємо вверх
        # Перевіряємо, чи вдарився м'яч об ракетку
        if self.hit_paddle(pos):
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
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[3] <= pos[3] >= paddle_pos[1]:
                self.x += self.paddle.x
                self.score.hit()
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
        self.started = False
        # Пов'язуємо (біндимо) функції з відповідними клавішами
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

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

    def start_game(self, evt):
        self.started = True


class Score:
    """docstring for Score"""

    def __init__(self, canvas, color):
        super(Score, self).__init__()
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10,
                                     text=self.score,
                                     fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

#    ______                        ____             _
#   / ____/___ _____ ___  ___     ( __ )___  ____ _(_)___
#  / / __/ __ `/ __ `__ \/ _ \   / __  / _ \/ __ `/ / __ \
# / /_/ / /_/ / / / / / /  __/  / /_/ /  __/ /_/ / / / / /
# \____/\__,_/_/ /_/ /_/\___/  /_____/\___/\__, /_/_/ /_/
#                                         /____/


score = Score(canvas, 'red')
paddle = Paddle(canvas, 'blue')
# paddle перед м'ячем, щоб передати цей елемент ф-ції класу
ball = Ball(canvas, paddle, score, 'red')
game_over_text = canvas.create_text(250, 200,
                                    text='КІНЕЦЬ ГРИ',
                                    state='hidden')

start_the_game = canvas.create_text(250, 200,
                                    text="START!",
                                    font=('Helvetica Bold', 21),
                                    state='hidden')


while 1:
    if ball.hit_bottom is False and paddle.started is True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    root.update_idletasks()  # Перемальовують
    root.update()  # полотно
    time.sleep(0.01)


# TODO 9.4 Записати рахунок гравця
