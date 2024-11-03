import menu, cursor, keylistener
import screen_ops as screen
from screen_ops import TextDescriptor

def init():
    if not screen.validate_screen():
        quit()

    cursor.hide_cursor()
    keylistener.addListener(key_press)
    keylistener.start()
    screen.init()
    menu.show()

def key_press(key):
    pass
init()