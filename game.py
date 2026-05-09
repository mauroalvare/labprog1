import pygame
import config

def ejecutar_juego(palabra, generar_pista_func, verificar_func, actualizar_pista_func, calcular_puntaje_func):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption(config.TITULO)

    font = pygame.font.SysFont(config.FUENTE, config.TAMANO_TEXTO)
    font_big = pygame.font.SysFont(config.FUENTE, config.TAMANO_TITULO, bold=True)
    font_small = pygame.font.SysFont(config.FUENTE, 28)

    clock = pygame.time.Clock()

    pista = generar_pista_func(palabra)

    input_text = ""
    running = True
    ganado = False

    inicio = pygame.time.get_ticks()
    tiempo_restante = inicio
    intentos_restantes = config.INTENTOS_MAX

    while running:
        screen.fill(config.COLOR_FONDO)

        # PANEL CENTRAL
        pygame.draw.rect(
            screen,
            (30, 30, 40),
            (50, 50, config.WIDTH - 100, config.HEIGHT - 100),
            border_radius=20
        )

        # TIEMPO
        tiempo_restante = config.TIEMPO_LIMITE - (pygame.time.get_ticks() - inicio) / 1000
        if tiempo_restante <= 0:
            running = False

        # badge tiempo
        pygame.draw.rect(screen, (100, 200, 255), (config.WIDTH - 140, 70, 90, 40), border_radius=10)
        texto_tiempo = font_small.render(str(int(max(0, tiempo_restante))) + "s", True, (0,0,0))
        screen.blit(texto_tiempo, (config.WIDTH - 115, 75))

        # EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Si ingreso texto que no sean espacios y presiono enter
                if len(input_text.strip()) > 0 and event.key == pygame.K_RETURN:
                    # Si acerté la palabra
                    if verificar_func(palabra, input_text):
                        ganado = True
                        running = False
                    # Si no acierta
                    else:
                        intentos_restantes -= 1
                        pista = actualizar_pista_func(pista, palabra)
                        input_text = ""
                        if intentos_restantes <= 0:
                            running = False

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    if event.unicode.isalpha():
                        input_text += event.unicode

        # PISTA
        texto = font_big.render(pista, True, config.COLOR_TEXTO)
        rect = texto.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 - 80))
        screen.blit(texto, rect)

        # INPUT BOX
        pygame.draw.rect(
            screen,
            (50, 50, 70),
            (config.WIDTH//2 - 220, config.HEIGHT//2, 440, 70),
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (100, 200, 255),
            (config.WIDTH//2 - 220, config.HEIGHT//2, 440, 70),
            2,
            border_radius=12
        )

        if input_text == "":
            texto_input = font.render("Escribí la palabra...", True, (120, 120, 120))
        else:
            texto_input = font.render(input_text, True, config.COLOR_INPUT)

        rect_input = texto_input.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 + 35))
        screen.blit(texto_input, rect_input)

        # INTENTOS
        texto_intentos = font_small.render(
            "Intentos: " + str(intentos_restantes),
            True,
            config.COLOR_TEXTO
        )
        screen.blit(texto_intentos, (70, 70))

        # AYUDA
        ayuda = font_small.render(
            "Presioná ENTER para enviar",
            True,
            (150, 150, 150)
        )
        ayuda_rect = ayuda.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 + 100))
        screen.blit(ayuda, ayuda_rect)

        pygame.display.flip()
        clock.tick(60)

    # PANTALLA FINAL
    screen.fill(config.COLOR_FONDO)

    if ganado:
        puntaje = calcular_puntaje_func(tiempo_restante, intentos_restantes)
        texto_puntaje = font.render("Puntaje: " + str(puntaje), True, config.COLOR_TEXTO)
        screen.blit(texto_puntaje, (config.WIDTH // 2 - 100, config.HEIGHT // 2 + 50))
        texto = font_big.render("GANASTE!", True, config.COLOR_EXITO)
        rect = texto.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 - 20))
        screen.blit(texto, rect)
    else:
        texto = font_big.render("PERDISTE!", True, config.COLOR_ERROR)
        rect = texto.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 - 40))
        screen.blit(texto, rect)

        texto_palabra = font.render("La palabra era: " + palabra, True, config.COLOR_TEXTO)
        rect2 = texto_palabra.get_rect(center=(config.WIDTH//2, config.HEIGHT//2 + 30))
        screen.blit(texto_palabra, rect2)

    pygame.display.flip()
    pygame.time.wait(config.TIEMPO_FINAL_MS)

    pygame.quit()