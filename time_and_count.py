'''
Melinda Grad
CS 305
ASM 6
'''

import time

def time_and_count(function):
    """ the decorator counts how many times f has been called, and
    for each call, how long it takes to execute
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1

        start = time.time()
        call = function(*args, **kwargs)
        end = time.time()
        wrapper.time = end - start

        #format output
        wrapper.out = {wrapper.count: wrapper.time}

        return call
    wrapper.count = 0
    return wrapper

if __name__ == '__main__':

    """Function to be decorated"""
    @time_and_count
    def countdown(num: int):
        """ count down from n to 0 """
        while num > 0:
            num -= 1

    """Function to be decorated"""
    @time_and_count
    def sum_of_squares(num):
        total = 0
        for i in range(num):
            total += i*i
        return total

    '''********TESTING OUTPUT CODE BELOW*******'''

    print('sum of squares(10000)')
    for i in range(10):
        sum_of_squares(10000)
        print(sum_of_squares.out)

    print('countdown(10000)')
    for i in range(1, 10):
        countdown(10000)
        print(countdown.out)
