import pygame
import audio

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("./song.mp3")
    pygame.mixer.music.play()
