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
    "a": {"interval": 86, "scan_code": 0x1E, "next_press": 86},
    "s": {"interval": 188, "scan_code": 0x1F, "next_press": 188},
    "d": {"interval": 15, "scan_code": 0x20, "next_press": 15},
    "r": {"interval": 40, "scan_code": 0x13, "next_press": 40},
    "f": {"interval": 90, "scan_code": 0x21, "next_press": 90},
    "end": {"interval": 160, "scan_code": 0xCF, "next_press": 160},
    "w": {"interval": 25, "scan_code": 0x11, "next_press": 25},
    "n": {"interval": 250, "scan_code": 0x31, "next_press": 250}
}

# Function to find the next key to be pressed
def find_next_key():
    return min(keys.items(), key=lambda x: x[1]["next_press"])

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
        press_key(next_data["scan_code"])
        next_data["next_press"] += next_data["interval"]
        # Add a random delay between 0 to 5 seconds after pressing the key
        delay = random.uniform(0, 5)
        print(f"Adding a random delay of {delay:.2f} seconds.")
        time.sleep(delay)
        elapsed_time += delay

# This will repeat indefinitely
