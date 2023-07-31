#!/usr/bin/python3
"""UTF-8 validation module.
"""


# def validUTF8(data):
#     # Helper function to check if a byte starts with '10'
#     def is_following_byte(byte):
#         return byte >> 6 == 0b10

#     # Iterate through the data bytes
#     idx = 0
#     while idx < len(data):
#         # Get the number of bytes for the current character
#         first_byte = data[idx]

#         # Determine the number of bytes for the current character
#         # based on the leading bits
#         if first_byte >> 7 == 0:  # Single-byte character
#             num_bytes = 1
#         elif first_byte >> 5 == 0b110:  # Two-byte character
#             num_bytes = 2
#         elif first_byte >> 4 == 0b1110:  # Three-byte character
#             num_bytes = 3
#         elif first_byte >> 3 == 0b11110:  # Four-byte character
#             num_bytes = 4
#         else:
#             # Invalid leading byte, not following UTF-8 encoding rules
#             return False

#         # Check that the subsequent bytes are valid following bytes
#         for i in range(1, num_bytes):
#             if idx + i >= len(data) or not is_following_byte(data[idx + i]):
#                 return False

#         idx += num_bytes

#     return True


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
