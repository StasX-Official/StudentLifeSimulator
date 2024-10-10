import time
from system.main import StudentLifeGame

try:
    app = StudentLifeGame()
    app.start()
except ImportError as e:
    print(f"Import error: {e}")
    print("A critical error has occurred, please try again later...")
    with open("system/logs/crach.log", "a") as log_file:
        log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] - Import error: {e}"+"\n")
    time.sleep(3)
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print("A critical error has occurred, please try again later...")
    with open("system/logs/crach.log", "a") as log_file:
        log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] - An unexpected error occurred: {e}"+"\n")
    time.sleep(3)
    exit()

#Copyright (c) 2024 Kozosvyst Stas (StasX)