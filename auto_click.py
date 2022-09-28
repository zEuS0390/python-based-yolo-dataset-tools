# This program is used for Google Colab to avoid runtime disconnection due to inactivity for 30 minutes.
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import threading, time

print("Press 's' to start/stop the auto-click.", "Press 'e' to exit the program.", end="\n")

delay = 10
button = Button.left
btn_str = 'Mouse Left'
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.times = 0
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
    def start_clicking(self):
        print("Start clicking.")
        self.running = True
    def stop_clicking(self):
        print("Stop clicking.")
        self.running = False
    def exit(self):
        print("Exit program.")
        self.stop_clicking()
        self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
                self.times += 1
                print(f"[{btn_str}] {self.times}")
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()