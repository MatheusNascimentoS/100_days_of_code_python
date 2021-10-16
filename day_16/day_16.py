# from turtle import Screen, Turtle

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight) 
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

table.align = "l"
print(table)

