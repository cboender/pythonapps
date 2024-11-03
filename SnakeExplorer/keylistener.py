import msvcrt
import threading
import time

_listeners = {}
_running = False
_processing = False
_listener_actions = [] #array of name of listeners to remove
def start():
    global _running
    _running = True
    global _processing
    t = threading.Thread(target = _listen)
    t.start()

def _listen():
    while _running:
        if msvcrt.kbhit():
            global key
            key = ord(msvcrt.getch())
            if key == 0:
                key = ord(msvcrt.getch())
            global _processing
            _processing = True
            for listener in _listeners.items():
                listener[1](key)
            _processing = False
            update_listeners()


    print('End listener')

def update_listeners():
    for action in _listener_actions:
        match action[0]:
            case 'add':
                _listeners[action[2]] = action[1]
            case 'remove':
                _listeners.pop(action[1])
    _listener_actions.clear()

def stop():
    global _running
    _running = False

def addListener(listener, name=time.time()):
    if _processing:
        _listener_actions.append(('add', listener, name))
    else:
        _listeners[name] = listener

def removeListener(name):
    if _processing:
        _listener_actions.append(('remove', name))
    else:
        _listeners.pop(name)