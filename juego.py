import pygame 
import sys 
from teclado_mouse import *

def gatito(contador,dire):
    hoja = pygame.image.load('Imagenes/sprites/gatito.png')
    
    
    quieto = {0: (437, 0, 50, 100), 
              1: (487, 0, 50, 100), 
              2: (537, 0, 50, 100), 
              3: (487, 0, 50, 100)}

    caminar = {0: (888, 0, 100, 100), 
               1: (988, 0, 100, 100),  
               2: (1088, 0, 100, 100),
               3: (1188, 0, 100, 100),
               4: (1288, 0, 100, 100),
               5: (1388, 0, 100, 100),
               6: (1488, 0, 100, 100)}
    
    if dire == "QUIETO":
        if contador > len(quieto)-1:
            contador = contador % len(quieto)
        hoja.set_clip(pygame.Rect(quieto[contador]))

    if dire == "RIGHT":
        if contador > len(caminar)-1:
            contador = contador % len(caminar)
        hoja.set_clip(pygame.Rect(caminar[contador]))

    imagen = hoja.subsurface(hoja.get_clip())
    rect = imagen.get_rect()
    
    return imagen
        





def juego(ventana_info):
    clock = pygame.time.Clock()
    en_juego = True
    print ("en juego")
    contador = 0
    pos_x = 400
    while en_juego:
        pygame.init()
        ventana = pygame.display.set_mode((ventana_info["ancho"],ventana_info["alto"]),pygame.RESIZABLE)
        pygame.display.set_caption(ventana_info["titulo"]) 
        fondo = pygame.image.load("imagenes/fondo_slice.png")
        ventana.blit(fondo, (0,720-1500))

        tecla = comando()
        direccion = "QUIETO"
        if tecla == "ESC":
            en_juego = False
        if tecla == "RIGHT":
            direccion = "RIGHT"
            pos_x += 5
        if tecla == "LEFT":
            direccion = "RIGHT"
            pos_x -= 5
        
        
        ventana.blit(gatito(contador,direccion),(pos_x,400))

        contador += 1
        pygame.display.update()
        #clock.tick(20)

    