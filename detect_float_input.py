if __name__ == '__main__':

    N = str(input())

    result = "False"
    if N.startswith('+') or N.startswith('+.') and N[1].isdigit():
        result = True
    if N.startswith('-') or N.startswith('-.')and N[1].isdigit():
        result = "True"
    if N.startswith('.') and N[1].isdigit():
        result = "True"
    if N.
    print(result)
