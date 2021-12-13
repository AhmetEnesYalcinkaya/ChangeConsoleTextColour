import random
from sty import fg #you need to downloand to "sty" with pip install sty 

def generateRGB():
    """
    generate random 
    RGB colours
    """
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red,green,blue):
    """
    we create to change 
    foreground's colour
    """
    return fg(red,green,blue)

red,green,blue = generateRGB()
colour = generateColour(red,green,blue)

print(colour, "I'm randomly changing colours!",fg.rs)

