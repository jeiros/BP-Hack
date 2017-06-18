import pygame
import audio

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("./winsong.mp3")
    pygame.mixer.music.play()


if __name__ == '__main__':
    play_music()