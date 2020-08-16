import pygame as pe

def crtaj(window):
    duzina_prozora, visina_prozora = pe.display.get_surface().get_size()
    window.fill((0, 0, 0))
    velicina_fonta = int(visina_prozora * 0.0625)
    font = pe.font.SysFont("couriernew", velicina_fonta) 
    tekst1 = font.render("Problem N kraljica", True, (0, 0, 170))
    tekst2 = font.render("Unesite broj n :", True, (0, 204, 85))
    x_1 = int(duzina_prozora - (velicina_fonta * 9)) // 2
    y_1 = int(visina_prozora * 0.1)
    x_2 = int(duzina_prozora - (velicina_fonta * 8)) // 2
    y_2 = int(visina_prozora * 0.25)
    window.blit(tekst1, (x_1, y_1))
    window.blit(tekst2, (x_2, y_2))

    x_pravougaonika = int((duzina_prozora * 0.3) / 2)
    y_pravougaonika = int((visina_prozora * 0.375))
    stranica_a = int(duzina_prozora * 0.7)
    stranica_b = int(visina_prozora * 0.1)
    pe.draw.rect(window, (136, 0, 0), (x_pravougaonika, y_pravougaonika, stranica_a, stranica_b))

    A_1 = (0, int(visina_prozora * 0.6))
    B_1 = (0, visina_prozora)
    C_1 = (int(duzina_prozora * 0.4), visina_prozora)
    pe.draw.polygon(window, (221, 136, 85), [A_1, B_1, C_1])
    A_2 = (duzina_prozora, int(visina_prozora * 0.6))
    B_2 = (duzina_prozora, visina_prozora)
    C_2 = (int(duzina_prozora * 0.6), visina_prozora)
    pe.draw.polygon(window, (221, 136, 85), [A_2, B_2, C_2])

    pe.draw.rect(window, (0, 136, 255), (int(duzina_prozora * 0.3), int(visina_prozora * 0.5), int(duzina_prozora * 0.4), int(visina_prozora * 0.2)))
    dugme = font.render("UNESI", True, (170, 255, 102))
    window.blit(dugme, (int(int(duzina_prozora * 0.3) + (int(duzina_prozora * 0.4) - (5 * (velicina_fonta / 2)))/2), int(visina_prozora * 0.6 - velicina_fonta / 2)))

    x = duzina_prozora - 100
    y = visina_prozora - 100
    font = pe.font.SysFont("couriernew", 80)
    tekst = font.render("X", False, (136, 0, 0))
    pe.draw.circle(window,(170, 255, 102), (x, y), 50)
    window.blit(tekst, (x - 22, y - 40))

def dodatak(N, window):
    duzina_prozora, visina_prozora = pe.display.get_surface().get_size()
    n = 0
    mnozilac = 10
    for i in range(0, len(N)):
        n *= mnozilac
        n += N[i]
            
    x_pravougaonika = int((duzina_prozora * 0.3) / 2)
    y_pravougaonika = int((visina_prozora * 0.375))
    stranica_a = int(duzina_prozora * 0.7)
    stranica_b = int(visina_prozora * 0.1)
    pe.draw.rect(window, (136, 0, 0), (x_pravougaonika, y_pravougaonika, stranica_a, stranica_b))

    velicina_fonta = int(visina_prozora * 0.0625)
    font = pe.font.SysFont("couriernew", velicina_fonta) 
    tekst = font.render(str(n), True, (0, 255, 131))
    x = int(x_pravougaonika + ((stranica_a - (len(str(n)) / 2)) / 2))
    y = int(y_pravougaonika + ((stranica_b - velicina_fonta) / 2))
    window.blit(tekst, (x, y))
    
def brisanje(N, window):
        N.pop()
        dodatak(N, window)

def obrada(N, window):
    duzina_prozora, visina_prozora = pe.display.get_surface().get_size()
    x = duzina_prozora - 100
    y = visina_prozora - 100
    test = True
    while test:
        for event in pe.event.get():
            if event.type == pe.KEYDOWN:
                key = event.key
                if key != pe.K_RETURN:
                    if key != pe.K_BACKSPACE and key != pe.K_DELETE:
                        if int(key) >= 48 and int(key) <= 57:
                            N.append(int(key - 48))
                            dodatak(N, window)
                        elif int(key) >= 256 and int(key) <= 265:
                            N.append(int(key - 256))
                            dodatak(N, window)
                    elif len(N) > 0:
                        brisanje(N, window)
                    
                    pe.display.update()
                
                else:
                    test = False
                    break

            elif event.type == pe.MOUSEMOTION:
                kordinate = event.pos
                if (kordinate[0] >= int(duzina_prozora * 0.3) and kordinate[0] <= int(duzina_prozora * 0.7)) and (kordinate[1] >= int(visina_prozora * 0.5) and kordinate[1] <= int(visina_prozora * 0.7)):
                    pe.draw.rect(window, (0, 136, 255), (int(duzina_prozora * 0.29), int(visina_prozora * 0.49), int(duzina_prozora * 0.42), int(visina_prozora * 0.22)))
                    velicina_fonta = int(visina_prozora * 0.0850)
                    font = pe.font.SysFont("couriernew", velicina_fonta) 
                    dugme = font.render("UNESI", True, (170, 255, 102))
                    window.blit(dugme, (int(int(duzina_prozora * 0.29) + (int(duzina_prozora * 0.42) - (5 * (velicina_fonta / 2)))/2), int(visina_prozora * 0.49 + (visina_prozora * 0.22 - (velicina_fonta)) / 2)))
                    pe.display.update()
                else:
                    pe.draw.rect(window, (0, 0, 0), (int(duzina_prozora * 0.29), int(visina_prozora * 0.49), int(duzina_prozora * 0.42), int(visina_prozora * 0.22)))
                    velicina_fonta = int(visina_prozora * 0.0625)
                    font = pe.font.SysFont("couriernew", velicina_fonta)
                    pe.draw.rect(window, (0, 136, 255), (int(duzina_prozora * 0.3), int(visina_prozora * 0.5), int(duzina_prozora * 0.4), int(visina_prozora * 0.2)))
                    dugme = font.render("UNESI", True, (170, 255, 102))
                    window.blit(dugme, (int(int(duzina_prozora * 0.3) + (int(duzina_prozora * 0.4) - (5 * (velicina_fonta / 2)))/2), int(visina_prozora * 0.6 - velicina_fonta / 2)))
                    pe.display.update()

                if (kordinate[0] >= x - 50 and kordinate[0] <= x + 50) and (kordinate[1] >= y - 50 and kordinate[1] <= y + 50):
                    font = pe.font.SysFont("couriernew", 120)
                    tekst = font.render("X", False, (136, 0, 0))
                    pe.draw.circle(window,(170, 255, 102), (x, y), 70)
                    window.blit(tekst, (x - 35, y - 60))
                    pe.display.update()
                else:
                    font = pe.font.SysFont("couriernew", 80)
                    tekst = font.render("X", False, (136, 0, 0))
                    pe.draw.circle(window,(221, 136, 85), (x, y), 120)
                    pe.draw.circle(window,(170, 255, 102), (x, y), 50)
                    window.blit(tekst, (x - 22, y - 40))
                    pe.display.update()

            elif event.type == pe.MOUSEBUTTONUP:
                kordinate = event.pos
                if (kordinate[0] >= int(duzina_prozora * 0.29) and kordinate[0] <= int(duzina_prozora * 0.71)) and (kordinate[1] >= int(visina_prozora * 0.49) and kordinate[1] <= int(visina_prozora * 0.71)):
                    test = False
                    break
                if (kordinate[0] >= x - 70 and kordinate[0] <= x + 70) and (kordinate[1] >= y - 70 and kordinate[1] <= y + 70):
                    return 0
            elif event.type == pe.QUIT:
                pe.quit()
                return 0

    return N

def inicijalizacija(window):
    n = 0

    window.fill((0, 0, 0))

    crtaj(window)
    pe.display.update()
    N = obrada([], window)
    if N == 0:
        return None
    mnozilac = 10
    for i in range(0, len(N)):
        n *= mnozilac
        n +=N [i]
    
    window.fill((0, 0, 0))
    pe.display.update()
    return int(n)

def dugme(window, n):
    duzina_prozora, visina_prozora = pe.display.get_surface().get_size()
    x = duzina_prozora - 100
    y = visina_prozora - 100

    font = pe.font.SysFont("couriernew", 80)
    tekst = font.render("X", False, (136, 0, 0))
    pe.draw.circle(window,(170, 255, 102), (x, y), 50)
    window.blit(tekst, (x - 22, y - 40))
    pe.display.update()

    loop = True
    while loop == True:
        for event in pe.event.get():
            if event.type == pe.MOUSEMOTION:
                kordinate = event.pos
                if (kordinate[0] >= x - 50 and kordinate[0] <= x + 50) and (kordinate[1] >= y - 50 and kordinate[1] <= y + 50):
                    font = pe.font.SysFont("couriernew", 120)
                    tekst = font.render("X", False, (136, 0, 0))
                    pe.draw.circle(window,(170, 255, 102), (x, y), 70)
                    window.blit(tekst, (x - 35, y - 60))
                    pe.display.update()
                else:
                    font = pe.font.SysFont("couriernew", 80)
                    tekst = font.render("X", False, (136, 0, 0))
                    pe.draw.circle(window,(0, 0, 0), (x, y), 120)
                    pe.draw.circle(window,(170, 255, 102), (x, y), 50)
                    window.blit(tekst, (x - 22, y - 40))
                    pe.display.update()

            elif event.type == pe.MOUSEBUTTONUP:
                kordinate = event.pos
                if (kordinate[0] >= x - 70 and kordinate[0] <= x + 70) and (kordinate[1] >= y - 70 and kordinate[1] <= y + 70):
                    return None