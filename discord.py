import time
import random
from pynput import keyboard, mouse

should_strafe = False
center_x = 960

mouse_controller = None
keyboard_controller = None

def on_press(key):
    global should_strafe

    if key == keyboard.Key.space:
        should_strafe = True

def on_release(key):
    global should_strafe

    if key == keyboard.Key.insert:
        print("Quitting.")
        return False

    elif key == keyboard.Key.space:
        keyboard_controller.release('a')
        keyboard_controller.release('d')

        should_strafe = False

def do_strafe():
    global center_x, mouse_controller, keyboard_controller

    x, _ = mouse_controller.position
    print(x)
    # 0.0001
    # 0.0003
    # delay = random.uniform(0.0, 0.000003)
    # print(f"\t{delay}")
    # time.sleep(delay)  # Add a random delay between 0.01 and 0.1 seconds
    # strafe right
    if x > center_x:
        keyboard_controller.press('d')
        keyboard_controller.release('a')

    elif x < center_x:
        keyboard_controller.press('a')
        keyboard_controller.release('d')
    
    # else:
    #     # time.sleep(random.uniform(0.0, 0.0005))  # Add a random delay between 0.01 and 0.1 seconds
    #     keyboard_controller.release('d')
    #     keyboard_controller.release('a')






def main():
    global mouse_controller, keyboard_controller
    mouse_controller = mouse.Controller()
    keyboard_controller = keyboard.Controller()

    print("Press INSERT to quit.")

    # Start listener
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:

        while True:
            if should_strafe:
                do_strafe()
            # time.sleep(0.00001)  # Adjust the sleep duration as needed
            delay = random.uniform(0.0, 0.0001)
            print(f"\t", delay)
            time.sleep(delay)
            
            # Break the loop and exit the program if insert key is pressed
            if not listener.running:
                break

if __name__ == "__main__":
    main()
