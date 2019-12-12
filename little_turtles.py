import turtle
from random import randint

class turtle_racer():
    def __init__(self, color, position):
        self.color = color
        self.pos = position
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.color(color)
        self.turt.shape('turtle')
        self.turt.setpos(position)
        self.turt.setheading(90)
        self.turt.speed(1)

    def update(self):
        speed = randint(10, 20)
        x, y = self.pos
        y += speed
        self.pos = (x, y)
        self.turt.forward(speed)
        return self.pos

    def win(self, win_condition):
        x, y = self.pos
        return y >= win_condition

def game_start():
    colors = ['red', 'green', 'pale goldenrod', 'violet', 'royal blue', 'PaleVioletRed3', 'SeaGreen3', 'SlateGray4']
    turtle_nums = 8
    width = -500
    list_turtle = []
    win_condition = 300

    for color in colors:
        width += 100
        list_turtle.append(turtle_racer(color, (width, -200)))

    win = False
    while not win:
        for turtle in list_turtle:
            turtle.update()
            win = turtle.win(win_condition)
            if win:
                print('winner: ', turtle.color)
                break


wn = turtle.Screen()
wn.screensize(500, 1000, 'lightgreen')

start = True
while start:
    game_start()
    start = input('Do you want to watch again(yes?): ')
    if start == "yes": start = True
    else:
        wn.bye()
    wn.clearscreen()
    wn.screensize(500, 1000, 'lightgreen')

wn.mainloop()


# def draw_clock(steps):
#
#     wn = turtle.Screen()
#     wn.screensize(500, 1000, 'yellow')
#
#     alex = turtle.Turtle()
#     alex.shape('turtle')
#
#     bar = steps / 10
#     line = bar * (10 - 2)
#     for _ in range(12):
#         alex.penup()
#         alex.forward(line)
#         alex.pendown()
#         alex.forward(bar)
#         alex.penup()
#         alex.forward(bar)
#         alex.stamp()
#         alex.backward(steps)
#         alex.left(30)
#
#     wn.mainloop()
#
# draw_clock(200)

# def draw_star(steps):
#
#     wn = turtle.Screen()
#     wn.screensize(500, 1000, 'yellow')
#
#     alex = turtle.Turtle()
#
#     alex.left(36)
#     alex.forward(steps)
#     for _ in  range(4):
#         alex.left(144)
#         alex.forward(steps)
#
#     alex.left(108)
#
#     wn.mainloop()
#
# draw_star(250)


# def draw_star(steps):
#
#     wn = turtle.Screen()
#     wn.bgcolor('lightgreen')
#     wn.window_height()
#     wn.window_width()
#
#     alex = turtle.Turtle()
#
#     alex.left(36)
#     alex.forward(steps)
#     for _ in  range(4):
#         alex.left(144)
#         alex.forward(steps)
#
#     alex.left(108)
#     wn.mainloop()
#
# draw_star(250)











# def regular_polygons(edge):
#     wn = turtle.Screen()
#     wn.bgcolor('lightgreen')
#     wn.title(str(edge))
#     wn.window_height()
#     wn.window_width()
#
#     alex = turtle.Turtle()
#     for _ in  range(edge):
#         alex.forward(100)
#         alex.left(360/edge)
#
#     wn.mainloop()
#
# regular_polygons(18)