
import pygame
from menu import *
import sys

ventana_info = {
    "ancho":  1080,
    "alto":   720,
    "titulo": "titulo del juego",
    "color_fondo": (10,10,10) ## casi negro
}

Game_over = False

cuentavuelta = 0
while Game_over == False:
    if "menu_bucle" in locals():
        cuentavuelta += 1
        print (cuentavuelta)
        menu_bucle = menu(ventana_info,opcion)
    else: 
        menu_bucle = menu(ventana_info)
        opcion = menu.resultado(ventana_info)
        print (cuentavuelta, menu_bucle)

