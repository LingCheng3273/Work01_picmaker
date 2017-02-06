#Ling Cheng
#Work01_picmaker
#2/5/2017

def makeRed():
    return "255 0 0 "
def makeOrange():
    return "255 100 0 "
def makeYellow():
    return "255 255 0 "
def makeGreen():
    return "0 255 0 "
def makeBlue():
    return "0 0 255 "
def makePurple():
    return "255 0 255 "

def makeColor(color):
    if color == 0:
        return makeRed()
    if color == 1:
        return makeOrange()
    if color == 2:
        return makeYellow()
    if color == 3:
        return makeGreen()
    if color == 4:
        return makeBlue()
    else:
        return makePurple()


f = open("pic.ppm", "w")

content = "P3 600 600 255\n"

f.write(content)

#Hardcoding picture
"""for x in range(600):
    for y in range(600):
        if x / 100 == 0:
            f.write(makeColor(y/100))
        elif x / 100 == 1:
            if y / 100 <= 1:
                f.write(makeOrange())
            else:
                f.write(makeColor(y/100))
        elif x / 100 == 2:
            if y / 100 <= 2:
                f.write(makeYellow())
            else:
                f.write(makeColor(y/100))
        elif x / 100 == 3:
            if y / 100 <= 3:
                f.write(makeGreen())
            else:
                f.write(makeColor(y/100))
        elif x / 100 == 4:
            if y / 100 <= 4:
                f.write(makeBlue())
            else:
                f.write(makeColor(y/100))
        elif x / 100 == 5:
            if y / 100 <= 5:
                f.write(makePurple())
            else:
                f.write(makeColor(y/100))
"""

#Algorithm for picture
for x in range(600):
    for y in range(600):
        for counter in range(6):
            if x / 100 == counter:
                if y / 100 <= counter:
                    f.write(makeColor(counter))
                else:
                    f.write(makeColor(y/100))

f.write("\n")
print("done!!")
f.close()

