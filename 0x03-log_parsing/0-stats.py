#!/usr/bin/python3
"""
Script to parse logs from stdin and compute metrics.
"""

import sys
import signal


def print_stats(total_size, status_counts):
    """
    Print the current statistics including total size and status code counts.
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def log_parsing():
    """
    Reads lines from stdin, parses them, and computes the required metrics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = parts[-1]

                # Update total file size
                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                # Update status code counts
                try:
                    status_code = int(status_code)
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except ValueError:
                    pass

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print stats upon keyboard interruption
        print_stats(total_size, status_counts)
        raise

    # Print stats at the end
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    log_parsing()
