from enum import Enum
class Chars(Enum):
    FULL = '\u2588'
    NEW_LINE = '\x1b[u\x1b[1B\x1b[s'
    LOWER_HALF = '\u2584'
    UPPER_HALF = '\u2580'
    LEFT_HALF = '\u258C'
    RIGHT_HALF = '\u2590'

    def move_cols(cols):
        return _CharReturn(name='move_cols', value= '\x1b[{0}C'.format(cols))

class _CharReturn:
    def __init__(self, name, value):
        self.name = name
        self.value = value

letters = {
    'S': [Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL,Chars.NEW_LINE,
          Chars.move_cols(3), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL],
    'N': [Chars.FULL, Chars.move_cols(2), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.FULL,Chars.move_cols(1), Chars.FULL,Chars.NEW_LINE,
          Chars.FULL,Chars.FULL,Chars.FULL,Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.move_cols(1),Chars.FULL,Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2),Chars.FULL],
    'A': [Chars.move_cols(1), Chars.FULL, Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.FULL,Chars.FULL,Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2),Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2),Chars.FULL],
    'K': [Chars.FULL,Chars.move_cols(2),Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(1), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(1), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.move_cols(2),Chars.FULL],
    'E': [Chars.FULL,Chars.FULL,Chars.FULL,Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.FULL,Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.FULL,Chars.FULL,Chars.FULL],
    'X': [Chars.FULL,Chars.move_cols(2), Chars.FULL, Chars.NEW_LINE,
          Chars.RIGHT_HALF, Chars.LEFT_HALF,Chars.RIGHT_HALF, Chars.LEFT_HALF, Chars.NEW_LINE,
          Chars.move_cols(1), Chars.RIGHT_HALF, Chars.LEFT_HALF, Chars.NEW_LINE,
          Chars.RIGHT_HALF, Chars.LEFT_HALF,Chars.RIGHT_HALF, Chars.LEFT_HALF, Chars.NEW_LINE,
          Chars.FULL,Chars.move_cols(2), Chars.FULL],
    'L': [Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL],
    'O': [Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2), Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2), Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2), Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.FULL, Chars.FULL],
    'R': [Chars.FULL, Chars.FULL, Chars.FULL, Chars.LOWER_HALF, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(1), Chars.LOWER_HALF, Chars.FULL,Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.UPPER_HALF, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(1), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL,Chars.move_cols(2),Chars.FULL],
    'P': [Chars.FULL, Chars.FULL, Chars.FULL, Chars.LOWER_HALF, Chars.NEW_LINE,
          Chars.FULL, Chars.move_cols(2), Chars.FULL, Chars.NEW_LINE,
          Chars.FULL, Chars.FULL, Chars.FULL, Chars.UPPER_HALF, Chars.NEW_LINE,
          Chars.FULL, Chars.NEW_LINE,
          Chars.FULL
         ]
}