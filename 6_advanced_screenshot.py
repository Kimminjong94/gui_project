import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strtime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("=", screenshot)

keyboard.wait("esc")