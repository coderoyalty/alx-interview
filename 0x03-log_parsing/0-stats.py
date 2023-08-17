#!/usr/bin/python3
"""
0-stats
script that reads for stdin and compute metrics
"""
import sys


def print_stats(status_codes, size):
    print(f"File size: {size}")
    for code, count in status_codes.items():
        if count != 0:
            print(f"{code}: {count}")


try:
    total_size = 0
    count = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0,
        "401": 0, "403": 0, "404": 0,
        "405": 0, "500": 0
    }
    for line in sys.stdin:
        chunks = line.split()

        if count == 10:
            print_stats(status_codes, total_size)

        count += 1

        try:
            total_size += int(chunks[-1])
        except Exception:
            pass

        try:
            if chunks[-2] in status_codes:
                status_codes[chunks[-2]] += 1
        except Exception:
            pass
    print_stats(status_codes, total_size)


except KeyboardInterrupt:
    print_stats(status_codes, total_size)
    raise
