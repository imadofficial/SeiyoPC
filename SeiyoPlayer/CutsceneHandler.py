import pygame
from pygame import mixer
import tkinter as Tk
from tkinter import messagebox
import json, math, moviepy.editor, os
from pyvidplayer import Video

CutScreneInProgress = True

screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption(f'SeiyoPC <Cutscene Mode>')


try:
    vid = Video("./ChartData/Cutscene.mp4")
    vid.set_size((1280, 720))

    while CutScreneInProgress:
        vid.draw(screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    os.system('Main.py')
                    pygame.quit()
                    
except FileNotFoundError:
    os.system('Main.py')
    os.system('exit')
    pygame.quit()