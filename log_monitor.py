# log_monitor.py

import time

# Path to the log file you want to monitor
#sudo journalctl -f > ~/log-monitor-devops/sample.log
# this that docker needs to acces it from the main is not possible so this is how we do it
LOG_FILE = "sample.log"  # Works for Ubuntu systems
#LOG_FILE = "/var/log/syslog"


# Keywords to look for
KEYWORDS = ["error", "failed", "critical"]

def process_log_lines(file):
    """
    Reads lines from a file-like object once and returns alerts found.
    Returns a list of alert messages.
    """
    alerts = []
    for line in file:
        for keyword in KEYWORDS:
            if keyword.lower() in line.lower():
                alerts.append(f"[ALERT] Keyword '{keyword}' found:\n{line.strip()}")
    return alerts


def monitor_log():
    """
    Continuously reads a log file and prints an alert if any of the KEYWORDS appear in new log lines.
    """
    try:
        with open(LOG_FILE, "r") as file:
            file.seek(0, 2)  # Move to the end of the file

            print(f"Monitoring {LOG_FILE} for keywords: {KEYWORDS}...\n")
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)
                    continue

                for keyword in KEYWORDS:
                    if keyword.lower() in line.lower():
                        print(f"[ALERT] Keyword '{keyword}' found:\n{line.strip()}\n")

    except FileNotFoundError:
        print(f"Log file {LOG_FILE} not found. Please check the path.")
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

if __name__ == "__main__":
    monitor_log()

