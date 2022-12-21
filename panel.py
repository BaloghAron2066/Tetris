#Initializing pygame
import pygame
pygame.init()

#Storing necessary information about the display in a variable (current_h, current_w)
info = pygame.display.Info()

#Creating the panel class
#This class will be used as a superclass for classes in the interface module
class Panel:
    
    #The constructor needs 5 parameters
    #center_left_frac = the distance between the center of the panel and the left side of the screen as a fraction
    #center_top_frac = the distance between the center of the panel and the top side of the screen as a fraction
    #width_frac = the width of the panel as a fraction of the width of the screen
    #height_frac = the height of the panel as a fraction of the height of the screen
    #screen = the screen we will display the panel on
    def __init__(self,center_left_frac,center_top_frac,width_frac,height_frac,screen):

        #Some variables we will need
        self.top = int(round((center_top_frac - height_frac / 2) * info.current_h)) #The distance between the top side of the screen and the top side of the panel in pixels
        self.left = int(round((center_left_frac - width_frac / 2) * info.current_w)) #The distance between the left side of the screen and the left side of the panel in pixels
        self.bottom = int(round(self.top + (height_frac * info.current_h))) #The distance between the bottom side of the screen and the bottom side of the panel in pixels
        self.right = int(round(self.left + (width_frac * info.current_w))) #The distance between the right side of the screen and the right side of the panel in pixels
        self.width = int(round(width_frac * info.current_w)) #The width of the panel in pixels
        self.height = int(round(height_frac * info.current_h)) #The height of the panel in pixels
        self.screen = screen

    #This method will display the borders of the panel
    def show_panel(self,color: tuple = (255,255,255)):
        pygame.draw.line(self.screen, color, (self.left, self.top), (self.right, self.top), 1)
        pygame.draw.line(self.screen, color, (self.left, self.bottom), (self.right, self.bottom), 1)
        pygame.draw.line(self.screen, color, (self.right, self.top), (self.right, self.bottom), 1)
        pygame.draw.line(self.screen, color, (self.left, self.top), (self.left, self.bottom), 1)
    
    #This method will display a given text with the given parameters
    def show_text(self,center_left,center_top,font_size,text,color):
        font = pygame.font.Font(None, font_size) 
        text_image = font.render(text, True, color)
        text_rect = text_image.get_rect()
        text_rect.center = (center_left, center_top)
        self.screen.blit(text_image, text_rect)



        
