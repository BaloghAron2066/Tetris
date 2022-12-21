#Initializing pygame
import pygame 
pygame.init()

#Importing panel for inheritance
from panel import Panel
#Importing button to create buttons on the UI
from button import Button

#Declaring the size of a block (as a fraction of the height of the grid)
unit = 0.05

#An object of this class is a 10*20 grid 
class Grid (Panel):

    #The constructor asks for the necessary parameters (same as the panel class)
    def __init__(self,center_left_frac,center_top_frac,width_frac,height_frac,screen):
        super().__init__(center_left_frac,center_top_frac,width_frac,height_frac,screen)

        #This variable stores the size of a block as pixels
        self.unit = int(round(unit * self.height))

        #We calculate the right and bottom border of the grid based on the unit variable (this was the blocks are always squares)
        self.right = self.left + self.unit * 10
        self.bottom = self.top + self.unit * 20
        
    #A method for displaying the grid (in white)
    def show_panel(self):
        for i in range(11):
            pygame.draw.line(self.screen, (255,255,255), (self.unit*i+self.left, self.top), (self.unit*i+self.left, self.bottom), 1)
        for i in range(21):
            pygame.draw.line(self.screen, (255,255,255), (self.left, self.unit*i+self.top), (self.right, self.unit*i+self.top), 1)

    #A method for displaying a block based on coordinates
    def create_block(self,xpos,ypos,color):
        ypos = (-ypos+19)#Converting coordinates 
        rect=pygame.Rect(self.left+self.unit*xpos+1,self.top+self.unit*ypos+1,self.unit-2,self.unit-2)
        pygame.draw.rect(self.screen, color, rect)
    
#An object of this class is a panel that displays the next tetromino
class NextPanel (Panel):

    #The constructor takes the same input as the panel class
    def __init__(self,center_left_frac,center_top_frac,width_frac,height_frac,screen):
        super().__init__(center_left_frac,center_top_frac,width_frac,height_frac,screen)

        #We declare a separator, that separates the text from the tetromino
        self.separator_top = self.top + int(round(self.height * 0.7))

    #A method for displaying the panel
    def show_panel(self):
        super().show_panel()
        pygame.draw.line(self.screen, (255,255,255), (self.left, self.separator_top), (self.right,self.separator_top), 1)
        self.show_text(self.left + self.width / 2, self.separator_top + self.height * 0.15,30,"NEXT",(255,255,255))
        

    #A method for displaying the tetromino
    def display_tetromino(self,T,unit):

        #We store the height of the subpanel in which we display the tetromino
        subpanel_height = self.separator_top - self.top

        #Displaying the square tetromino
        if T.ttype == 1:
            for i in T.blocks:
                rect=pygame.Rect(self.left + int(round(self.width/2)) - 1 * unit + unit * (i[0] - 4) ,self.top + int(round(subpanel_height/2)) - 1 * unit + unit * (i[1] - 20),unit-2,unit-2)
                pygame.draw.rect(self.screen, T.color, rect)

        #Displaying the long tetromino
        if T.ttype == 2:
            for i in T.blocks:
                rect=pygame.Rect(self.left + int(round(self.width/2)) - 2 * unit + unit * (i[0] - 3) ,self.top + int(round(subpanel_height/2)) - int(round(0.5 * unit)) + unit * (i[1] - 20),unit-2,unit-2)
                pygame.draw.rect(self.screen, T.color, rect)

        #Displaying the other tetrominos
        l = [3,4,5,6,7]
        if T.ttype in l:
            for i in T.blocks:
                rect=pygame.Rect(self.left + int(round(self.width/2)) - int(round(1.5 * unit)) + unit * (i[0] - 3) ,self.top + int(round(subpanel_height/2)) - unit * (i[1] - 20),unit-2,unit-2)
                pygame.draw.rect(self.screen, T.color, rect)
        
#A class for the panel that displays the current level
class LevelPanel (Panel):
    def show_panel(self, level):
        super().show_panel()
        self.show_text(self.left + self.width / 2, self.top + self.height / 2,30,"LEVEL: " + str(level),(255,255,255))

#A class for the panel that displays the current score
class ScorePanel (Panel):
    def show_panel(self, score):
        super().show_panel()
        self.show_text(self.left + self.width / 2, self.top + self.height / 2,30,"SCORE: " + str(score),(255,255,255))

#An object of this class is a game over panel
class GameOverPanel (Panel):

    def show_panel(self, final_score):

        #We create a play again button 
        B = Button(self, 0.5, 0.75, 0.6, 0.2, self.screen,"PLAY AGAIN", 60, (255,255,255), (0,0,0), (255,255,255))

        #A loop for displaying the button
        running = True
        while running:
            for event in pygame.event.get():

                #The loop ends if the user closes the window
                if event.type == pygame.QUIT:
                    running = False

                #The loop ends if the user presses the ESCAPE button
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            #We display the panel borders
            super().show_panel()

            #We display the final score
            self.show_text(self.left + self.width/2,self.top + self.height/2,60,"Score: " + str(final_score),(255, 255, 255))
            
            #We display the game over text
            self.show_text(self.left + self.width/2,self.top + self.height/4,100,"GAME OVER",(255, 0, 0))

            #If the user clicks the play again button the method returns true
            if B.show_button():
                return True

            # Update the screen
            pygame.display.update()

        # Quit Pygame
        pygame.quit()

#An object of this class is a start panel
class StartPanel (Panel):

    #We declare the position of the start button
    def __init__(self, screen):
        self.center_left_frac = 0.5
        self.center_top_frac = 0.5
        self.width_frac = 0.2
        self.height_frac = 0.05
        super().__init__(self.center_left_frac, self.center_top_frac, self.width_frac, self.height_frac, screen)

    #We display the panel
    def show_panel(self):

        #We create a start button 
        B = Button(self, 0.5, 0.5, 1, 1, self.screen,"START", 60, (255,255,255), (0,0,0), (255,255,255))

        #A loop for displaying the button
        running = True
        while running:
            for event in pygame.event.get():

                #The loop ends if the user closes the window
                if event.type == pygame.QUIT:
                    running = False

                #The loop ends if the user presses the ESCAPE button
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    
            #We display the panel borders
            super().show_panel()

            #If the user clicks the play again button the method returns true
            if B.show_button():
                return True

            # Update the screen
            pygame.display.update()

        # Quit Pygame
        pygame.quit()
