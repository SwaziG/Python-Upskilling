import turtle

def draw_multicolor_square(t, sz):
    """
    Make turtle t draw a multi-color square of sz.
    """
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

def draw_rectangle(t, w, h):
    """
    Get turtle t to draw a rectangle of width w and height h.
    """
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz): # A new version of draw_square
    """
    Uses the the draw_rectangle function filing in both w and h with the same value.
    """
    draw_rectangle(tx, sz, sz)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

wn.mainloop()