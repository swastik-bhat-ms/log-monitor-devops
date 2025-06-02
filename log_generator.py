# log-generator.py

import time
import random

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User logged in",
    "Database connection failed",
    "File not found",
    "Task completed",
    "Unexpected value received"
]

log_file = "sample.log"

def write_random_log_entry():
    level = random.choice(log_levels)
    msg = random.choice(messages)
    with open(log_file, "a") as f:
        f.write(f"{level}: {msg}\n")

if __name__ == "__main__":
    while True:
        write_random_log_entry()
        time.sleep(50)  # Adjust speed as needed

