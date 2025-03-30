# from turtle import Turtle, Screen
# import random


# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")

# for i in range(100):
#     timmy.forward(10)
#     timmy.left(10)
#     timmy.forward(10)
#     timmy.left(10)
#     timmy.forward(10)
#     timmy.right(10)
#     timmy.teleport(random.randint(1,100))
    

 
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.align = "l"

table.field_names = ["Pokémon","Type"]
table.add_rows( 
    [
        ["Pikachu","Electric"],
        ["Mudkip","Water"],
    ]
)

print(table)