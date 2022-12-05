# OHJELMAN INIT
import pygame
from random import randrange
pygame.init()
naytto = pygame.display.set_mode((640, 480))
peli_kaynnissa = False

# MAIN PELI
def pelaa(peli_kaynnissa: bool, hpnyt: int, nopeusnyt: float, hnopeusnyt: float, level: int):
    def anna_koordinaatit():
        return (randrange(0, 640 - robo.get_width()), randrange(0, 480 - robo.get_height()))

    taso = level
    # HAHMOT
    robo = pygame.image.load("robo.png")
    hirvio = pygame.image.load("hirvio.png")

    # IRTAIMISTO
    kolikko = pygame.image.load("kolikko.png")
    pisteet = 0

    #FONTIT
    fontti = pygame.font.SysFont("Arial", 24)
    fontti2 = pygame.font.SysFont("Arial", 12)
    
    # HAHMOJEN OMINAISUUDET
    hp = hpnyt
    nopeus = nopeusnyt
    hirvio_nopeus = hnopeusnyt

    # ALKUSIJOITUKSET
    x = 0
    y = 480-robo.get_height()
    x_hirvio = 640 - hirvio.get_width()
    y_hirvio = 0 + hirvio.get_height()
    x_kolikko, y_kolikko = anna_koordinaatit()

    # LIIKKUMISKÄSKYJEN INIT
    oikealle = False
    vasemmalle = False
    ylos = False
    alas = False

    # TAHDITUKSEN INIT
    kello = pygame.time.Clock()

    
    # PELISILMUKKA
    while peli_kaynnissa:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    alas = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    alas = False

            if tapahtuma.type == pygame.QUIT:
                exit()

        # ROBON LIIKKUMINEN
        if oikealle and x + robo.get_width() <= 640:
            x += nopeus
        if vasemmalle and x > 0:
            x -= nopeus
        if ylos and y > 0:
            y -= nopeus
        if alas and y + robo.get_height() <= 480:
            y += nopeus
        # HIRVIÖ SEURAA
        if x_hirvio > x:
            x_hirvio -= hirvio_nopeus
        if x_hirvio < x:
            x_hirvio += hirvio_nopeus
        if y_hirvio > y:
            y_hirvio -= hirvio_nopeus
        if y_hirvio < y:
            y_hirvio += hirvio_nopeus

        # HIRVIÖ TEKEE DAMAGEA
        if (x_hirvio + hirvio.get_width() >= x + 10 and x_hirvio + 10 < x + hirvio.get_width()) and (y_hirvio + hirvio.get_height() > y + 10 and y_hirvio + 10 < y + hirvio.get_height()):
            hp -= 1
            if hp <= 0:
                peli_kaynnissa = False
                gameover(taso)

        # KOLIKKOJEN KERUU
        if (x_kolikko + kolikko.get_width() >= x and x_kolikko < x + robo.get_width()) and (y_kolikko + kolikko.get_height() > y and y_kolikko < y + robo.get_height()):
            pisteet += 1
            if pisteet >= 10:
                peli_kaynnissa = False
                levelup(peli_kaynnissa, hp, nopeus, hirvio_nopeus, taso)
            x_kolikko, y_kolikko = anna_koordinaatit()


        hpteksti = fontti.render(f"HP:", True, (255, 0, 0))
        hpjaljella = fontti2.render(f"{int(hp /  10) * '+'}", True, (255, 0, 0))
        pisteteksti = fontti.render(f"Pisteet: {pisteet} / 10", True, (255, 0, 0))
        tasoteksti = fontti.render(f"Taso: {taso}", True, (255, 0, 0))
        # DISPLAY
        naytto.fill((50, 50, 50))

        naytto.blit(robo, (x, y))
        naytto.blit(hirvio, (x_hirvio, y_hirvio))

        naytto.blit(kolikko, (x_kolikko, y_kolikko))

        naytto.blit(pisteteksti, (640 - pisteteksti.get_width(), 0))
        naytto.blit(tasoteksti, (320 - pisteteksti.get_width() / 2, 0))
        naytto.blit(hpteksti, (0, 0))
        naytto.blit(hpjaljella, (0 + hpteksti.get_width(), 0 + (hpteksti.get_height() / 2) - hpjaljella.get_height() / 2))
        pygame.display.flip()

        #TAHDITUS
        kello.tick(60)

#LEVEL UP
def levelup(peli_kaynnissa: bool, hpnyt: int, nopeusnyt: float, hnopeusnyt: float, level: int):
    peli_kaynnissa = peli_kaynnissa
    hp = hpnyt
    nopeus = nopeusnyt
    hirvio_nopeus = hnopeusnyt
    taso = level

    fontti = pygame.font.SysFont("Arial", 16)
    teksti1 = fontti.render(f"Läpäisit tason!", True, (255, 255, 255))
    teksti2 = fontti.render(f"Täytätkö HP:si vai kehitätkö nopeutta?", True, (255, 255, 255))
    kehitahp = fontti.render(f"HP", True, (255, 0, 0))
    kehitanop = fontti.render(f"NOPEUS", True, (0, 255, 0))

    naytto.fill((50, 50, 50))
    naytto.blit(teksti1, (320 - teksti1.get_width() / 2, 0))
    naytto.blit(teksti2, (320 - teksti2.get_width() / 2, teksti1.get_height()))
    naytto.blit(kehitahp, (0 + 20, 320))
    naytto.blit(kehitanop, (640 - 20 - kehitanop.get_width(), 320))
    pygame.display.flip()

    while peli_kaynnissa == False:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x_hiiri = tapahtuma.pos[0]
                y_hiiri = tapahtuma.pos[1]

                if (x_hiiri > 20 and x_hiiri < 20 + kehitahp.get_width()) and (y_hiiri > 320 and y_hiiri < 320 + kehitahp.get_height()):
                    peli_kaynnissa = True
                    taso += 1
                    hirvio_nopeus += 0.5
                    hp = 100
                    pelaa(peli_kaynnissa, hp, nopeus, hirvio_nopeus, taso)

                if (x_hiiri > 640 - 20 - kehitanop.get_width() and x_hiiri < 640 - 20) and (y_hiiri > 320 and y_hiiri < 320 + kehitanop.get_height()):
                    peli_kaynnissa = True
                    taso += 1
                    hirvio_nopeus += 0.5
                    nopeus += 1
                    pelaa(peli_kaynnissa, hp, nopeus, hirvio_nopeus, taso)

            if tapahtuma.type == pygame.QUIT:
                exit()

# ALKURUUTU
def intro():
    peli_kaynnissa = False
    while peli_kaynnissa == False:
        fontti = pygame.font.SysFont("Arial", 24)
        teksti = fontti.render(f"Kolikkojahti", True, (255, 0, 0))
        teksti2 = fontti.render(f"Pelaa", True, (255, 0, 0))
        pygame.draw.rect(naytto, (50, 0, 0), (320 - teksti.get_width() / 2, 240 - teksti.get_height() /  2 + teksti.get_height(), teksti.get_width(), teksti.get_height()))
        naytto.blit(teksti, (320 - teksti.get_width() / 2, 240 - teksti.get_height() /  2))
        naytto.blit(teksti2, (320 - teksti2.get_width() / 2, 240 - teksti.get_height() /  2 + teksti.get_height()))
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x_hiiri = tapahtuma.pos[0]
                y_hiiri = tapahtuma.pos[1]

                # KÄYNNISTÄÄ PELIN ALKUARVOILLA
                if (x_hiiri > 320 - teksti.get_width() / 2 and x_hiiri < 320 - teksti.get_width() / 2 + teksti.get_width()) and (y_hiiri > 240 - teksti.get_height() /  2 + teksti.get_height() and y_hiiri < 240 - teksti.get_height() /  2 + teksti.get_height() + teksti.get_height()):
                    peli_kaynnissa = True
                    pelaa(peli_kaynnissa, 100, 2, 1, 1)
            if tapahtuma.type == pygame.QUIT:
                    exit()
        pygame.display.flip()

# HÄVIÖ
def gameover(taso):
    peli_kaynnissa = False
    while peli_kaynnissa == False:
        fontti = pygame.font.SysFont("Arial", 24)
        teksti = fontti.render(f"Kuolit, pääsit tasolle {taso}", True, (255, 0, 0))
        teksti2 = fontti.render(f"Pelaa uudestaan", True, (255, 0, 0))
        pygame.draw.rect(naytto, (50, 0, 0), (320 - teksti2.get_width() / 2, 240 - teksti2.get_height() /  2 + teksti2.get_height(), teksti2.get_width(), teksti2.get_height()))
        naytto.blit(teksti, (320 - teksti.get_width() / 2, 240 - teksti.get_height() /  2))
        naytto.blit(teksti2, (320 - teksti2.get_width() / 2, 240 - teksti.get_height() /  2 + teksti.get_height()))
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x_hiiri = tapahtuma.pos[0]
                y_hiiri = tapahtuma.pos[1]

                if (x_hiiri > 320 - teksti2.get_width() / 2 and x_hiiri < 320 - teksti2.get_width() / 2 + teksti2.get_width()) and (y_hiiri > 240 - teksti2.get_height() /  2 + teksti2.get_height() and y_hiiri < 240 - teksti2.get_height() /  2 + teksti2.get_height() + teksti2.get_height()):
                    peli_kaynnissa = True
                    pelaa(peli_kaynnissa, 100, 2, 1, 1)
            if tapahtuma.type == pygame.QUIT:
                    exit()
        pygame.display.flip()

# PELIN ALOITUS
intro()