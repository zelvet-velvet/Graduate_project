from pynput.keyboard import Listener as KeyboardListener
import time
from threading import Thread
import threading
from pynput.keyboard import Key, Controller

def on_press(key):
    #print("Key pressed: {0}".format(key))
    global k
    k =f"{key}"
    if k=='"\'"':
        k="@"
    

def on_release(key):
    #print("Key release: {0}".format(key))
    global r
    r = f"{key}"

def mov():
    while True:
        print("wee")
        time.sleep(1)

a= "wee"

locals()[a]=Thread(target = mov,daemon = True)
locals()[a].start()
print(locals()[a])
b="bruh"
locals()[b] = threading.Event()

class b():
    def __init__(self):
        while True:
            print("r:"+r+"k:"+k)
            time.sleep(1)


# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()

if __name__ == '__main__':
    keyboard = Controller()
    time.sleep(1)
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(1)
    print("start")
    bing =b()
    

keyboard_listener.join()
