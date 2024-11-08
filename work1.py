import turtle

house = turtle.Turtle()

for i in range(4):
    if i == 0:

        house.forward(75)
        house.left(90)
        house.forward(100)
        house.right(90)
        house.forward(50)
        house.right(90)
        house.forward(100)
        house.left(90)
        house.forward(75)
        house.left(90)
    else:
        house.forward(200)
        house.left(90)        


house.left(90)
house.forward(200)
house.right(45)
house.forward(141.42)
house.right(90)
house.forward(141.42)
house.right(45)
house.forward(200)
