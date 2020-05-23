import pygame
from teclado_mouse import *

def intro(ventana_info):
    en_intro = True
    a = 0
    while en_intro == True:
        pygame.init()
        ventana = pygame.display.set_mode((ventana_info["ancho"],ventana_info["alto"]),pygame.RESIZABLE)
        pygame.display.set_caption(ventana_info["titulo"]) 
        
        fondo = pygame.image.load("imagenes/fondo_1080x720.png")
        ventana.blit(fondo, (0,0))
        press = pygame.image.load("imagenes/pressspace_1080x720.png")
        press = press.convert()
         
        if a <= 50:
            subiendo = True
        if a >= 320:
            subiendo = False        
        if subiendo:
            a += 30
        else:
            a -= 30
        press.set_alpha(a)
        ventana.blit(press, (0,0))


        tecla = comando()
        if tecla == "SPACE":
            en_intro = False
        pygame.display.update()
