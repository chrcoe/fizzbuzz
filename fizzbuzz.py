def fizzbuzz():
    '''
    Prints fizz if divisble by 3, buzz if divisble by 5 and (only)
    fizzbuzz if divisble by 15.  Also gives the number when anything is printed.
    '''
    for num in range (1, 100):
        if num % 15 == 0:
            print('{}-->fizzbuzz'.format(num))
        else:
            if num % 3 == 0:
                print('{}-->fizz'.format(num))
            if num % 5 == 0:
                print('{}-->buzz'.format(num))


if __name__ == '__main__':
    fizzbuzz()
