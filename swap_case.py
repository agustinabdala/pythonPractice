def swap_case(s):
    new=""
    for i in s:
        if i.islower():
            new = new + i.upper()
        else:
            new = new + i.lower()
    
    return new


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)