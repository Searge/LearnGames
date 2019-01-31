import tkinter as tk
import time
# import random

size: int = 500
spr = "sprites/"
plate = ("platform0.gif", "platform1.gif", "platform2.gif")


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Містер Руки-палички біжить до виходу")
        self.root.resizable(0, 0)
        self.root.wm_attributes("-topmost", 1)
        self.canvas = tk.Canvas(self.root, width=size, height=size,
                                highlightthickness=0)
        self.canvas.pack()
        self.root.update()
        self.canvas.width = size
        self.canvas.height = size
        self.bg = tk.PhotoImage(file="sprites/background.gif")
        self.bg2 = tk.PhotoImage(file="sprites/background2.gif")
        w = self.bg.width()
        h = self.bg.height()
        draw = True
        for columns in range(5):
            for rows in range(5):
                if draw:
                    self.canvas.create_image(columns * w, rows * h,
                                             image=self.bg, anchor='nw')
                    draw = False
                else:
                    self.canvas.create_image(columns * w, rows * h,
                                             image=self.bg2, anchor='nw')
                    draw = True
        self.sprites = []
        self.running = True

    def mainloop(self):
        while True:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.01)


class Coords:
    """ Вказує позиції об'єктів на ігровому екрані.
        Зберігає верхню ліву (x1, y1)
        і нижню праву (x2, y2) координати
        будь-якого компонента гри.
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        super(Coords, self).__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    """ Приймає два аргументи (об'єкти класу Coords) та визначає,
        чи один набір координати x (x1, x2)
        перетнув другий набір координат x (x1, x2)
    """
    if (co2.x2 > co1.x1 > co2.x1) \
            or (co2.x2 > co1.x2 > co2.x1) \
            or (co1.x2 > co2.x1 > co1.x1) \
            or (co1.x2 > co2.x2 > co1.x1):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co2.y2 > co1.y1 > co2.y1) \
            or (co2.y2 > co1.y2 > co2.y1) \
            or (co1.y2 > co2.y1 > co1.y1) \
            or (co1.y2 > co2.y2 > co1.y1):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co2.x2 >= co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co2.x2 >= co1.x2 >= co2.x1:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co2.y2 >= co1.y1 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if co2.y2 >= y_calc >= co2.y1:
            return True
    return False


class Sprite:
    """docstring for Sprite"""

    def __init__(self, game):
        super(Sprite, self).__init__()
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class Platform(Sprite):
    """docstring for Platform"""

    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y,
                                              image=self.photo_image,
                                              anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)


go = Game()

platform1 = Platform(go, tk.PhotoImage(file=spr + plate[0]),
                     0, 480, 100, 10)
platform2 = Platform(go, tk.PhotoImage(file=spr + plate[0]),
                     150, 440, 100, 10)
platform3 = Platform(go, tk.PhotoImage(file=spr + plate[0]),
                     300, 400, 100, 10)
platform4 = Platform(go, tk.PhotoImage(file=spr + plate[0]),
                     300, 160, 100, 10)
platform5 = Platform(go, tk.PhotoImage(file=spr + plate[1]),
                     175, 350, 66, 10)
platform6 = Platform(go, tk.PhotoImage(file=spr + plate[1]),
                     50, 300, 66, 10)
platform7 = Platform(go, tk.PhotoImage(file=spr + plate[1]),
                     170, 120, 66, 10)
platform8 = Platform(go, tk.PhotoImage(file=spr + plate[1]),
                     45, 60, 66, 10)
platform9 = Platform(go, tk.PhotoImage(file=spr + plate[2]),
                     170, 250, 32, 10)
platform10 = Platform(go, tk.PhotoImage(file=spr + plate[2]),
                      230, 200, 32, 10)
go.mainloop()
