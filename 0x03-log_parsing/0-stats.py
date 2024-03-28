#!/usr/bin/python3
"""
0-stats.py
"""
import sys
import re


def print_statistics(total_file_size: int, stats: dict) -> None:
    """
    Prints statistics.
    """
    print(f"File size: {total_file_size}")

    for k, v in stats.items():
        if v > 0:
            print(f"{k}: {v}")


if __name__ == "__main__":
    p = r'^(\S+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)'

    total_file_size = 0
    stats = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_file_size, stats)

            match = re.match(p, line)

            if match:
                status_code = match.group(3)
                file_size = match.group(4)

                if status_code in stats.keys():
                    stats[status_code] += 1

                total_file_size += int(file_size)
    except KeyboardInterrupt:
        print_statistics(total_file_size, stats)
        raise
