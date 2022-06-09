import pygame
import pygame_menu

from main import main

# Initialize pygame
pygame.init()

screenWidth, screenHeight = 1280, 1024
surface = pygame.display.set_mode((screenWidth, screenHeight))


# Make Selection Menu

# Zero = Spaceship("zero")
# Falcon = Spaceship("falcon")

# ListSpaceship = [Zero, Falcon]

selectMenuTheme = pygame_menu.themes.THEME_DARK.copy()
selectMenuTheme.background_color = pygame_menu.BaseImage(
    'assets/images/space_bg.png')
selectMenuTheme.title_background_color = (0, 0, 0, 25)
selectMenuTheme.title_font = pygame_menu.font.FONT_DIGITAL
selectMenuTheme.title_offset = (screenWidth/2.75, 0)
selectMenuTheme.widget_font = pygame_menu.font.FONT_DIGITAL
selectMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE

selectMenu = pygame_menu.Menu(
    'Select a spaceship', screenWidth, screenHeight, theme=selectMenuTheme)
selectMenu.add.label("Choose a character")
# TODO Selector qui fait changer l'image en fonction du personnage choisi
# selectMenu.add.selector("Choose a character", items=ListSpaceship)


# Make Instructions Menu
instructMenuTheme = pygame_menu.themes.THEME_DARK.copy()
instructMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
instructMenuTheme.title_background_color = (0, 0, 0, 25)
instructMenuTheme.title_offset = (screenWidth/2.75, 0)
instructMenuTheme.title_font = pygame_menu.font.FONT_DIGITAL
instructMenuTheme.background_color = (17, 26, 43)
instructMenuTheme.widget_font = pygame_menu.font.FONT_DIGITAL
instructMenuTheme.widget_font_size = 15


instructMenu = pygame_menu.Menu(
    'Instructions', screenWidth, screenHeight, theme=instructMenuTheme)
instructMenu.add.label("Voici les règles pour pouvoir jouer au jeu \n")
instructMenu.add.label(
    "Pour le joueur 1: \n Les déplacement se font avec les touches Z,Q,S,D et le joystick gauche de la manette \n On tire en utilisant la touche Ctrl ou le bouton R1 sur la manette \n")
instructMenu.add.label("Pour le joueur 2: \n Les déplacement se font avec les touches flèches du clavier : \n UP,LEFT,DOWN,RIGHT et le joystick gauche de la manette \n On tire en utilisant la touche LCtrl ou le bouton R1 sur la manette \n")

# Make Options Menu

optionsMenuTheme = pygame_menu.themes.THEME_DARK.copy()
optionsMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
optionsMenuTheme.title_background_color = (0, 0, 0, 25)
optionsMenuTheme.title_offset = (screenWidth/2.75, 0)
optionsMenuTheme.title_font = pygame_menu.font.FONT_DIGITAL
optionsMenuTheme.background_color = (17, 26, 43)
optionsMenuTheme.widget_font = pygame_menu.font.FONT_DIGITAL
optionsMenuTheme.widget_font_size = 15

optionsMenu = pygame_menu.Menu(
    'Options', screenWidth, screenHeight, theme=optionsMenuTheme)


# Make main menu

mainMenuTheme = pygame_menu.themes.THEME_DARK.copy()
mainMenuTheme.background_color = pygame_menu.BaseImage(
    'assets/images/space_bg.png')
mainMenuTheme.title_background_color = (0, 0, 0, 25)
mainMenuTheme.title_font = pygame_menu.font.FONT_DIGITAL
mainMenuTheme.title_offset = (screenWidth/2.75, 0)
mainMenuTheme.widget_font = pygame_menu.font.FONT_DIGITAL
mainMenuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE


mainMenu = pygame_menu.Menu(
    'Pi-Fighters', screenWidth, screenHeight, theme=mainMenuTheme)
mainMenu.add.button('Play', main)
mainMenu.add.button('Instructions', instructMenu)
mainMenu.add.button('Options', optionsMenu)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)

# Run your menu
mainMenu.mainloop(surface)
