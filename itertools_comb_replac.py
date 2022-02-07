from itertools import combinations_with_replacement

if __name__ == '__main__':

    inputs = input().split()
    # print(inputs)
    s = str(inputs[0])
    n = int(inputs[1])

    result = ["".join(sorted(i)) for i in combinations_with_replacement(s, n)]
    result.sort()
    print("\n".join(result))
