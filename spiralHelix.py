import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("grey")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")
turtle_colors = ["red", "blue", "yellow", "green", "purple", "orange", "black"]
turtle_instance.speed(0)

for i in range(10):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.right(i)

turtle.mainloop()