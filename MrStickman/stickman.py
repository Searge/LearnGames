import tkinter as tk
import random
import time

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
                    sprite.move
            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.01)


go = Game()
go.mainloop()
