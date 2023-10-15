import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 3

shrinkingSquare(150)
shrinkingSquare(135)
shrinkingSquare(120)
shrinkingSquare(105)
shrinkingSquare(90)
shrinkingSquare(75)
shrinkingSquare(60)
shrinkingSquare(45)
shrinkingSquare(30)
shrinkingSquare(15)


turtle.done()
