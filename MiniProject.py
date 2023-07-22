# import modules
#generate or manipulate random numbers
import random as r
#drawing board
import turtle as t

# set the screen
Screen = t.Screen()

# choose background color
Screen.bgcolor("gray")


# define the function for creating a square section for the game

def Square(x, y):

    # change the color of the turtle
    t.color('white', 'pink')
    # pull the pen up from the screen
    t.up()
    # move the turtle to an absolute position
    t.goto(x, y)
    # pull back the pen down on the screen
    t.down()
    # call just before drawing a shape to be filled
    t.begin_fill()

    for count in range(4):
        # move the turtle forward
        t.forward(50)
        # change the direction of the turtle
        t.left(90)
        # Fill the shape drawn after the call begin_fill()
    t.end_fill()


# define function to keep a check of index number
def Numbering(x, y):

    return int((x + 200) // 50
               + ((y + 200) // 50) * 8)


# define function keep the position
def Coordinates(count):

    return (count % 8) * 50 - 200\
        , (count // 8) * 50 - 200


# define function to make it interactive user click
def click(x, y):

    spot = Numbering(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:

        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

# show the numbers
def draw():

    t.clear()
    t.goto(0, 0)
    t.stamp()

    for count in range(64):

        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:

        x, y = Coordinates(mark)
        t.up()
        t.goto(x + 2, y)
        t.color('black')
        t.write(tiles[mark], font=('Arial', 30, 'normal'))

    t.update()
    # install a timer
    t.ontimer(draw, 10)


tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

# for shuffling the numbers placed inside the square tiles
r.shuffle(tiles)
# turn turtle animation on or off and set a delay for update drawings
t.tracer(False)
#bind fun to a mouse-click event on canvas
t.onscreenclick(click)
draw()
# starts event loop
t.done()


