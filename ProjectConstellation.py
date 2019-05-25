# Coder: Andrew R Cabezudo, 2019.5.25, Ver:1
# The code is a digital reprentation of the constellation Orion
# Angle/Distance references taken from the following webpage:
# http://wordpress.mrreid.org/2011/10/30/constellations-from-a-different-angle/

import turtle
turtle.hideturtle()
turtle.pensize(3)

#Draw Betelgeuse
turtle.penup()
turtle.goto(-400,370)
turtle.pendown()
turtle.dot(14)
turtle.penup()
turtle.goto(-400,360)
turtle.pendown()
turtle.write("   Betelgeuse", move=False, align="left", font=(10))
turtle.penup()
turtle.goto(-400,370)
turtle.pendown()

#Draw Alnitak
turtle.goto(-260,-100)
turtle.pendown()
turtle.dot(14)
turtle.penup()
turtle.goto(-260,-120)
turtle.pendown()
turtle.write("  Alnitak", move=False, align="left", font=(10))
turtle.penup()
turtle.goto(-260,-100)
turtle.pendown()

#Draw Saiph
turtle.goto(-380,-480)
turtle.pendown()
turtle.dot(14)
turtle.penup()
turtle.goto(-400,-508)
turtle.pendown()
turtle.write("Saiph", move=False, align="left", font=(10))
turtle.penup()

#Draw Alnilam
turtle.goto(-260,-100)
turtle.pendown()
turtle.goto(-180,-60)
turtle.dot(14)
turtle.penup()
turtle.goto(-180,-80)
turtle.pendown()
turtle.write("  Alnilam", move=False, align="left", font=(10))
turtle.penup()
turtle.goto(-180,-60)
turtle.pendown()

#Draw Mintaka
turtle.goto(-115,-20)
turtle.dot(14)
turtle.penup()
turtle.goto(-115,-30)
turtle.pendown()
turtle.write("   Mintaka", move=False, align="left", font=(10))
turtle.penup()
turtle.goto(-115,-20)
turtle.pendown()

#Draw Meissa
turtle.goto(-10,320)
turtle.dot(14)
turtle.penup()
turtle.goto(-31,328)
turtle.pendown()
turtle.write("Meissa", move=False, align="left", font=(10))
turtle.penup()
turtle.goto(-115,-20)
turtle.pendown()

#Draw Rigel
turtle.goto(170,-405)
turtle.dot(14)
turtle.penup()
turtle.goto(154,-432)
turtle.pendown()
turtle.write("Rigel", move=False, align="left", font=(10))


