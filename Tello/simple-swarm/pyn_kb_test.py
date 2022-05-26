from pynput.keyboard import Listener as KeyboardListener


def on_press(key):
    print("Key pressed: {0}".format(key))

def on_release(key):
    print(" {0}".format(key))



# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
keyboard_listener.join()
