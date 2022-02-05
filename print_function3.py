if __name__ == '__main__':
    n = int(input())
    result = 0
    expo = 0
    while n >= 1:
        if n <= 9:
            result += n*(10 ** expo)
            n -= 1
            expo += 1

        elif n >= 10 and n < 100:
            result += n*(10**(expo))
            n -= 1
            expo += 2

        elif n >= 100 and n < 151:
            result += n*(10**(expo))
            n -= 1
            expo += 3

    print(result)
