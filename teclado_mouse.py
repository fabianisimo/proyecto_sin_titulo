import pygame 
import sys

def comando():
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                  
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                return "SPACE"
            if evento.key == pygame.K_w:
                return "W"
            if evento.key == pygame.K_LEFT:
                return "LEFT"
            if evento.key == pygame.K_RIGHT:
                return "RIGHT"
            if evento.key == pygame.K_UP:
                return "UP"
            if evento.key == pygame.K_DOWN:
                return "DOWN"
            if evento.key == pygame.K_RETURN:
                return "ENTER"
