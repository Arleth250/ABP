import flet as ft
import pygame
import os
from mutagen.mp3 import MP3

async def main(page: ft.Page ):
    page.title = "Reproductor de Musica"
    page.bgcolor="black"
    page.height= 20
    page.width= 20
    page.