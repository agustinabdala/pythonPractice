from tempfile import tempdir


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    ordered = list(set(arr))
    ordered.sort()

    print(ordered[-2])