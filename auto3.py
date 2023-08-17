# 上下左右 要關閉 Num.
import ctypes
import time
import random

# Constants for key press and release events
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
# Constants for mouse events
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Structure for the point
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

# Function to get the current mouse position
def get_mouse_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

# Function to simulate a mouse click at a new position with y offset
def mouse_click_with_offset(x_offset):
    # Get the current mouse position
    x, y = get_mouse_position()

    # Move to the new position
    ctypes.windll.user32.SetCursorPos(x + x_offset, y)

    # Simulate the mouse click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(6)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # Move back to the original position
    ctypes.windll.user32.SetCursorPos(x, y)
# Function to simulate a mouse click at a new position with y offset
def mouse_click_with_offset2(x_offset):
    # Get the current mouse position
    x, y = get_mouse_position()

    # Move to the new position
    ctypes.windll.user32.SetCursorPos(x + x_offset, y)

    # Simulate the mouse click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(4.1)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # Move back to the original position
    ctypes.windll.user32.SetCursorPos(x, y)
# Function to simulate a mouse click
def mouse_click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# Function to simulate key press and release
def press_key(scan_code):
    ctypes.windll.user32.keybd_event(0, scan_code, KEYEVENTF_SCANCODE, 0)
    ctypes.windll.user32.keybd_event(0, scan_code, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0)

# Tracking time for each key
keys = {
    "a": {"code":'a', "interval": 86, "scan_code": 0x1E, "next_press": 86},
    "s": {"code":'s', "interval": 188, "scan_code": 0x1F, "next_press": 188},
    "d": {"code":'d', "interval": 15, "scan_code": 0x20, "next_press": 15},
    "r": {"code":'r', "interval": 40, "scan_code": 0x13, "next_press": 40},
    "f": {"code":'f', "interval": 90, "scan_code": 0x21, "next_press": 90},
    "end": {"code":'end', "interval": 160, "scan_code": 0xCF, "next_press": 160},
    "w": {"code":'w', "interval": 25, "scan_code": 0x11, "next_press": 25},
    "n": {"code":'n', "interval": 250, "scan_code": 0x31, "next_press": 250}
}

# Function to find the next key to be pressed
def find_next_key():
    return min(keys.items(), key=lambda x: x[1]["next_press"])


"""A module for simulating low-level keyboard and mouse key presses."""
import ctypes
import time
from ctypes import wintypes
import random


user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

MAPVK_VK_TO_VSC = 0
wintypes.ULONG_PTR = wintypes.WPARAM

KEY_MAP = {
    'left': 0x25,   # Arrow keys
    'up': 0x26,
    'right': 0x27,
    'down': 0x28,

    'backspace': 0x08,      # Special keys
    'tab': 0x09,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'caps lock': 0x14,
    'esc': 0x1B,
    'space': 0x20,
    'page up': 0x21,
    'page down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'insert': 0x2D,
    'delete': 0x2E,

    '0': 0x30,      # Numbers
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,

    'a': 0x41,      # Letters
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,

    'f1': 0x70,     # Functional keys
    'f2': 0x71,
    'f3': 0x72,
    'f4': 0x73,
    'f5': 0x74,
    'f6': 0x75,
    'f7': 0x76,
    'f8': 0x77,
    'f9': 0x78,
    'f10': 0x79,
    'f11': 0x7A,
    'f12': 0x7B,
    'num lock': 0x90,
    'scroll lock': 0x91,

    ';': 0xBA,      # Special characters
    '=': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE
}

class MouseInput(ctypes.Structure):
    _fields_ = (('dx', wintypes.LONG),
                ('dy', wintypes.LONG),
                ('mouseData', wintypes.DWORD),
                ('dwFlags', wintypes.DWORD),
                ('time', wintypes.DWORD),
                ('dwExtraInfo', wintypes.ULONG_PTR))


class HardwareInput(ctypes.Structure):
    _fields_ = (('uMsg', wintypes.DWORD),
                ('wParamL', wintypes.WORD),
                ('wParamH', wintypes.WORD))
    
class KeyboardInput(ctypes.Structure):
    _fields_ = (('wVk', wintypes.WORD),
                ('wScan', wintypes.WORD),
                ('dwFlags', wintypes.DWORD),
                ('time', wintypes.DWORD),
                ('dwExtraInfo', wintypes.ULONG_PTR))

    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)
def key_down(key):
    """
    Simulates a key-down action. Can be cancelled by Bot.toggle_enabled.
    :param key:     The key to press.
    :return:        None
    """

    key = key.lower()
    if key not in KEY_MAP.keys():
        print(f"Invalid keyboard input: '{key}'.")
    else:
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key]))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def key_up(key):
    """
    Simulates a key-up action. Cannot be cancelled by Bot.toggle_enabled.
    This is to ensure no keys are left in the 'down' state when the program pauses.
    :param key:     The key to press.
    :return:        None
    """

    key = key.lower()
    if key not in KEY_MAP.keys():
        print(f"Invalid keyboard input: '{key}'.")
    else:
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key], dwFlags=KEYEVENTF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def press(key, n, down_time=0.05, up_time=0.1):
    """
    Presses KEY N times, holding it for DOWN_TIME seconds, and releasing for UP_TIME seconds.
    :param key:         The keyboard input to press.
    :param n:           Number of times to press KEY.
    :param down_time:   Duration of down-press (in seconds).
    :param up_time:     Duration of release (in seconds).
    :return:            None
    """

    for _ in range(n):
        delay = random.uniform(0, 1)
        key_down(key)
        time.sleep(down_time * (0.8 + 0.4 * delay))
        key_up(key)
        time.sleep(up_time * (0.8 + 0.4 * delay))

class Input(ctypes.Structure):
    class _Input(ctypes.Union):
        _fields_ = (('ki', KeyboardInput),
                    ('mi', MouseInput),
                    ('hi', HardwareInput))

    _anonymous_ = ('_input',)
    _fields_ = (('type', wintypes.DWORD),
                ('_input', _Input))

def mypress(key):
    '''
    key = d
    n = 1次
    '''
    for i in range(0,1):
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key]))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
        delay = random.uniform(0, 1)
        time.sleep(0.05 * (0.8 + 0.4 * delay))
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key], dwFlags=KEYEVENTF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
        time.sleep(0.1 * (0.8 + 0.4 * delay))    




# Infinite loop to keep pressing the keys at the desired intervals
elapsed_time = 0
next_dump=60
alt_down_timer = 0
while True:
    '''
    alt_down_timer=alt_down_timer +1
    print("jump event:")
    print(next_dump-alt_down_timer)
    
    if alt_down_timer >= next_dump:
        mouse_click()
        mouse_click_with_offset(-50)
        mouse_click_with_offset2(50)
        # Add a random delay between 0 to 5 seconds after pressing the key
        delay = random.uniform(0, 5)
        print(f"Adding a random delay of {delay:.2f} seconds.")
        time.sleep(delay)
        press_key(0x2d)#x
        alt_down_timer = 0
        next_dump = random.uniform(60, 180)
    '''
    next_key, next_data = find_next_key()
    remaining_time = next_data["next_press"] - elapsed_time
    print(f"Next key: '{next_key}' will be pressed in {remaining_time} seconds.")
    
    time.sleep(1)
    elapsed_time += 1
    
    if elapsed_time >= next_data["next_press"]:
        #press_key(next_data["scan_code"])
        mypress(next_data["code"])
        next_data["next_press"] += next_data["interval"]
        # Add a random delay between 0 to 5 seconds after pressing the key
        delay = random.uniform(0, 5)
        print(f"Adding a random delay of {delay:.2f} seconds.")
        time.sleep(delay)
        elapsed_time += delay

# This will repeat indefinitely
