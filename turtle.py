import turtle
turtle.speed(30)
turtle.width(2)
sc = turtle.Screen()
sc.setup(800, 800)
sc.bgcolor("black")
sc.title("Naqsh")

turtle.penup()
turtle.back(100)
turtle.pendown()

for n in range(25):
  for color in ["red", "yellow", "blue", "purple"]:
    turtle.color(color)
    turtle.forward(n*5)
    turtle.left(90)


for n in range(25):
  for color in ["red", "blue", "yellow", "purple"]:
    turtle.color(color)
    turtle.forward(n*5)
    turtle.right(90)

turtle.left(90)

for n in range(25):
  for color in ["red", "yellow", "blue", "purple"]:
    turtle.color(color)
    turtle.forward(n*5)
    turtle.left(90)

turtle.left(90)

for n in range(25):
  for color in ["red", "yellow", "blue", "purple"]:
    turtle.color(color)
    turtle.forward(n*5)
    turtle.left(90)
    