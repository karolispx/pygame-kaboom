#!/usr/bin/env python

import os
import sys
import random
import pygame

# Import custom classes
from config import Config
from obstacle import Obstacle
from player import Player


# Initialize config
config = Config()

# Center pygame window in center of the screen when started
os.environ["SDL_VIDEO_CENTERED"] = "True"

# Initialize pygame and setup WINDOW
pygame.init()
WINDOW = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.WINDOW_CAPTION)


# Display text
def displayText(textSize, message, color, topOffset):
    font = pygame.font.Font('assets/fonts/segoe-ui-symbol/seguisym.ttf', textSize)
    text = font.render(message, True, color)
    WINDOW.blit(text, text.get_rect(center=(config.WINDOW_WIDTH / 2, topOffset)))


# Create obstacles
def createObstacles(number):
    while number > 0:
        config.OBSTACLES.append(Obstacle(config))
        number -= 1


# Initialize pygame audio mixer
pygame.mixer.init(22050, -16, 2, 4096)

# Play audio
def playAudio(name):
    if name == 'gameplay' or name == 'gameover' or name == 'theme':
        pygame.mixer.music.pause()

        pygame.mixer.music.set_volume(config.AUDIO_VOLUME)
        pygame.mixer.music.load("assets/audio/" + name + ".ogg")

        if name == 'gameover':
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
        elif name == 'gameplay': 
            pygame.mixer.music.play(-1)
        else: 
            pygame.mixer.music.play(-1)

# Start playing theme audio before game loops begins
playAudio('theme')


# Initialize player
player = Player(config)

# Initialize a few obstacles
createObstacles(config.MAX_OBSTACLES)


# Game loop
while config.GAME_RUNNING:
    # Set up background color and the ticker/timer
    WINDOW.fill(config.WINDOW_BACKGROUND)
    pygame.time.delay(config.GAME_TICKER)


    # Capture events
    for event in pygame.event.get():
        # Exit out of game loop because pressed on X/quit
        if event.type == pygame.QUIT: 
            config.GAME_RUNNING = False 

        # If this event is fired that means 'gameover' audio has finished playing
        if event.type == pygame.USEREVENT: 
            # Start playing theme audio
            playAudio('theme')


    # Get keys being pressed
    keys = pygame.key.get_pressed()


    # Game over
    if config.GAME_OVER == True:
        # Show game over screen
        WINDOW.blit(pygame.image.load("assets/images/game-over-screen.jpg"), (0, 0))

        displayText(120, "☹", config.HEADING_COLOR, (config.WINDOW_HEIGHT - 290))
        displayText(80, "GAME OVER!", config.HEADING_COLOR, (config.WINDOW_HEIGHT - 170))
        displayText(50, "★ Score: " + str(config.SCORE) + "     ♔ Level: " + str(config.LEVEL) + "/5", config.TEXT_COLOR, (config.WINDOW_HEIGHT - 70))

        # When game over - press space to restart
        if keys[pygame.K_SPACE]: 
            # Start playing gameplay audio if game is restarted
            playAudio('gameplay')

            # Reset player position
            player.resetPlayerPosition()
            
            # Restart the game
            config.resetDefaultValues()

            # Initialize a few obstacles
            createObstacles(config.MAX_OBSTACLES)

    # Game not started
    elif config.GAME_STARTED == False and config.GAME_OVER == False:
        # Show welcome screen
        WINDOW.blit(pygame.image.load("assets/images/welcome-screen.jpg"), (0, 0))

        # When game not started - press space to start
        if keys[pygame.K_SPACE]: 
            # Start playing gameplay audio if game is started
            playAudio('gameplay')

            # Start the game
            config.GAME_STARTED = True

    # Gameplay
    else: 
        # Show gameplay background
        WINDOW.blit(pygame.image.load("assets/images/game-screen.jpg"), (0, 0))

        # Calculate game difficulty based on score/level
        player.adjustDifficulty()
        
        # Render obstacles
        for obstacle in config.OBSTACLES:
            if obstacle.control():
                pygame.draw.circle(WINDOW, obstacle.color, [obstacle.positionX, obstacle.positionY], obstacle.radius)

        # Render player
        player.control(pygame, keys)
        pygame.draw.circle(WINDOW, player.color, [player.positionX, player.positionY], player.radius)

        # Display score
        displayText(24, "★ Score: " + str(config.SCORE) + "          ♔ LEVEL: " + str(config.LEVEL) + "/5", config.TEXT_COLOR, (config.WINDOW_HEIGHT - 24))

        # Detect Collisions
        if player.detectCollisions():
            # Start playing gameover
            playAudio('gameover')

            # Set the game to ve over
            config.GAME_OVER = True

 
    # Update screen
    pygame.display.update() 


# Quit the game if outside of the game loop
pygame.quit()

sys.exit()










