import random
import math
from graphics import *

# Maybe make Position a class
class Position:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

class Shark:
    def __init__(self, shark_pos, file_name):
        self.x_pos = shark_pos[0]
        self.y_pos = shark_pos[1]
        #make sure its in same folder
        self.image = Image(Point(self.x_pos,self.y_pos),file_name)

    def get_pos_closest_fish(self, fish_positions):
        max_dist = 100
        min_dist = max_dist
        min_idx = 0

        my_pos = [self.x_pos, self.y_pos]

        for index, fish_pos in enumerate(fish_positions):
            cur_dist = math.dist(my_pos, fish_pos)
            if cur_dist < min_dist:
                min_dist = cur_dist
                min_idx = index
            #pick between two fish if they are equal distance 
            if cur_dist == min_dist:
                if random.randint(0,1) == 0:
                    min_idx = index
                  
        return fish_positions[min_idx]

    def get_adjusted_pos(self, shark_pos):
        """Returns the adjusted position: checks if hitting a wall"""

        #sets the boundaries of the shark's movement,
            #so essentially if the shark tries to pass through the wall,
            #it will bounce back
        
        if self.x_pos > 10.5: 
            self.x_pos = 10
        elif self.x_pos < 0.5: 
            self.x_pos = 1
        elif self.y_pos > 10.5: 
            self.y_pos = 10
        elif self.y_pos < 0.5: 
            self.y_pos = 1
        
        return self.x_pos, self.y_pos


    #if the fish is dead, position will be (-1,-1)
    #how am I gonna do if the fish is closer than two spots then break it
    
    def move(self, fish_positions):
        old_pos = self.get_shark_pos()
        old_img = self.get_image()
        my_pos = [self.x_pos, self.y_pos]
        closest_fish_pos = self.get_pos_closest_fish(fish_positions)
        fish_x_pos = closest_fish_pos[0]
        fish_y_pos = closest_fish_pos[1]

        if math.dist(closest_fish_pos, my_pos) <= math.sqrt(2):
            self.x_pos = fish_x_pos
            self.y_pos = fish_y_pos
            return

        for fish in fish_positions:
            fish_x, fish_y = fish[0], fish[1]
            if fish_x == -1 and fish_y == -1:
                fish_positions.remove(fish)
        

        #if shark gets to boundaries it should bounce back into grid
        if self.x_pos > 10.5: 
            self.x_pos = 10
        if self.x_pos < 0.5: 
            self.x_pos = 1
        if self.y_pos > 10.5: 
            self.y_pos = 10
        if self.y_pos < 0.5: 
            self.y_pos = 1   
    
            
        # check if shark is in same row as fish
        if self.y_pos == fish_y_pos:
            if fish_x_pos > self.x_pos:
                self.x_pos += 2
            elif fish_x_pos < self.x_pos:
                self.x_pos -= 2
        elif self.x_pos == fish_x_pos: # check if shark is in same column as fish
            if fish_y_pos > self.y_pos:
                self.y_pos += 2
            elif fish_y_pos < self.y_pos:
                self.y_pos -= 2
        else:
            # check if we need to move NE
            if (fish_x_pos >= self.x_pos) and (fish_y_pos >= self.y_pos):
                self.x_pos += 2
                self.y_pos += 2
            #southwest
            elif (fish_x_pos <= self.x_pos) and (fish_y_pos <= self.y_pos): # move SW
                self.x_pos -= 2
                self.y_pos -= 2
            #southeast
            elif (fish_x_pos <= self.x_pos) and (fish_y_pos >= self.y_pos): # move NW
                self.x_pos -= 2
                self.y_pos += 2
            #southwest
            elif (fish_x_pos >= self.x_pos) and (fish_y_pos <= self.y_pos): # move SE
                self.x_pos += 2
                self.y_pos -= 2
                
        dx = self.x_pos - old_pos[0]
        dy = self.y_pos - old_pos[1]
        old_img.move(dx, dy)
        
            
    #help
    def get_image(self):
        file_name = "Shark.png"
        return self.image

    def get_shark_pos(self):
        return self.x_pos, self.y_pos

    
        


