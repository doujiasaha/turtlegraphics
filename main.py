from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("circle")

print(timmy)
timmy.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

my_screen = Screen()
my_screen.screensize(400,400)
my_screen.colormode(255)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

timmy.speed("fastest")

#spirograph
def spirograph(size):
    for _ in range(int(360/size)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)
    
spirograph(7)

 
"""#randomwalk

path = [0,90,180,270]
timmy.pensize(10)
while True:
    timmy.speed("fast")
    timmy.pencolor(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(path))"""
    

"""triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon"""
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(50)
#         timmy.right(angle) 

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
    

 



print(my_screen.canvheight)
my_screen.exitonclick()