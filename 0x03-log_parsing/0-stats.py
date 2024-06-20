#!/usr/bin/python3
"""
parsing function
"""
import sys
import signal

counters = {
    "size": 0,
    "lines": 1
}

cntCode = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

def printCodes():
    """
    Function to print the codes and the number of occurrences
    """
    # Print file size
    print("File size: {}".format(counters["size"]))
    # Print all codes
    for key in sorted(cntCode.keys()):
        # If a value is not 0
        if cntCode[key] != 0:
            print("{}: {}".format(key, cntCode[key]))

def countCodeSize(listData):
    """
    Count the codes and file size
    """
    # Validate format
    if len(listData) < 7:
        return
    # Validate request format
    if listData[5] != '"GET' or listData[6] != '/projects/260' or listData[7] != 'HTTP/1.1"':
        return
    try:
        # Count file size
        counters["size"] += int(listData[-1])
        # If exists the code
        if listData[-2] in cntCode:
            # Count status code
            cntCode[listData[-2]] += 1
    except ValueError:
        pass

def signal_handler(sig, frame):
    printCodes()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                countCodeSize(line.split(" "))
            except Exception:
                pass
            if counters["lines"] % 10 == 0:
                printCodes()
            counters["lines"] += 1
    except KeyboardInterrupt:
        printCodes()
        raise
    printCodes()
