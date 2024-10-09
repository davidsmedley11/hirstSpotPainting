import colorgram
import random
import turtle as t


tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.goto(-350, -350)
t.bgcolor(233, 233, 232)

colors = colorgram.extract("wallpaper.png", 14)
print(colors)

def get_random_color(random_choice):
    r = colors[random_choice].rgb[0]
    g = colors[random_choice].rgb[1]
    b = colors[random_choice].rgb[2]
    chosen_colour = (r, g, b)
    return chosen_colour

def draw_circle(chosen_colour):
    tim.color(chosen_colour)
    tim.fillcolor(chosen_colour)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()

def move_column():

    for _ in range(8):
        colour = get_random_color(random.randint(0,13))
        draw_circle(colour)
        tim.forward(100)

def move_row():
    tim.right(180)
    tim.forward(800)
    tim.right(90)
    tim.forward(100)
    tim.right(90)

for _ in range(8):
    move_column()
    move_row()

screen = t.Screen()
screen.exitonclick()
screen.screensize(1000, 1000)
