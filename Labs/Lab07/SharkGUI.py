#Malyka Ram
#
#SharkGUI
    #images are moving properly, but the fish orientation doesn't change...
    #The last thing I probably need to do is to create the personalized
        #input validation statments and instructional statements
        #but I am going to leave that until the end
    #other problem is that shark is not bouncing off walls, it simply goes off
    #the grid
    #To do List:
        #1.personalized messages for input validation
        #2.make sure shark STOPS pursuing dead fish, or else it just gets stuck at
            #-1,-1
            #so also make sure it bounces of the walls (being only the blue grid,
            #which should get rid of the problem
        #3. do stalemate cases
        #4. make sure quit button functions without error
        #5. fix the directional orientation of the fish images 
        

from graphics import *

class SharkGUI: 
    def __init__(self, sharky):
        self.sharky = sharky
        self.win = GraphWin("Shark game", 700, 700)
        self.win.setBackground("lightblue")
        self.win.setCoords(0.5,-1.5,10.5,10.5)
        fish_entry1 = Entry(Point(200,200), 5)
        fish_entry1.draw(self.win)
        fish_entry2 = Entry(Point(200,150), 5)
        fish_entry2.draw(self.win)
        fish_entry3 = Entry(Point(200,100), 5)
        fish_entry3.draw(self.win)       

        for i in range(11):
            vert_line = Line(Point(0.5,0.5), Point(0.5,10.5))
            vert_line.draw(self.win)
            vert_line_clone = vert_line.clone()
            vert_line_clone.move(1+i, 0)
            vert_line_clone.draw(self.win)
            hor_line = Line(Point(0.5,0.5), Point(10.5,0.5))
            hor_line.draw(self.win)
            hor_line_clone = hor_line.clone()
            hor_line_clone.move(0, 1+i)
            hor_line_clone.draw(self.win)

        white_box = Rectangle(Point(0.5,-1.5), Point(10.5,0.5))
        white_box.draw(self.win)
        white_box.setFill("white")
        
        self.input_text3 = Entry(Point(3.5, -1), 5)
        self.input_text3.draw(self.win)
        text3 = Text(Point(1.5, -1), "Enter fish position 3:")
        text3.draw(self.win)

        self.input_text2 = Entry(Point(3.5, -0.5), 5)
        self.input_text2.draw(self.win)
        text2 = Text(Point(1.5, -0.5), "Enter fish position 2:")
        text2.draw(self.win)
        
        self.input_text1 = Entry(Point(3.5, 0), 5)
        self.input_text1.draw(self.win)
        text1 = Text(Point(1.5, 0), "Enter fish position 1:")
        text1.draw(self.win)
        
        #for each point, to get the image in the actual boxes instead of the point
            #subtract both metrics by 0.5
    
    def add_object(self, obj):
        obj.draw(self.win)
     
    def remove_object(self, obj):
        obj.undraw()

    def create_quit_button(self, qbutton):
        rect1 = qbutton.getRectangle()
        label1 = qbutton.getLabel()
        self.add_object(rect1)
        self.add_object(label1)
        qbutton.activate()

    def valid_input(self, button1, button2):
        rect2 = button1.getRectangle()
        label2 = button1.getLabel()
        self.add_object(rect2)
        self.add_object(label2)
        button1.activate()
        while True:
            pt = self.win.getMouse()
            if button1.clicked(pt):
                button1.deactivate()
                try:
                    loc_1 = self.input_text1.getText()
                    list_xy_1 = loc_1.split(",")
                    x1,y1 = int(list_xy_1[0]), int(list_xy_1[1])
                    print(x1)
                    print(y1)
                    
                    loc_2 = self.input_text2.getText()
                    list_xy_2 = loc_2.split(",")
                    x2,y2 = int(list_xy_2[0]), int(list_xy_2[1])
                    print(x2)
                    print(y2)

                    loc_3 = self.input_text3.getText()
                    list_xy_3 = loc_3.split(",")
                    x3,y3 = int(list_xy_3[0]), int(list_xy_3[1])
                    print(x3)
                    print(y3)

                    length_x1 = len(str(x1))
                    print(length_x1)
                    length_x2 = len(str(x2))
                    print(length_x2)
                    length_x3 = len(str(x3))
                    print(length_x3)
                    
                    if length_x1 == 1 and length_x2 == 1 and length_x3 == 1:
                        length_y1 = len(str(y1))
                        print(length_y1)
                        length_y2 = len(str(y2))
                        print(length_y2)
                        length_y3 = len(str(y3))
                        print(length_y3)
                        if length_y1 == 1 and length_y2 == 1 and length_y3 == 1:
                            print("Yeah babe!")
                            initial_xy_positions = [x1, y1, x2, y2, x3, y3]
                            button1.undraw()
                            rect3 = button2.getRectangle()
                            label3 = button2.getLabel()
                            self.add_object(rect3)
                            self.add_object(label3)
                            button2.activate()
                            return initial_xy_positions
                        else:
                           print("Nice try...Your y coord needs to be 0-9")
                           button1.activate()
                except:
                    print("Something went wrong")
                    button1.activate()


    def create_a_fish_1(self, fish_1):
        self.fish_1 = fish_1
        self.fish_1_img = self.fish_1.getImage()
        self.add_object(self.fish_1_img)

    def create_a_fish_2(self, fish_2):
        self.fish_2 = fish_2
        self.fish_2_img = self.fish_2.getImage()
        self.add_object(self.fish_2_img)
        
    def create_a_fish_3(self, fish_3):
        self.fish_3 = fish_3
        self.fish_3_img = self.fish_3.getImage()
        self.add_object(self.fish_3_img)
       
    def update_shark(self):
##        fish_1 = self.fish_list[0]
##        fish_2 = self.fish_list[1]
##        fish_3 = self.fish_list[2]
        fish_1_pos_x, fish_1_pos_y = self.fish_1.getPosition()
        fish_1_pos = [fish_1_pos_x, fish_1_pos_y]
        fish_2_pos_x, fish_2_pos_y = self.fish_2.getPosition()
        fish_2_pos = [fish_2_pos_x, fish_2_pos_y]
        fish_3_pos_x, fish_3_pos_y = self.fish_3.getPosition()
        fish_3_pos = [fish_3_pos_x, fish_3_pos_y]
        fish_positions = [fish_1_pos, fish_2_pos, fish_3_pos]
        old = self.sharky.get_image()
        old.undraw()
        self.sharky.move(fish_positions)
        self.redraw_fish()
        new_img = self.sharky.get_image()
        new_img.draw(self.win)

##    def redraw_fish(self):
        #everything in update fish except instead of move, its update for sharkmove
        #call redraw fish in sharkupdate
    def redraw_fish(self):
        shark_pos_x, shark_pos_y = self.sharky.get_shark_pos()
        self.fish_1_img.undraw()
        self.fish_2_img.undraw()
        self.fish_3_img.undraw()
        self.fish_1.updateForSharkMove(shark_pos_x, shark_pos_y)
        self.fish_2.updateForSharkMove(shark_pos_x, shark_pos_y)
        self.fish_3.updateForSharkMove(shark_pos_x, shark_pos_y)
        self.fish_1_img = self.fish_1.getImage()
        self.fish_2_img = self.fish_2.getImage()
        self.fish_3_img = self.fish_3.getImage()
        self.fish_1_img.draw(self.win)
        self.fish_2_img.draw(self.win)
        self.fish_3_img.draw(self.win)
        
    def move_fish(self):
        shark_pos_x, shark_pos_y = self.sharky.get_shark_pos()
        fish1_x_pos, fish1_y_pos = self.fish_1.getPosition()
        fish2_x_pos, fish2_y_pos = self.fish_2.getPosition()
        fish3_x_pos, fish3_y_pos = self.fish_3.getPosition()  
        #fish 1
        if (fish1_x_pos == shark_pos_x) and (fish1_y_pos == shark_pos_y):
            self.fish_1_img.undraw()
            self.fish_1.eaten()
            self.fish_1.setPosition(-1,-1)
            
        elif self.fish_1.isAlive():
            #old pos
            dnx, dny = self.fish_1.getPosition()
            self.fish_1_img.undraw()
            self.fish_1.move(shark_pos_x, shark_pos_y, self.fish_2, self.fish_3)
            print(self.fish_1.getPosition())
            self.fish_1_img = self.fish_1.getImage()
            #new pos
            gnx, gny = self.fish_1.getPosition()
            self.fish_1_img.draw(self.win)
            
        #fish 2
        if (fish2_x_pos == shark_pos_x) and (fish2_y_pos == shark_pos_y):
            self.fish_2_img.undraw()
            self.fish_2.setPosition(-1,-1)
            
        elif self.fish_2.isAlive():
            #old pos
            lnx, lny = self.fish_2.getPosition()
            self.fish_2_img.undraw()
            self.fish_2.move(shark_pos_x, shark_pos_y, self.fish_1, self.fish_3)
            self.fish_2_img = self.fish_2.getImage()
            #new pos
            pnx, pny = self.fish_2.getPosition()
            self.fish_2_img.draw(self.win)
      
        #fish 3
        if (fish3_x_pos == shark_pos_x) and (fish3_y_pos == shark_pos_y):
            self.fish_3_img.undraw()
            self.fish_3.setPosition(-1,-1)
            
        elif self.fish_3.isAlive():
            rnx, rny = self.fish_3.getPosition()
            self.fish_3_img.undraw()
            self.fish_3.move(shark_pos_x, shark_pos_y, self.fish_1, self.fish_2)
            self.fish_3_img = self.fish_3.getImage()
            #new pos
            onx, ony = self.fish_3.getPosition()
            self.fish_3_img.draw(self.win)

    def update(self, moveButton, quitButton):
        pt = self.win.getMouse()
        print("got click")
        if moveButton.clicked(pt):
            print("move clicked")
            lab = moveButton.getLabel()
            text = lab.getText()
            if text == "Move Fish":
                print("label was move fish")
                moveButton.setLabel("Move Shark")
                self.move_fish()
            elif text == "Move Shark":
                moveButton.setLabel("Move Fish")
                self.update_shark()
        elif quitButton.clicked(pt):
            self.win.close()
            
    def check_if_stalemate(self):
        # Alison
        numFishAlive = 0
        fishNum = 1
        if self.fish_1.isAlive():
            numFishAlive += 1
        if self.fish_2.isAlive():
            numFishAlive += 1
            fishNum = 2
        if self.fish_3.isAlive():
            numFishAlive += 1
            fishNum = 3

        if numFishAlive != 1:
            return False

        # only one fish left
        if fishNum == 1:
            return self.checkStalemate(fishNum)
        elif fishNum == 2:
            return self.checkStalemate(fishNum)
        elif fishNum == 3:
            return self.checkStalemate(fishNum)
        
        return False

    def checkStalemate(self, fishNum):
        if fishNum == 1:
            curFish = self.fish_1
        elif fishNum == 2:
            curFish = self.fish_2
        elif fishNum == 3:
            curFish = self.fish_3

        x,y = curFish.getPosition()
        sharkX, sharkY = self.sharky.get_shark_pos()

        # horizontal case
        if sharkY == y:
            # x is 1 and sharkX is 2
            if (x == 1 and sharkX == 2):
                return True
            # x is 1 and sharkX is 3
            if (x == 1 and sharkX == 3):
                return True
            # x is 10 and sharkX is 9
            if (x == 10 and sharkX == 9):
                return True
            # x is 10 and sharkX is 8
            if (x == 10 and sharkX == 8):
                return True
        # vertical case
        if sharkX == x:
            # y is 1 and sharkY is 2
            if (y == 1 and sharkY == 2):
                return True
            # y is 1 and sharkY is 3
            if (y == 1 and sharkY == 3):
                return True
            # y is 10 and sharkY is 9
            if (y == 10 and sharkY == 9):
                return True
            # y is 10 and sharkY is 8
            if (y == 10 and sharkY == 8):
                return True
            
        return False
            
