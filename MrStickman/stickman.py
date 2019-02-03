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
        self.canvas_width = size
        self.canvas_height = size
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
            if self.running == True:
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


class StickMan(Sprite):
    """docstring for StickMan"""

    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [
            tk.PhotoImage(file=spr + 'stickman-L1.gif'),
            tk.PhotoImage(file=spr + 'stickman-L2.gif'),
            tk.PhotoImage(file=spr + 'stickman-L3.gif')
        ]
        self.images_right = [
            tk.PhotoImage(file=spr + 'stickman-R1.gif'),
            tk.PhotoImage(file=spr + 'stickman-R2.gif'),
            tk.PhotoImage(file=spr + 'stickman-R3.gif')
        ]
        self.image = game.canvas.create_image(200, 470,
                                              image=self.images_left[0],
                                              anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(
                    self.image,
                    image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(
                    self.image,
                    image=self.images_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1
        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        if self.x > 0 and co.x2 >= self.game.canvas_height:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False

        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False

            if bottom and self.y > 0 and collided_bottom(self.y,
                                                         co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False

            if bottom and falling and self.y == 0 \
                    and co.y2 < self.game.canvas_height \
                    and collided_bottom(1, co, sprite_co):
                falling = False

            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.game.running = False
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.game.running = False
        if falling and bottom \
                and self.y == 0 \
                and co.y2 < self.game.canvas_height:
            self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)

    def end(self, sprite):
        self.game.running = False
        sprite.opendoor()
        time.sleep(1)
        self.game.canvas.itemconfig(self.image, state='hidden')
        sprite.closedoor()


class Door(Sprite):
    """Doors"""
    def __init__(self, game, x, y, width, height):
        Sprite.__init__(self, game)
        self.closed_door = tk.PhotoImage(file=spr + 'door1.gif')
        self.open_door = tk.PhotoImage(file=spr + 'door2.gif')
        self.image = game.canvas.create_image(x, y,
                                              image=self.closed_door,
                                              anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True

    def opendoor(self):
        self.game.canvas.itemconfig(self.image, image=self.open_door)
        self.game.root.update_idletasks()

    def closedoor(self):
        self.game.canvas.itemconfig(self.image, image=self.closed_door)


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

go.sprites.append(platform1)
go.sprites.append(platform2)
go.sprites.append(platform3)
go.sprites.append(platform4)
go.sprites.append(platform5)
go.sprites.append(platform6)
go.sprites.append(platform7)
go.sprites.append(platform8)
go.sprites.append(platform9)
go.sprites.append(platform10)

# for i in range(1, 10 + 1):
#     go.sprites.append('platform' + str(i))

door = Door(go, 45, 30, 40, 35)
go.sprites.append(door)
sf = StickMan(go)
go.sprites.append(sf)
go.mainloop()
