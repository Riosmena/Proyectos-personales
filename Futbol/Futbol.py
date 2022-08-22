import pygame
import time
fin=3
pygame.init()
#Colores---------------------
Rojo=(255,0,0)
Azul=(0,0,255)
Negro=(0,0,0)
Gris=(200,200,200)
Blanco=(255,255,255)
Naranja=(250,167,21)
#Ventana---------------------
tam=(1000,700)
screen=pygame.display.set_mode(tam)
pygame.display.set_caption("Fútbol")
fuente1=pygame.font.SysFont("Kristen ITC",80)
fuente2=pygame.font.SysFont("Showcard Gothic",100)
fondo=pygame.image.load("campo.png").convert()
puntos1=0
puntos2=0
#Frames----------------------
tiempo=pygame.time.Clock()
#Configuración del juego-----
#Jugadores///////////////////
largo=60
ancho=20
#Jugador1********************
p11x=350
p11y=380
p11v=0
#Jugador2********************
p12x=130
p12y=380
p12v=0
#Jugador3********************
p21x=650
p21y=380
p21v=0
#Jugador4********************
p22x=870
p22y=380
p22v=0
#Pelota//////////////////////
px=500
py=400
pvx=5
pvy=3
#Principal///////////////////
gg=False
while not gg:
    puntuacion1=fuente1.render(str(puntos1),True,Blanco)
    puntuacion2=fuente1.render(str(puntos2),True,Blanco)
    gameover=fuente2.render("¡Fin del juego!",True,Naranja)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gg=True
        #Teclado|||||||||||||
        if event.type==pygame.KEYDOWN:
            #Jugador1****
            if event.key==pygame.K_w:
                p11v=-3
            if event.key==pygame.K_s:
                p11v=3
            #Jugador2****
            if event.key==pygame.K_q:
                p12v=-3
            if event.key==pygame.K_a:
                p12v=3
            #Jugador3****
            if event.key==pygame.K_i:
                p21v=-3
            if event.key==pygame.K_k:
                p21v=3
            #Jugador4****
            if event.key==pygame.K_o:
                p22v=-3
            if event.key==pygame.K_l:
                p22v=3
        if event.type==pygame.KEYUP:
            #Jugador1****
            if event.key==pygame.K_w:
                p11v=0
            if event.key==pygame.K_s:
                p11v=0
            #Jugador2****
            if event.key==pygame.K_q:
                p12v=0
            if event.key==pygame.K_a:
                p12v=0
            #Jugador3****
            if event.key==pygame.K_i:
                p21v=0
            if event.key==pygame.K_k:
                p21v=0
            #Jugador4****
            if event.key==pygame.K_o:
                p22v=0
            if event.key==pygame.K_l:
                p22v=0
    #Límites/////////////////
    #Jugador1****************
    if p11y<100:
        p11y=101
    if p11y>630:
        p11y=629
    #Jugador2****************
    if p12y<100:
        p12y=101
    if p12y>630:
        p12y=629
    #Jugador3****************
    if p21y<100:
        p21y=101
    if p21y>630:
        p21y=629
    #Jugador4****************
    if p22y<100:
        p22y=101
    if p22y>630:
        p22y=629
    #Pelota******************
    if py>690 or py<100:
        pvy*=-1 
    #Movimiento//////////////
    p11y+=p11v
    p12y+=p12v
    p21y+=p21v
    p22y+=p22v
    px+=pvx
    py+=pvy
    #Anotacion---------------
    if px>1010:
        puntos1=puntos1+1
        px=500
        py=400
        pvx*=-1
        pvy*=-1
    if px<-10:
        puntos2=puntos2+1
        px=500
        py=400
        pvx*=-1
        pvy*=-1
    #Zona de trabajo---------
    screen.blit(fondo,[0,0])
    #Marcador----------------
    screen.blit(puntuacion1,(350,0))
    screen.blit(puntuacion2,(620,0))
    #Personajes--------------
    jugador1=pygame.draw.rect(screen,Rojo,(p11x,p11y,ancho,largo))
    jugador2=pygame.draw.rect(screen,Rojo,(p12x,p12y,ancho,largo))
    jugador3=pygame.draw.rect(screen,Azul,(p21x,p21y,ancho,largo))
    jugador4=pygame.draw.rect(screen,Azul,(p22x,p22y,ancho,largo))
    #Pelota------------------
    pelota=pygame.draw.circle(screen,Gris,(px,py),10)
    #Limite horizontal-------
    lim1=pygame.draw.line(screen,Negro,(0,0),(0,305))
    lim11=pygame.draw.line(screen,Negro,(0,307),(56,307))
    lim2=pygame.draw.line(screen,Negro,(0,480),(0,700))
    lim22=pygame.draw.line(screen,Negro,(0,479),(56,479))
    lim3=pygame.draw.line(screen,Negro,(999,0),(999,312))
    lim33=pygame.draw.line(screen,Negro,(943,313),(999,313))
    lim4=pygame.draw.line(screen,Negro,(999,485),(999,700))
    lim44=pygame.draw.line(screen,Negro,(943,484),(999,484))
    #Game Over---------------
    if puntos1>10 or puntos2>10:
        screen.blit(gameover,(150,400))
        gg=True
    #Colisiones--------------
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2) or pelota.colliderect(jugador3) or pelota.colliderect(jugador4):
        pvx*=-1
    if pelota.colliderect(lim1) or pelota.colliderect(lim2) or pelota.colliderect(lim3) or pelota.colliderect(lim4):
        pvx*=-1
    if pelota.colliderect(lim11) or pelota.colliderect(lim22) or pelota.colliderect(lim33) or pelota.colliderect(lim44):
        pvy*=-1
    #Actualizar--------------
    pygame.display.flip()
    tiempo.tick(80)
time.sleep(fin)
pygame.quit()
