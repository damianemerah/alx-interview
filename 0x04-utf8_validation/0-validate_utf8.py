#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    # Helper function to check if a byte starts with '10'
    def is_following_byte(byte):
        return byte >> 6 == 0b10

    # Iterate through the data bytes
    idx = 0
    while idx < len(data):
        # Get the number of bytes for the current character
        first_byte = data[idx]
        if first_byte >> 7 == 0:  # Single-byte character
            idx += 1
        elif first_byte >> 5 == 0b110:  # Two-byte character
            if idx + 1 >= len(data) or not is_following_byte(data[idx + 1]):
                return False
            idx += 2
        elif first_byte >> 4 == 0b1110:  # Three-byte character
            if idx + 2 >= len(data) or not is_following_byte(data[idx + 1])\
                    or not is_following_byte(data[idx + 2]):
                return False
            idx += 3
        elif first_byte >> 3 == 0b11110:  # Four-byte character
            if idx + 3 >= len(data) or not is_following_byte(data[idx + 1]) \
                or not is_following_byte(data[idx + 2])\
                    or not is_following_byte(data[idx + 3]):
                return False
            idx += 4
        else:
            # Invalid leading byte, not following UTF-8 encoding rules
            return False

    return True
