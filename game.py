#Initializing pygame
import pygame
pygame.init()

#Storing necessary information about the display in a variable (current_h, current_w)
info = pygame.display.Info()

#importing all the classes and methods that we need to run the game
from datetime import datetime
from interface import Grid
from interface import NextPanel
from interface import LevelPanel
from interface import ScorePanel
from objects import Tetromino
from objects import Border
from objects import Fix_blocks


#An object of this class is a tetris game and it can be started with a method
class Game:

    #In the constructor we set all the necessary parameters
    def __init__(self):

        #We set the screen to fullscreen
        self.screen = pygame.display.set_mode((info.current_w, info.current_h))

        #Allocating the panels
        self.grid = Grid(0.5,0.5,0.4,0.8,self.screen)
        self.nextpanel = NextPanel(0.8,0.17,0.15,0.15,self.screen)
        self.levelpanel = LevelPanel(0.8,0.3,0.15,0.05,self.screen)
        self.scorepanel = ScorePanel(0.8,0.38,0.15,0.05,self.screen)

        #Creating 2 tetrominos (current and next)
        self.T_curr = Tetromino()
        self.T_next = Tetromino()

        #Creating the object that stores the fix blocks
        self.fix_blocks = Fix_blocks()

        #Declaring start time
        self.start = datetime.now()
        
        #Creating border object
        self.border = Border()

        #A counter for tetrominos (for speed acceleration)
        self.T_counter = 1

        #A base value for speed (1 second)
        self.speed = 1

        #Setting level to 1
        self.level = 1

        #setting score to 1
        self.score = 0
        
    #This method starts the game
    def Start(self):
        
        #We store a start time for every key that can be pressed continuously
        d_start = datetime.now()
        r_start = datetime.now()
        l_start = datetime.now()

        # Running the game loop
        running = True
        while running:

            # Handling events
            for event in pygame.event.get():

                #The loop stops if the user closes the window
                if event.type == pygame.QUIT:
                    running = False

                #The loop stops if the user presses the ESCAPE button
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    #movements
                    elif event.key == pygame.K_LEFT:
                        self.T_curr.move_left(self.fix_blocks,self.border)
                        k_left_start = datetime.now()
                    elif event.key == pygame.K_RIGHT:
                        self.T_curr.move_right(self.fix_blocks,self.border)
                        k_right_start = datetime.now()
                    elif event.key == pygame.K_DOWN:
                        k_down_start = datetime.now()
                        self.T_curr.move_down()
                    elif event.key == pygame.K_SPACE:
                        self.T_curr.move_down_fixate(self.fix_blocks)
                    
                    #rotation
                    if event.key == pygame.K_UP:
                        self.T_curr.rotate(self.fix_blocks,self.border)
            
            #Continouos movements
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] :
                down = True
                now = datetime.now()
                if (now -k_down_start).total_seconds() > 0.3:
                    if (now - d_start).total_seconds() > 0.1:
                        d_start = datetime.now()
                        self.T_curr.move_down()
            else:
                down = False
            if keys[pygame.K_LEFT]:
                now = datetime.now()
                if (now - k_left_start).total_seconds() > 0.3:
                    if (now - l_start).total_seconds() > 0.1:
                        l_start = datetime.now()
                        self.T_curr.move_left(self.fix_blocks,self.border)
            if keys[pygame.K_RIGHT]:
                now = datetime.now()
                if (now -k_right_start).total_seconds() > 0.3:
                    if (now - r_start).total_seconds() > 0.1:
                        r_start = datetime.now()
                        self.T_curr.move_right(self.fix_blocks,self.border)
           
           #We move the current tetromino down for every tick
            now = datetime.now()
            if (now - self.start).total_seconds() > self.speed and down == False:
                self.start = datetime.now()
                self.T_curr.move_down()
                
            #We check if the current tetromino needs to be fixed
            if self.fix_blocks.check_tetromino(self.T_curr):

                #If yes we fix it
                score_current = self.fix_blocks.add_tetromino(self.T_curr)

                #We add the correct amount to the score
                if score_current == 1:
                    self.score += 40
                elif score_current == 2:
                    self.score += 100
                elif score_current == 3:
                    self.score += 300
                elif score_current == 4:
                    self.score += 1200

                #Check if the games is lost
                for i in self.T_curr.blocks:
                    if i[1]>=19:

                        #If the game is lost the method returns false
                        del self
                        return False

                #We create a new next tetromino and set the current to the previous next
                self.T_curr,self.T_next = self.T_next, Tetromino()

                #Escalating the speed
                self.T_counter += 1
                if self.T_counter == 10:
                    self.speed *= 0.9
                    self.T_counter = 0
                    self.level += 1
            
            #Displaying everything that needs to be displayed
            self.T_curr.draw_tetromino(self.grid)
            self.fix_blocks.draw_blocks(self.grid)
            self.nextpanel.display_tetromino(self.T_next,self.grid.unit)
            pygame.display.update()
            self.grid.screen.fill((0, 0, 0))
            self.nextpanel.show_panel()
            self.levelpanel.show_panel(self.level)
            self.scorepanel.show_panel(self.score)
            self.grid.show_panel()
    
    
        # Quit Pygame
        pygame.quit()





