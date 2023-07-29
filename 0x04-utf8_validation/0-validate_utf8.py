#!/usr/bin/env python3
'''UTF-8 validation'''


def validUTF8(data):
    '''UTF-8 validation'''
    n = len(data)
    i = 0

    while i < n:
        # Check if the first byte is valid
        if data[i] > 0x7F:
            # Determine the character length based on the first byte
            if data[i] & 0xF0 == 0xF0:  # 4-byte utf-8 character encoding
                span = 4
            elif data[i] & 0xE0 == 0xE0:  # 3-byte utf-8 character encoding
                span = 3
            elif data[i] & 0xC0 == 0xC0:  # 2-byte utf-8 character encoding
                span = 2
            else:
                return False

            # Check if there are enough bytes remaining in the data list
            if i + span > n:
                return False

            # Check if the continuation bytes are valid (start with 10xxxxxx)
            for j in range(i + 1, i + span):
                if data[j] & 0xC0 != 0x80:
                    return False

            # Move to the next character
            i += span
        else:
            i += 1

    return True
