import tkinter as tk
import time
import random

size = 500


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
        w = self.bg.width()
        h = self.bg.height()
        for x in range(5):
            for y in range(5):
                self.canvas.create_image(x * w, y * h,
                                         image=self.bg, anchor='nw')
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


class Coords():
    """docstring for Coords"""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        super(Coords, self).__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co2.x2 > co1.x1 > co2.x1) \
            or (co2.x2 > co1.x2 > co2.x1) \
            or (co1.x2 > co2.x1 > co1.x1) \
            or (co1.x1 > co2.x2 > co1.x1):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co2.y2 > co1.y1 > co2.y1) \
            or (co2.y2 > co1.y2 > co2.y1) \
            or (co1.y2 > co2.y1 > co1.y1) \
            or (co1.y1 > co2.y2 > co1.y1):
        return True
    else:
        return False


go = Game()
go.mainloop()
