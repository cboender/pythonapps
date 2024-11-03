import os, math
import sys
import bigfont

screen_width =  84
screen_height = 34
start_x = 0
start_y = 0

class TextDescriptor:
    def __init__(self,color='30', background= '42', underline=False, container_size=0):
        self.color = color
        self.background=background
        self.underline=underline
        self.containerSize = container_size

    def get_attributes(self):
        attrs = [self.color,self.background]
        if self.underline:
            attrs.append('4')
        return '\x1b[' + ";".join(map(str, attrs)) + 'm'

    def get_reset_attributes(self):
        attrs = []
        if self.underline:
            attrs.append(str("24"))
        return '\x1b[' + ";".join(map(str, attrs)) + 'm'


def init():
    #Code to get command prompt and power sheell to work
    os.system('')
    sys.stdout.write('\x1b[2J')
    size = os.get_terminal_size()
    global start_x
    global start_y
    start_x = math.ceil((size.columns - screen_width) / 2)
    start_y = math.ceil((size.lines - screen_height) / 2)
    draw_border()
   # clear_background()

def screen_size():
    return os.get_terminal_size()

def validate_screen():
    size = os.get_terminal_size()
    valid = True
    if size.columns < screen_width:
        valid = False
        print("Columns on the screen must be larger than " + str(screen_width))

    if size.lines < screen_height:
        valid = False
        print("Lines on the screen should be larger than "  + str(screen_height))
    return valid


def draw_border():
    global start_x
    global start_y
    global screen_width
    global screen_height
    text = ''.rjust(screen_width - 4)


    for y in range(1,screen_height - 1):
        sys.stdout.write('\x1b[44m\x1b[{0};{1}H{2}'.format(y + start_y,start_x + screen_width - 3,'  '))
        sys.stdout.write('\x1b[44m\x1b[{0};{1}H{2}'.format(y + start_y,start_x,'  '))
    sys.stdout.write('\x1b[44m\x1b[{0};{1}H{2}'.format(start_y,start_x,text.rjust(screen_width - 1)))
    sys.stdout.write('\x1b[44m\x1b[{0};{1}H{2}'.format(start_y + screen_height - 2,start_x + 1,text))
    sys.stdout.flush()
    screen_width = screen_width -4
    screen_height = screen_height - 2
    start_x = start_x + 2
    start_y = start_y + 1

def clear_background():
    text = ''.rjust(screen_width - 1)
    global start_x
    global start_y
    for y in range(0,screen_height - 1):
        sys.stdout.write('\x1b[42m\x1b[{0};{1}H{2}'.format(y + start_y,start_x,text))
    sys.stdout.flush()

def print_text(text, x,y, descriptor = TextDescriptor()):
    output_text = text
    if descriptor.containerSize > 0:
        if len(text) > descriptor.containerSize:
            output_text = text[:descriptor.containerSize]
            pass
        else:
            output_text = text.center(descriptor.containerSize)

    commands = [descriptor.get_attributes(), '\x1b[{0};{1}H{2}', descriptor.get_reset_attributes()]
    line = ''.join(commands).format(y + start_y,x + start_x,output_text)
    sys.stdout.write(line)
    sys.stdout.flush()


def print_big_text(text, x,y):
    text = text.upper()
    x= x + start_x
    y = y + start_y

    for c in text:
        letter = "".join([l.value for l in bigfont.letters[c]])
        line = '\x1b[37;42m\x1b[{0};{1}H\x1b[s{2}'.format(y,x,letter)
        sys.stdout.write(line)
        x = x + 5

    sys.stdout.flush()
