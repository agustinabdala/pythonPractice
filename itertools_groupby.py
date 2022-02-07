from itertools import groupby

if __name__ == '__main__':
    s = input()

    groups = []
    uniquekeys = []
    string = sorted(s)
    for k, g in groupby(s):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)

    for i in range(0, len(groups)):
        print((groups[i].count(uniquekeys[i]), int(uniquekeys[i])), end=" ")
