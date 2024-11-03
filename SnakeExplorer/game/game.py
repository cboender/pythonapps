import screen_ops as screen
import keylistener, menu
from screen_ops import TextDescriptor
from game.snake import Snake
import time
import threading
import random


_SNAKE_CHAR = '\u2588'
_APPLE_CHAR = '\xF0'
_MAX_APPLE_AMT = 2
_APPLE_DELAY = 16
class Game:
    def __init__(self):
        self.game_thread = None
        self._game_running = False
        self._screen_size = (78,30)
        self._snake = Snake()
        self._next_dir = None
        self.apples = []
        self.score = 0
        self.apple_spawn_counter = 0
    def start(self):
        #Setup game an screen
        self._game_running = True
        keylistener.addListener(self.key_press,'game')
        screen.clear_background()

        #build the snake
        self._snake.add_part(x=40, y= 15)
        self._snake.add_part(x=40, y= 16)
        self._snake.add_part(x=40, y= 17)
        self._snake.add_part(x=40, y= 18)
        for part in self._snake.list_parts():
            screen.print_text(_SNAKE_CHAR,part[0],part[1], TextDescriptor(color='36'))

        #Initalize apples
        self.add_apple()


        #Start game loop
        self.game_thread = threading.Thread(target = self.game_loop)
        self.game_thread.start()

    def add_apple(self):
        safe_space = False
        while not safe_space:
            apple = (random.randint(0,self._screen_size[0]),random.randint(0,self._screen_size[1]))
            if apple not in self._snake.list_parts():
                safe_space = True

        self.apples.append(apple)
        screen.print_text(_APPLE_CHAR,apple[0],apple[1], TextDescriptor(color='33'))

    def game_loop(self):
        while self._game_running:
            self.move_snake()
            if len(self.apples) <= _MAX_APPLE_AMT:
                self.apple_spawn_counter += 1
            if self.apple_spawn_counter == _APPLE_DELAY:
                self.add_apple()
                self.apple_spawn_counter = 0
            time.sleep(.1)
        menu.show()

    def move_snake(self):
        pos = self._snake.get_first_part()
        x = pos[0]
        y = pos[1]
        if self._next_dir is not None:
            self._snake.dir = self._next_dir

        if self._snake.dir[0] != 0:
            x += self._snake.dir[0]
        else:
            y += self._snake.dir[1]

        #Check for collision with walls
        if x < 0 or x > self._screen_size[0]:
            self.game_over()
            return
        elif y < 0 or y > self._screen_size[1]:
            self.game_over()
            return

        if (x,y) in self._snake.list_parts():
            self.game_over()

        grow = False
        if (x,y) in self.apples:
            grow = True
            self.apples.remove((x,y))
            self.score += 1
            screen.print_text(str(self.score),-1,-1, TextDescriptor(container_size=6, background=47))

        last_part = self._snake.move(x=x, y=y, grow=grow)
        if last_part is not None:
            screen.print_text(' ', last_part[0],last_part[1], TextDescriptor(color='36'))
        screen.print_text(_SNAKE_CHAR, x,y, TextDescriptor(color='36'))


    def change_snake_dir(self, dir):
        s = self._snake
        match dir:
            case 'up':
                if s.dir[1] != 1:
                    self._next_dir = (0,-1)
                pass
            case 'down':
                if s.dir[1] != -1:
                    self._next_dir = (0,1)
                pass
            case 'left':
                if s.dir[0] != 1:
                    self._next_dir = (-1,0)
                pass
            case 'right':
                if s.dir[0] != -1:
                    self._next_dir = (1,0)
                pass
    def game_over(self):
        self._game_running = False
        keylistener.removeListener('game')

    def key_press(self,key):
        if key == 27:
            self.game_over()
        elif key == 72 or key == 119:
            self.change_snake_dir('up')
        elif key == 80 or key == 115:
            self.change_snake_dir('down')
        elif key == 75 or key == 97:
            self.change_snake_dir('left')
        elif key == 77 or key == 100:
            self.change_snake_dir('right')

