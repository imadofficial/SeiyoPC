import pygame
from pygame import mixer
import tkinter as Tk
from tkinter import messagebox
import json, math

Timer = pygame.time.Clock()

pygame.init()

Score = 0
Combo = 0
screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)

# "Class" pour la configuration des clés
class CleDeClavier():
    def __init__(self,x,y,couleur1,couleur2,cle):
        self.x = x
        self.y = y
        self.couleur1 = couleur1
        self.couleur2 = couleur2
        self.cle = cle
        self.rect = pygame.Rect(self.x,self.y,100,20)
        self.handled = False

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #Initializer le sprite
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

Cles = [
    CleDeClavier(420,650,(169,169,169), (255,255,255), pygame.K_d),
    CleDeClavier(530,650,(169,169,169), (255,255,255), pygame.K_f),
    CleDeClavier(640,650,(169,169,169), (255,255,255), pygame.K_j),
    CleDeClavier(750,650,(169,169,169), (255,255,255), pygame.K_k),
]

def load():
    mixer.init()
    rects = []

    f = open("./ChartData/Chart.txt", 'r')
    data = f.readlines()
    
    mixer.music.load('./ChartData/Song.mp3')
    mixer.music.play()
        
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rect = pygame.Rect(Cles[x].rect.x,y * -150,100,20)
                rects.append(rect)
    
    return rects

rects = load()

#region TextRendering
BigFont = pygame.font.Font('Assets/SeiyoDefault.ttf', 28)
SmolFont = pygame.font.Font('Assets/SeiyoDefault.ttf', 24)

SongName = BigFont.render('Distorted Fate', True, (255, 255, 255))
Artist = SmolFont.render('Sakuzyo', True, (255, 255, 255))

Difficulty = BigFont.render('Insane 14.8', True, (255, 255, 255))
Scorecount = BigFont.render('0000000', True, (255, 255, 255))
ComboCount = SmolFont.render('Combo 0', True, (255, 255, 255))

SongRect = SongName.get_rect()
SongRect = (50, 640)

DifficultyRect = Difficulty.get_rect()
DifficultyRect = (1100, 655)

ArtistRect = Artist.get_rect()
ArtistRect = (50, 670)

ScoreRect = Scorecount.get_rect()
ScoreRect.center = (100, 40)

ComboRect = ComboCount.get_rect()
ComboRect.center = (87, 65)
#endregion

image = pygame.image.load('./ChartData/Background.png')

#region
Pointsperhit = 0

Config = json.load(open('Config.json'))
pygame.display.set_caption(f'SeiyoPC v{Config["CurrentVersion"]} <{Config["Edition"]} | Metal Compatible>')

with open('./ChartData/Chart.txt', 'r') as file:
    content = file.read()

count = content.count('0')
Pointsperhit = int(1000000/count)

Config = json.load(open('./ChartData/ChartConfig.json'))
SongName = BigFont.render(f'{Config["Name"]}', True, (255, 255, 255))
Artist = SmolFont.render(f'{Config["Artist"]}', True, (255, 255, 255))
Difficulty = BigFont.render(f'{Config["Difficulty"]}', True, (255, 255, 255))
#endregion

while True:
    screen.fill((0,0,0))
    screen.blit(image, (0, 0))

    screen.blit(SongName, SongRect)
    screen.blit(Difficulty, DifficultyRect)
    screen.blit(Artist, ArtistRect)
    screen.blit(Scorecount, ScoreRect)
    screen.blit(ComboCount, ComboRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    k = pygame.key.get_pressed()

    for note in Cles:
        if(k[note.cle]):
            pygame.draw.rect(screen, note.couleur1, note.rect)
            note.handled = False
        else:
            pygame.draw.rect(screen, note.couleur2, note.rect)
            note.handled = True

    for rect in rects:
        pygame.draw.rect(screen,(200,0,0), rect)
        rect.y += 20
    
        for key in Cles:
            if(key.rect.colliderect(rect)and not key.handled):
                rects.remove(rect)
                key.handled = True
                Score += Pointsperhit
                Combo += 1
                Scorecount = BigFont.render(f'{Score}', True, (255, 255, 255))
                ComboCount = SmolFont.render(f'Combo {Combo}', True, (255, 255, 255))
                break
    

    pygame.display.update()
    pygame.display.flip()
    Timer.tick(60)