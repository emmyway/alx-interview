#!/usr/bin/python3
"""
Script to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers where each integer represents
                            a byte (8 least significant bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character being processed
    num_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Mask to get only the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue  # 1-byte character (ASCII), no need to do anything
            elif (byte & (mask1 >> 1)) == 0:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == 0:
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == 0:
                num_bytes = 3
            else:
                return False
        else:
            # For the continuation bytes, they must have the format 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
