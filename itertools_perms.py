from itertools import permutations

if __name__ == '__main__':
    
    
    inputs = input().split()
    #print(inputs)
    s = str(inputs[0])
    k = int(inputs[1])
    
    #debug print("str{} int{}".format(s,k))
    joined_vals = ["".join(i) for i in permutations(s,k)]
    joined_vals.sort()
    
    for i in range(0, len(joined_vals)):
        print(joined_vals[i])
