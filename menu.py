import pygame 
from teclado_mouse import *
        
menus = {
    "flecha" : pygame.image.load("imagenes/flechita.png"),
    "menu_inicial" : [
            pygame.image.load("imagenes/opcion_1.png"),
            pygame.image.load("imagenes/opcion_2.png"),
            pygame.image.load("imagenes/exit.png")
            ],
    "menu_dos" : [
            pygame.image.load("imagenes/opcion_1.png"),
            pygame.image.load("imagenes/opcion_2.png"),
            pygame.image.load("imagenes/exit.png")
            ]
}

def printar_menu(ventana,menu,posicion_arbol):  ## posicion arbol parte en 0
    posicion_base = [90,300]
    lista_opciones = menu
    contador_printar = 0
    for opcion in lista_opciones:
        en_x = posicion_base[0] + posicion_arbol*350 
        en_y = posicion_base[1] + contador_printar*50
        ventana.blit(opcion, (en_x,en_y))
        contador_printar += 1

def pritnar_flecha(ventana,menu,posicion_arbol,arribaabajo):
    posicion_base = [90,300]
    listado_opciones = menu
    opcion_seleccionada = arribaabajo
    if opcion_seleccionada >= len(menu):
        opcion_seleccionada = opcion_seleccionada % len(menu)  
    if opcion_seleccionada < 0:
        opcion_seleccionada = len(menu)-1 - (((opcion_seleccionada*-1)+len(menu)-1) % len(menu))
    en_x = posicion_base[0] - 40 + 350*posicion_arbol
    en_y = posicion_base[1] + opcion_seleccionada*50
    #print ("len menu: ",len(menu)," opcion: ",opcion_seleccionada, "  en_x: ",en_x, "  en_y: ", en_y)
    ventana.blit(menus["flecha"], (en_x,en_y))
    return (opcion_seleccionada)

def pantalla_a_negro(ventana):
    for a in range(255):
        ventana.fill((0,0,0,a))


def menu(ventana_info):
    posicion_flecha = 0
    opcion_1 = False
    a = 0
    apagandose = False
    while True:
        pygame.init()
        ventana = pygame.display.set_mode((ventana_info["ancho"],ventana_info["alto"]))
        pygame.display.set_caption(ventana_info["titulo"]) 
        
        fondo = pygame.image.load("imagenes/fondo_1080x720.png")
        ventana.blit(fondo, (0,0))
        printar_menu(ventana,menus["menu_inicial"],0)

        tecla = comando()
        if tecla == "UP":
            posicion_flecha -= 1
        if tecla == "DOWN":
            posicion_flecha += 1

        if opcion_1 == False:
            opcion_seleccionada  = pritnar_flecha(ventana,menus["menu_inicial"],0,posicion_flecha)
            if tecla == "ENTER":
                if opcion_seleccionada == 2:
                    apagandose = True
                if opcion_seleccionada == 1:
                    opcion_1 = True
                    menu_0 = False
        
        if opcion_1:
            printar_menu(ventana,menus["menu_dos"],1)
            opcion_seleccionada_1 = pritnar_flecha(ventana,menus["menu_dos"],1,posicion_flecha-opcion_seleccionada)
            if tecla == "ENTER":
                if opcion_seleccionada_1 == 2:
                    opcion_1 = False
        
        if apagandose:
            fade = pygame.image.load("imagenes/fondo_fade.png")
            fade = fade.convert()
            fade.set_alpha(a)
            ventana.blit(fade, (0,0))
            a += 10
            if a == 350:
                exit()

        pygame.display.update()

