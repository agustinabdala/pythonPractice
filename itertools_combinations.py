from itertools import combinations

if __name__ == '__main__':

    inputs = input().split()
    # print(inputs)
    s = str(inputs[0])
    n = int(inputs[1])

    for i in range(1, int(n)+1):
        result = ["".join(sorted(i)) for i in combinations(s, i)]
        result.sort()
        print("\n".join(result))
