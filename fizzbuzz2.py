#!/usr/bin/python

def fizzbuzz():
    '''
    Prints fizz if divisble by 3, buzz if divisble by 5 and (only)
    fizzbuzz if divisble by 15.  Also gives the number when anything is printed.
    Alternate way using a string.
    '''
    for num in range (1, 101):
        s = ''
        if num % 3 == 0:
            s += 'Fizz'
        if num % 5 == 0:
            s += 'Buzz'
        if s == '':
            s = num
        print('{}-->{}'.format(num,s))

if __name__ == '__main__':
    fizzbuzz()
