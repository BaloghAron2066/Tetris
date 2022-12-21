#Initializing pygame
import pygame
pygame.init()

#Importing panel for inheritance
from panel import Panel

#The objects of this class are buttons based on the given parameters
class Button (Panel):

    #The constructor takes all the necessary parameters for the creation of a button (he parameter names that are not named clearly are explained in the panel modul)
    def __init__(self, panel, center_left_frac, center_top_frac, width_frac, height_frac, screen,text,textsize,textcolor,backcolor,outlinecolor ):

        #We call the constructor of the superclass
        super().__init__(center_left_frac, center_top_frac, width_frac, height_frac, screen)

        #We calculate the same values as in the panel modul
        self.top = panel.top + int(round((center_top_frac - height_frac / 2) * panel.height))
        self.left = panel.left +  int(round((center_left_frac - width_frac / 2) * panel.width))
        self.bottom = int(round(self.top + (height_frac * panel.height)))
        self.right =  int(round(self.left + (width_frac * panel.width)))
        self.width =  int(round(width_frac * panel.width))
        self.height = int(round(height_frac * panel.height))
        self.text = text
        self.textsize = textsize
        self.textcolor = textcolor
        self.backcolor = backcolor
        self. outlinecolor = outlinecolor


    #This methos displays the button and makes sure that it is changing colors when the user is hovering the mouse on the button
    def show_button(self):
        button_image = pygame.Surface((self.width, self.height))
        button_image.fill(self.backcolor)
        button_rect = pygame.Rect(self.left , self.top ,self.width, self.height)
        self.screen.blit(button_image, button_rect)
        self.show_text(self.left + self.width / 2,self.top + self.height / 2,self.textsize,self.text,self.textcolor)

        #Calling the show_panel function of the superclass (for the borders)
        super().show_panel(self.outlinecolor)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is over the button
                if button_rect.collidepoint(event.pos):
                    return True
            else:
                if button_rect.collidepoint(event.pos):
                    self.backcolor = (255,255,255)
                    self.textcolor = (0,0,0)
                else:
                    self.backcolor = (0,0,0)
                    self.textcolor = (255,255,255)