import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # First side
    koch_curve(t, order, size)

    # Second side
    t.setheading(-120)
    koch_curve(t, order, size)

    # Third side
    t.setheading(-240)
    koch_curve(t, order, size)


    window.mainloop()

# Виклик функції
draw_koch_curve(4)
