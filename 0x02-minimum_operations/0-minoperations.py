#!/usr/bin/env python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in
this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


# def minOperations(n):
#     """
#     Returns the fewest number of operations needed to result in exactly
#     n H characters in the file.
#     """
#     def minOperations(n):
#         """Calculate fewest no. of operations needed to
#  result in n H characters"""
#         t = 0
#         m = 2
#         while n > 1:
#             while not n % m:
#                 t += m
#                 n /= m
#             m += 1
#         return t


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count
