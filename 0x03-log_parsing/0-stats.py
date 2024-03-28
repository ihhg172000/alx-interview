#!/usr/bin/python3
"""
0-stats.py
"""
import signal
import sys
import re

pattern = r'^(\S+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)'

total_file_size = 0
stats = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0,
}
line_count = 0


def print_statistics():
    """
    Prints statistics.
    """
    print(f"File size: {total_file_size}")

    for k, v in stats.items():
        if v > 0:
            print(f"{k}: {v}")


def  keyboard_interruption_handler(s, f):
    """
    Ctrl-C handler.
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, keyboard_interruption_handler)

if __name__ == "__main__":
    for line in sys.stdin:
        match = re.match(pattern, line)

        if line_count > 0 and line_count % 10 == 0:
            print_statistics()

        if match:
            status_code = match.group(3)
            file_size = match.group(4)

            if status_code in stats.keys():
                stats[status_code] += 1

            total_file_size += int(file_size)

        line_count += 1
