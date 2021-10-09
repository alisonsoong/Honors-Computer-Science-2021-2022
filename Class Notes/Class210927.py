from graphics import *

def changeColor():
    myFirstWindow = GraphWin()
    #myFirstWindow.setBackground(graphics.color_rgb(255,0,0)) # would need to use 'import graphics' instead
    myFirstWindow.setBackground(color_rgb(20,60,80))
    myFirstWindow.setBackground(color_rgb(100,155,155))

def myGUI():
	myFirstWindow = GraphWin()
	
	p1 = Point(80,40)
	p1.draw(myFirstWindow)
	
	p2 = Point(130,180)
	p2.draw(myFirstWindow)

	r = Rectangle(p1, p2)
	r.setFill('blue') # already defined colors
	r.draw(myFirstWindow)

	label = Text(Point(105,110), "Blue Rectangle")
	label.draw(myFirstWindow) # always have to draw objects on the screen





	
	
