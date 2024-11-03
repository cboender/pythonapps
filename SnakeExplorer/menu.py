import screen_ops as screen
import keylistener
from screen_ops import TextDescriptor
from game.game import Game


def show():
    screen.clear_background()
    screen.print_big_text('SNAKE', 27,2)
    screen.print_big_text('explorer', 20,10)

    screen.print_text('Press Enter to Start', 29,20, TextDescriptor(underline=True))
    keylistener.addListener(key_press,'menu')

def start_game():
    keylistener.removeListener('menu')
    Game().start()

def key_press(key):
    if key == 13:
        start_game()
    elif key == 27:
        quit()

