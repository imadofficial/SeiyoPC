import pygame
import json

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
Intro = True
MainMenu = False

Config = json.load(open('Assets/SeiyoMeta.json'))
pygame.display.set_caption(f'SeiyoPC | v{Config["CurrentVersion"]} (Build {Config["CurrentBuild"]})')

font = pygame.font.Font('Assets/SeiyoDefault.ttf', 32)
InstructiesNL = font.render('Druk op een knop om te starten.', True, (255, 255, 255))
InstructiesFR = font.render('Appuyez sur un bouton pour démarrer.', True, (255, 255, 255))
InstructiesEN = font.render('Press a button to start.', True, (255, 255, 255))

textRectNL = InstructiesNL.get_rect()
textRectNL.center = (1280 // 2, 480)

textRectFR = InstructiesFR.get_rect()
textRectFR.center = (1280 // 2, 720 // 2)

textRectEN = InstructiesEN.get_rect()
textRectEN.center = (1280 // 2, 250)

while Intro:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Intro = False

    screen.fill("black")

    # RENDER YOUR GAME HERE
    screen.blit(InstructiesNL, textRectNL)
    screen.blit(InstructiesFR, textRectFR)
    screen.blit(InstructiesEN, textRectEN)

    pygame.display.flip()

    clock.tick(60)

while MainMenu:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # RENDER YOUR GAME HERE

    pygame.display.flip()

    clock.tick(60)
    pygame.display.update()


pygame.quit()