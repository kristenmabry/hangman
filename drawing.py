from graphics import *

"""
Example Code
===============================================================================
win = GraphWin("Example", 200, 200)

a = Line(Point(50, 0), Point(50, 200))
b = Circle(Point(125, 50), 25)
c = Rectangle(Point(100, 125), Point(175, 175))

a.setWidth(10)
b.setFill("blue")
c.setOutline("red")

a.draw(win)
b.draw(win)
c.draw(win)
===============================================================================
"""

#Hangman Graphics: make your window here
win = GraphWin("Hangman", 200,400)

#Scaffold code here
top_right_corner = Point(100,350)
bottom_left_corner = Point(15,390)
scaffold = Rectangle(top_right_corner, bottom_left_corner)
scaffold.draw(win)

top_of_pole = Point(57.5, 10)
bottom_of_pole = Point(57.5, 350)
pole = Line(top_of_pole, bottom_of_pole)
pole.draw(win)

left_horizontal = Point(57.5, 10)
right_horizontal = Point(132.5, 10)
horizontal = Line(left_horizontal, right_horizontal)
horizontal.draw(win)

top_down = Point(132.5, 10)
bottom_down = Point(132.5, 30)
down_line = Line(top_down, bottom_down)
down_line.draw(win)

#Head code here
circ_center = Point(132.5, 60)
circ_radius = 30
head = Circle(circ_center, circ_radius)
head.draw(win)

#Torso code here
top_torso = Point(132.5, 90)
bottom_torso = Point(132.5, 220)
torso = Line(top_torso, bottom_torso)
torso.draw(win)

#Left Leg code here
top_left_leg = Point(132.5, 220)
bottom_left_leg = Point(90, 290)
left_leg = Line(top_left_leg, bottom_left_leg)
left_leg.draw(win)

#Right Leg code here
top_right_leg = Point(132.5, 220)
bottom_right_leg = Point(175, 290)
right_leg = Line(top_right_leg, bottom_right_leg)
right_leg.draw(win)

#Left Arm code here
top_left_arm = Point(132.5, 120)
bottom_left_arm = Point(100, 200)
left_arm = Line(top_left_arm, bottom_left_arm)
left_arm.draw(win)

#Right Arm code here
top_right_arm = Point(132.5, 120)
bottom_right_arm = Point(165, 200)
right_arm = Line(top_right_arm, bottom_right_arm)
right_arm.draw(win)

win.getMouse()
win.close()

