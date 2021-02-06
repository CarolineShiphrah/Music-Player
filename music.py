import pygame
import json

def Play(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def Reset():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def Pause():
    pygame.mixer.music.pause()

def Unpause():
    pygame.mixer.music.unpause()

def Exit():
    pygame.mixer.stop()
    exit()

def adjust_volume(volume):
    max_volume = volume / 10
    pygame.mixer.music.set_volume(max_volume)

def music_settings():
    settings_read = open("configure.json", 'r')
    read = json.loads(settings_read.read())
    return read

def append_new_settings(new_settings):
    settings = open("configure.json", 'w')
    settings.truncate(0)
    settings.write(json.dumps(new_settings))
