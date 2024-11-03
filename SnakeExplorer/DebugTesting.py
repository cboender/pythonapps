import sys
import  bigfont



def calcCenterLargeText(word):
    l = len(word)
    width = l * 4 + (l - 1)
    left = (80 - width) / 2
    print(left)

def calcCenterNormalText(word):
    width = len(word)
    left = (80 - width) / 2
    print(left)

calcCenterNormalText('Press Enter to start')

print('\uF8FF')