import pygame 
from teclado_mouse import *

def menu(ventana_info):
    while True:
        pygame.init()
        ventana = pygame.display.set_mode((ventana_info["ancho"],ventana_info["alto"]))
        pygame.display.set_caption(ventana_info["titulo"]) 
        ventana.fill(ventana_info["color_fondo"])
        
        fondo = pygame.image.load("imagenes/fondo_1080x720.png")
        ventana.blit(fondo, (0,0))

        opciones = [
            pygame.image.load("imagenes/opcion_1.png"),
            pygame.image.load("imagenes/opcion_2.png"),
            pygame.image.load("imagenes/exit.png")]
        flecha = pygame.image.load("imagenes/flechita.png")

        if "opcion" in locals():                ## para poner la flecha en 0 por defecto
            pass
        else:
            opcion = 0                          ## // 
        cant_op = 0
        op_pos = [90,300]

        tecla = comando()
        if tecla == "DOWN":                 ## si se apreta la flecha abajo
            opcion = opcion + 1
            if opcion == len(opciones):
                opcion = 0
        if tecla == "UP":
            opcion = opcion - 1
            if opcion < 0:
                opcion = len(opciones)-1
        if tecla == "SPACE" or tecla == "ENTER":
            if opcion == len(opciones)-1:
                pygame.quit()
                sys.exit()
            if opcion == 0:
                print ("ejecuta opcion 1")
            if opcion == 1:
                print ("ejecutar opcion 2")
        
        ventana.blit(flecha, (op_pos[0] - 40 , op_pos[1]+ 50*opcion))

        for op in opciones:
            ventana.blit(op, (90,op_pos[1]+ 50*cant_op))
            cant_op = cant_op + 1

        pygame.display.update()



