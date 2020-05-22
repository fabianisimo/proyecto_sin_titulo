import pygame 
from teclado_mouse import *


class menu(pygame.sprite.Sprite):
    def __init__(self,ventana_info,datos={"opcion": 0, "en_menu": True}):
        pygame.sprite.Sprite.__init__(self)
        self.ventana = pygame.display.set_mode((ventana_info["ancho"],ventana_info["alto"]))
        pygame.display.set_caption(ventana_info["titulo"]) 
        self.ventana.fill(ventana_info["color_fondo"])

        self.fondo = pygame.image.load("imagenes/fondo_1080x720.png")
        self.ventana.blit(self.fondo, (0,0))

        self.opciones = [
            pygame.image.load("imagenes/opcion_1.png"),
            pygame.image.load("imagenes/opcion_2.png"),
            pygame.image.load("imagenes/exit.png")
            ]
        self.poscion_opcion = [90,300]
        self.opcion = datos["opcion"] 
        self.en_menu = datos["en_menu"]
        self.flecha = pygame.image.load("imagenes/flechita.png")

        self.tecla = comando()

        ## ejecucion desde ahora
    
        self.__listar_opciones()
        self.__cursor()
        pygame.display.update()

        recursividad = {"opcion": self.opcion, "en_menu": self.en_menu}
        if datos["en_menu"]:
            menu(ventana_info,recursividad)
        else:
            self.resultado()   
        
    
    def __listar_opciones(self):
        nuemro_opcion = 0
        for op in self.opciones:
            self.ventana.blit(op, (self.poscion_opcion[0],self.poscion_opcion[1]+ 50*nuemro_opcion))
            nuemro_opcion = nuemro_opcion + 1

    def __cursor(self):
        if self.tecla == "DOWN":
            self.opcion += 1
            if self.opcion == len(self.opciones):
                self.opcion = 0
        if self.tecla == "UP":
            self.opcion -= 1
            if self.opcion < 0:
                self.opcion = len(self.opciones)-1  

        if self.tecla == "ENTER" or self.tecla == "SPACE":
            if self.opcion == 2:
                pygame.quit()
                sys.exit()
            if self.opcion == 0:
                self.en_menu = False

        self.ventana.blit(self.flecha, (self.poscion_opcion[0]-50, self.poscion_opcion[1]+ 50*self.opcion))   

    def resultado(self):
        print ("ocpion  1 elegido")
        rerere = "a"
        return rerere  
        print (rerere)     

    
        

        
''' 

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
                fadeout = True
            if opcion == 1:
                print ("ejecutar opcion 2")
        
        ventana.blit(flecha, (op_pos[0] - 40 , op_pos[1]+ 50*opcion))

        for op in opciones:
            ventana.blit(op, (90,op_pos[1]+ 50*cant_op))
            cant_op = cant_op + 1

        if "fadeout_alfa" in locals():
            pass
        else:
            fadeout_alfa = 0
        if "fadeout" in locals():
            if fadeout:
                ventana.fill((0,0,0,fadeout_alfa))
                #ventana.set_alpha(fadeout_alfa)
                fadeout_alfa = fadeout_alfa +1 

        
        pygame.display.update()

 '''

