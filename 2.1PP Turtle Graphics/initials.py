"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "YOUR NAME"

import turtle as t


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(3)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
    # moves to rhe start of the N, changes the pen size and colour
    t.penup()
    t.pensize(10)
    t.pencolor("magenta")
    t.left(135)
    t.forward(200)
    t.right(45)
    t.pendown()
    #draws the N
    t.forward (120)
    t.right(150)
    t.forward(140)
    t.left(150)
    t.forward(120)
    #moves to the start of the S and changes the colour
    t.penup()
    t.right(90)
    t.forward(300)
    t.right(180)
    t.pendown()
    t.pencolor("cyan")
    # draws the S
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(60)
    t.penup()
    t.left(45)
    t.forward(300)
    t.pendown()
    t.pencolor("green")
    # draws a circle 
    degree = 360
    while degree >0:
        t.forward(1)
        t.left(1)
        degree -= 1



    # Avoid closing the window automatically
    t.mainloop()


if __name__ == "__main__":
    main()
