#!/usr/bin/python

def fizzbuzz():
    '''
    Prints fizz if divisble by 3, buzz if divisble by 5 and (only)
    fizzbuzz if divisble by 15.  Also gives the number when anything is printed.
    '''
    for num in range (1, 101):
        if num % 15 == 0:
            print('{}-->FizzBuzz'.format(num))
        elif num % 3 == 0:
            print('{}-->Fizz'.format(num))
        elif num % 5 == 0:
            print('{}-->Buzz'.format(num))
        else:
            print('{}-->{}'.format(num, num))



if __name__ == '__main__':
    fizzbuzz()
