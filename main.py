
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


while Game_over == False:
    if menu(ventana_info) == "a":
        print ("salio del menu")


