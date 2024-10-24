#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print the statistics
def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Check if the line has the expected format
        if len(parts) < 7:
            continue
        
        try:
            # Extract the file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            
            # Update total file size
            total_size += file_size
            
            # Update the count for the status code if it's in the expected set
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
            
        except ValueError:
            # If file size or status code are not integers, skip the line
            continue
        
        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

