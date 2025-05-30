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

while True:
    level = random.choice(log_levels)
    msg = random.choice(messages)
    with open(log_file, "a") as f:
        f.write(f"{level}: {msg}\n")
    time.sleep(2)  # Adjust speed as needed
