import pygame

pygame.init()

#Atalhos
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()

#Cores
vermelho = (255, 0, 0)
branco = (255, 255, 255)
color = (255, 255, 255)
cinza1 = (100, 100, 100)
cinza2 = (50, 50, 50)
cor_gota = (255, 0, 0)
cor_esfera = (255, 0, 0)
cor_cubo = (255, 0, 0)
cor_ar = (0, 188, 255)
carrega_cx_1 = (50, 50, 50)
carrega_cx_2 = (50, 50, 50)
carrega_cx_3 = (50, 50, 50)

#Booleans
done = False
caiu = False
roda = False
maximo = False

#Posições
chao = 300
y_inicial =0
y_atual = y_inicial
y_atual_2 = y_inicial
x_bloco = 300
x_bloco_2 = 400
carrega_altura_fim = 240
carrega_aceleracao_fim = 240
carrega_massa_fim = 200

#Contadores
contador = 0
contador_2 = 0
velocidade = 0
velocidade_ar = 0
densidade_fluido = 1
constante_x = 0.00
fps = 60
tempo = 0
gravidade = 9.8 / fps
massa = 1000

#Textos
myfont = pygame.font.SysFont('Arial', 15)
myfont_2 = pygame.font.SysFont('Arial', 12)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    while not caiu:
        while not roda:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                chao -= 1
                carrega_altura_fim -= 1
            if pressed[pygame.K_DOWN]:
                chao += 1
                carrega_altura_fim += 1
            if pressed[pygame.K_LEFT]:
                gravidade -= 0.1 / fps
                carrega_aceleracao_fim -= 1
            if pressed[pygame.K_RIGHT]:
                gravidade += 0.1 / fps
                carrega_aceleracao_fim += 1
            if pressed[pygame.K_1]:
                cor_cubo = (255, 0, 0)
                cor_esfera = (255, 0, 0)
                cor_gota = cor_ar
                constante_x = 0.08
                carrega_cx_1 = cor_ar
                carrega_cx_2 = cinza2
                carrega_cx_3 = cinza2
            if pressed[pygame.K_2]:
                cor_esfera = cor_ar
                cor_cubo = (255, 0, 0)
                cor_gota = (255, 0, 0)
                constante_x = 0.47
                carrega_cx_1 = cor_ar
                carrega_cx_2 = cor_ar
                carrega_cx_3 = cinza2
            if pressed[pygame.K_3]:
                cor_cubo = cor_ar
                cor_gota = (255, 0, 0)
                cor_esfera = (255, 0, 0)
                constante_x = 1.05
                carrega_cx_1 = cor_ar
                carrega_cx_2 = cor_ar
                carrega_cx_3 = cor_ar
            if pressed[pygame.K_q]:
                massa -= 25
                carrega_massa_fim -= 1
            if pressed[pygame.K_w]:
                massa += 25
                carrega_massa_fim += 1
            if pressed[pygame.K_SPACE]: roda = True


            screen.fill((0, 0, 0))

            # texto da altura de antes
            textsurface = myfont.render('Altura: ' + str(chao) + ' m', False, (255, 255, 255))
            screen.blit(textsurface, (50, 50))
            textsurface = myfont_2.render('Height', False, (255, 255, 255))
            screen.blit(textsurface, (50, 70))

            # texto da aceleração antes
            textsurface = myfont.render('Aceleração: ' + str(round(gravidade * fps, 4)) + ' m/s²', False,(255, 255, 255))
            screen.blit(textsurface, (50, 100))
            textsurface = myfont_2.render('Acceleration', False,(255, 255, 255))
            screen.blit(textsurface, (50, 120))

            # texto da constante X
            textsurface = myfont.render('Coeficiente de arrasto: ' + str(constante_x), False, (255, 255, 255))
            screen.blit(textsurface, (50, 150))
            textsurface = myfont_2.render('drag coefficient', False, (255, 255, 255))
            screen.blit(textsurface, (50, 170))

            # texto da massa antes
            textsurface = myfont.render('Massa: ' + str(massa) + ' kg', False, (255, 255, 255))
            screen.blit(textsurface, (50, 200))
            textsurface = myfont_2.render('mass', False, (255, 255, 255))
            screen.blit(textsurface, (50, 220))

            # chão
            pygame.draw.rect(screen, color, pygame.Rect(0, chao + 5, 500, 1))
            textsurface = myfont_2.render('@gilberto.rms', False, cor_ar)
            screen.blit(textsurface, (10, chao + 10))

            # botão formato gota
            textsurface = myfont.render('1 - GOTA', False, (cor_gota))
            screen.blit(textsurface, (50, 450))
            textsurface = myfont_2.render('DROP', False, (cor_gota))
            screen.blit(textsurface, (50, 470))

            # botão formato esfera
            textsurface = myfont.render('2 - ESFERA', False, (cor_esfera))
            screen.blit(textsurface, (200, 450))
            textsurface = myfont_2.render('SPHERE', False, (cor_esfera))
            screen.blit(textsurface, (200, 470))

            # botão formato cubo
            textsurface = myfont.render('3 - CUBO', False, (cor_cubo))
            screen.blit(textsurface, (350, 450))
            textsurface = myfont_2.render('CUBE', False, (cor_cubo))
            screen.blit(textsurface, (350, 470))

            # Barra carregamento altura
            pygame.draw.line(screen, cor_ar, (140, 60),(carrega_altura_fim, 60), 7)

            # Barra carregamento aceleracao
            pygame.draw.line(screen, cor_ar, (200, 110), (carrega_aceleracao_fim, 110), 7)

            # Barra carregamento massa
            pygame.draw.line(screen, cor_ar, (165, 210), (carrega_massa_fim, 210), 7)

            # Barra carregamento cx
            pygame.draw.rect(screen, carrega_cx_1, (235, 155, 10, 10), 0)
            pygame.draw.rect(screen, carrega_cx_2, (250, 155, 10, 10), 0)
            pygame.draw.rect(screen, carrega_cx_3, (265, 155, 10, 10), 0)


            pygame.display.flip()
            clock.tick(fps)

        pygame.event.get()


        diferenca_de_distancia = 0

        if y_atual > y_atual_2:
            diferenca_de_distancia = y_atual - y_atual_2
        if y_atual_2 > y_atual:
            diferenca_de_distancia = y_atual_2 - y_atual


        resistencia_ar = 0.5 * densidade_fluido * constante_x * 10 * velocidade * velocidade
        forca_resultante = (massa * gravidade * fps) - resistencia_ar
        aceleracao_final = forca_resultante / massa


        #Com resistencia do ar
        if forca_resultante <= 0:
            if y_atual_2 < chao:
                y_atual_2 += velocidade_ar / fps
                velocidade_ar += 0 / fps
                aceleracao_final = 0
            if y_atual_2 >= chao:
                y_atual_2 == chao
        if forca_resultante > 0:
            if y_atual_2 < chao:
                y_atual_2 += velocidade_ar / fps
                velocidade_ar += aceleracao_final / fps
            if y_atual_2 >= chao:
                y_atual_2 == chao
        if y_atual_2 != chao:
            contador_2 += 1
            tempo_2 = contador_2 / fps

        #Sem resistencia do ar
        if y_atual < chao:
            y_atual += velocidade / fps
            velocidade += gravidade
            contador += 1
            tempo_1 = contador / fps
        if y_atual >= chao:
            y_atual == chao

        if y_atual_2 >= chao and y_atual >= chao: caiu = True

        screen.fill((0, 0, 0))

        #texto do tempo sem resistencia do ar
        textsurface = myfont.render('Tempo: ' + str(round(tempo_1, 2)) + ' s', False, (255, 255, 255))
        screen.blit(textsurface, (50, 10))

        # texto do tempo com resistencia do ar
        textsurface = myfont.render('Tempo: ' + str(round(tempo_2, 2)) + ' s', False, cor_ar)
        screen.blit(textsurface, (50, 100))

        # texto da velocidade sem resistencia do ar
        textsurface = myfont.render('Velocidade: ' + str(int(velocidade)) + ' m/s', False, (255, 255, 255))
        screen.blit(textsurface, (50, 30))

        # texto da velocidade com resistencia do ar
        textsurface = myfont.render('Velocidade: ' + str(int(velocidade_ar)) + ' m/s', False, cor_ar)
        screen.blit(textsurface, (50, 120))
        if forca_resultante <= 0:
            textsurface = myfont.render('MAX', False, cor_ar)
            screen.blit(textsurface, (190, 120))

        # texto da aceleração sem resistencia do ar
        textsurface = myfont.render('Aceleração: ' + str(round(gravidade * fps, 2)) + ' m/s²', False, (255, 255, 255))
        screen.blit(textsurface, (50, 50))

        # texto da aceleração com resistencia do ar
        textsurface = myfont.render('Aceleração: ' + str(round(aceleracao_final, 2)) + ' m/s²', False, cor_ar)
        screen.blit(textsurface, (50, 140))

        #texto da altura sem resistencia do ar
        textsurface = myfont_2.render(str(abs(int(y_atual-chao))) + ' m', False, (255, 255, 255))
        screen.blit(textsurface, (x_bloco, y_atual-20))

        # texto da altura com resistencia do ar
        textsurface = myfont_2.render(str(abs(int(y_atual_2 - chao))) + ' m', False, cor_ar)
        screen.blit(textsurface, (x_bloco_2, y_atual_2 - 20))

        # texto da massa com resistencia do ar
        textsurface = myfont_2.render('Massa: ' + str(massa) + ' kg', False, cor_ar)
        screen.blit(textsurface, (50, 160))

        # texto da diferença de distancia
        textsurface = myfont_2.render('Diferença de distancia: ' + str(round(diferenca_de_distancia, 2)) + ' m', False, vermelho)
        screen.blit(textsurface, (50, 80))

        # linha de diferença de distancia
        pygame.draw.line(screen, vermelho, (350, y_atual), (350, y_atual_2))

        #bloco  sem resistencia do ar
        pygame.draw.rect(screen, color, pygame.Rect(x_bloco, y_atual, 5, 5))

        #bloco com resistencia do ar
        pygame.draw.rect(screen, cor_ar, pygame.Rect(x_bloco_2, y_atual_2, 5, 5))

        #chão
        pygame.draw.rect(screen, color, pygame.Rect(0, chao+5, 500, 1))

        pygame.display.flip()
        clock.tick(fps)

    pygame.display.flip()
