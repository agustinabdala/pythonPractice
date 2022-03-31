if __name__ == '__main__':
    s = input()
    
    alnum = alpha = digit = lower = upper = 0

    for i in s:
           
        
        alnum += (1 if (i.isalnum()) else 0)
        alpha += (1 if (i.isalpha()) else 0)
        digit += (1 if (i.isdigit()) else 0)
        lower += (1 if (i.islower()) else 0)
        upper += (1 if (i.isupper()) else 0)
    
        
        
    print(True if alnum > 0 else False)    
    print(True if alpha > 0 else False)
    print(True if digit > 0 else False)
    print(True if lower > 0 else False)
    print(True if upper > 0 else False)


    