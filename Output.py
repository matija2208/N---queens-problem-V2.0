import pygame
from time import sleep

def inicijalizacija_boja(n):
    colour = []

    red = 255
    green = 0
    blue = 0
    
    if n >= 6:
        g1 = True
        r2 = False
        b1 = False
        g2 = False
        r1 = False
        b2 = False
        
        for i in range(0,n):
            step = 1530 // n

            if g1 == True:
                if green+step <= 255:
                    green += step
                else:
                    g1 = False
                    r2 = True
                    red -= step
            elif r2 == True:
                if red - step >= 0:
                    red -= step
                else:
                    r2 = False
                    b1 = True
                    blue += step
            elif b1 == True:
                if blue+step <= 255:
                    blue += step
                else:
                    b1 = False
                    g2 = True
                    green -= step
            elif g2 == True:
                if green - step >= 0:
                    green -= step
                else:
                    g2 = False
                    r1 = True
                    red += step
            elif r1 == True:
                if red+step <= 255:
                    red += step
                else:
                    r1 = False
                    b2 = True
                    blue -= step
            elif b2 == True:
                if blue - step >= 0:
                    blue -= step
                else:
                    b2 = False
                    g1 = True
                    green += step
            colour.append((red, green, blue))
    else:
        for i in range(0, n):
            step = 255 // n
            colour.append((255 - (step * i), 0, step * i))

    return colour

def ispis(tabla, n, window):
    colour = inicijalizacija_boja(n)
    counter = 0
    duzina, visina = pygame.display.get_surface().get_size()
    duzina_stranice = visina // n
    border = visina - duzina_stranice * n

    for h in range(n):
        for w in range(n):
            if tabla[h][w] == 1:
                pygame.draw.rect(window, colour[h], (w * duzina_stranice + (border // 2), h * duzina_stranice + (border // 2), duzina_stranice, duzina_stranice))
                counter+=1
            else:
                if (w % 2 == 0 and h % 2 == 1)or(w % 2 == 1 and h % 2 == 0):
                    pygame.draw.rect(window, (0,0,0), (w * duzina_stranice, h * duzina_stranice, duzina_stranice, duzina_stranice))
                else:
                    pygame.draw.rect(window, (255,255,255), (w * duzina_stranice, h * duzina_stranice, duzina_stranice, duzina_stranice))

    font = pygame.font.SysFont("couriernew", visina // 20)
    if counter < n:
        tekst = font.render("STATUS : TRAZENJE RESENJA", False, (238, 238, 119))
    else:
        tekst = font.render("STATUS : NADJENO RESENJE", False, (0, 204, 85))
    
    pygame.draw.rect(window, (0, 0, 0), (visina + border, 0, abs(duzina - visina), visina // 20 +10))
    pygame.draw.lines(window, (119, 119, 119), True, [(visina + border, 0), (visina + border, visina // 20 + 10), (duzina, visina // 20 + 10), (duzina, 0)], 10)
    window.blit(tekst, (visina + 10, 10))
    pygame.display.update()
    vreme_kasnjenja = 1 / (n ** 2)
    sleep(vreme_kasnjenja)

def nije_moguce(window, n):
    duzina, visina = pygame.display.get_surface().get_size()
    duzina_stranice = visina // n
    border = visina - duzina_stranice * n

    font = pygame.font.SysFont("couriernew", visina // 20)
    tekst = font.render("STATUS : NEMA RESENJA", False, (136, 0, 0))
    pygame.draw.rect(window, (0, 0, 0), (visina + border, 0, abs(duzina - visina), visina // 20 +10))
    pygame.draw.lines(window, (119, 119, 119), True, [(visina + border, 0), (visina + border, visina // 20 + 10), (duzina, visina // 20 + 10), (duzina, 0)], 10)
    window.blit(tekst, (visina + 10, 10))
    pygame.display.update()