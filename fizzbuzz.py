def fizzbuzz():
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
