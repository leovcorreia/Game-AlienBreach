import pygame
import sys
from button \
    import Button

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pygame.display.set_caption("Play")

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def help():
    pygame.display.set_caption("Help")

    while True:
        HELP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        HELP_TEXT = get_font(45).render("This is the HELP screen.", True, "Black")
        HELP_RECT = HELP_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(HELP_TEXT, HELP_RECT)

        HELP_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")

        HELP_BACK.changeColor(HELP_MOUSE_POS)
        HELP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(HELP_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def about():
    pygame.display.set_caption("About")

    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("white")

        ABOUT_TEXT1 = get_font(20).render("EQUIPE:", True, "Black")
        ABOUT_RECT1 = ABOUT_TEXT1.get_rect(center=(640, 75))
        SCREEN.blit(ABOUT_TEXT1, ABOUT_RECT1)
        ABOUT_TEXT2 = get_font(20).render("Gustavo Giozeppe Bulgarelli RA129658", True, "Black")
        ABOUT_RECT2 = ABOUT_TEXT2.get_rect(center=(640, 150))
        SCREEN.blit(ABOUT_TEXT2, ABOUT_RECT2)
        ABOUT_TEXT3 = get_font(20).render("Leonardo Venâncio Correia RA129266", True, "Black")
        ABOUT_RECT3 = ABOUT_TEXT3.get_rect(center=(640, 225))
        SCREEN.blit(ABOUT_TEXT3, ABOUT_RECT3)
        ABOUT_TEXT4 = get_font(20).render("Disciplina de Sistemas Distribuídos", True, "Black")
        ABOUT_RECT4 = ABOUT_TEXT4.get_rect(center=(640, 300))
        SCREEN.blit(ABOUT_TEXT4, ABOUT_RECT4)
        ABOUT_TEXT5 = get_font(20).render("Curso de Ciência da Computação", True, "Black")
        ABOUT_RECT5 = ABOUT_TEXT5.get_rect(center=(640, 375))
        SCREEN.blit(ABOUT_TEXT5, ABOUT_RECT5)
        ABOUT_TEXT6 = get_font(20).render("Departamento de Informática - Centro de Tecnologia", True, "Black")
        ABOUT_RECT6 = ABOUT_TEXT6.get_rect(center=(640, 450))
        SCREEN.blit(ABOUT_TEXT6, ABOUT_RECT6)
        ABOUT_TEXT7 = get_font(20).render("Universidade Estadual de Maringá", True, "Black")
        ABOUT_RECT7 = ABOUT_TEXT7.get_rect(center=(640, 525))
        SCREEN.blit(ABOUT_TEXT7, ABOUT_RECT7)

        ABOUT_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")

        ABOUT_BACK.changeColor(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")
    play_image = pygame.image.load("assets/Play Rect.png")
    help_image = pygame.image.load("assets/help Rect.png")
    about_image = pygame.image.load("assets/About Rect.png")
    quit_image = pygame.image.load("assets/Quit Rect.png")

    scaled_play = pygame.transform.scale(play_image, (
                    int(play_image.get_width() * (.7)),
                    int(play_image.get_height() * (.7))
                ))
    scaled_help = pygame.transform.scale(help_image, (
                    int(help_image.get_width() * (.7)),
                    int(help_image.get_height() * (.7))
                ))
    scaled_about = pygame.transform.scale(about_image, (
                    int(about_image.get_width() * (.7)),
                    int(about_image.get_height() * (.7))
                ))
    scaled_quit = pygame.transform.scale(quit_image, (
                    int(quit_image.get_width() * (.7)),
                    int(quit_image.get_height() * (.7))
                ))

    while True:
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "#b68f40") # change color as needed
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=scaled_play, pos=(640, 250), 
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        HELP_BUTTON = Button(image=scaled_help, pos=(640, 350), 
                             text_input="HELP", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=scaled_about, pos=(640, 450), 
                              text_input="ABOUT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=scaled_quit, pos=(640, 550), 
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HELP_BUTTON, ABOUT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    pygame.init()

    SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("assets/Background.png")


    main_menu()
