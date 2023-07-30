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

        # Determine the number of bytes for the current character based on the leading bits
        if first_byte >> 7 == 0:  # Single-byte character
            num_bytes = 1
        elif first_byte >> 5 == 0b110:  # Two-byte character
            num_bytes = 2
        elif first_byte >> 4 == 0b1110:  # Three-byte character
            num_bytes = 3
        elif first_byte >> 3 == 0b11110:  # Four-byte character
            num_bytes = 4
        else:
            # Invalid leading byte, not following UTF-8 encoding rules
            return False

        # Check that the subsequent bytes are valid following bytes
        for i in range(1, num_bytes):
            if idx + i >= len(data) or not is_following_byte(data[idx + i]):
                return False

        idx += num_bytes

    return True
