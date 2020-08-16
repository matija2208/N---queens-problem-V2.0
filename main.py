import pygame
import Output
import GUI
import Algoritam

def main():
    pygame.init()
    pygame.display.set_caption("N - queens problem")
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    n = GUI.inicijalizacija(window)
    if n == None:
        return False
    tabla = [[0 for x in range(n)] for y in range(n)]
    R_broj_kraljice = 0
    R_broj_kombinacije = [0]*n
    tabla = Algoritam.trazenje_mogucih_pozicija(tabla, R_broj_kraljice, R_broj_kombinacije, n, window)

    if tabla == None:
        Output.nije_moguce(window, n)

    GUI.dugme(window, n)

main()