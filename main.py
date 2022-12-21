#Initializing pygame
import pygame
pygame.init()

#Storing necessary information about the display in a variable (current_h, current_w)
info = pygame.display.Info()

#importing all the classes and methods that we need to run the game
from game import Game
from interface import GameOverPanel
from interface import StartPanel

#We set the screen to fullscreen
screen = pygame.display.set_mode((info.current_w, info.current_h))

#Creating and displaying start panel
start = StartPanel(screen)
running = start.show_panel()

# Load the music file
pygame.mixer.music.load("TetrisMusic.mp3")

# Play the music
pygame.mixer.music.play()

#Running a loop that starts new games until the program is stopped (with ESCAPE or exit)
while running:
    for event in pygame.event.get():

        #The loop stops if the user exits the game
        if event.type == pygame.QUIT:
            running = False

        #The loop stops if the user presses the ESCAPE button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Creating and starting a new game
    game_curr = Game()
    if game_curr.Start() == False:

        #Storing score
        score = game_curr.score

        #Deleting current game
        del game_curr

        screen.fill(( 0,0,0))

        #New game over panel
        gameover = GameOverPanel(0.5,0.5,0.35,0.4,screen)
        if gameover.show_panel(score):
            del gameover

            #Creating new game
            game_curr = Game()
        
# Quit Pygame
pygame.quit()

