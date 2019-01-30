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
