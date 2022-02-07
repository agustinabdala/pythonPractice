if __name__ == '__main__':
    N = int(input())

    cmds = []
    result_list = []
    for i in range(0, N):
        cmds.append(list(map(str, input().split())))

    for i in range(0, len(cmds)):
        # print(cmds[i][0])
        if cmds[i][0] == "insert":
            # print("inserting")
            result_list.insert(int(cmds[i][1]), int(cmds[i][2]))

        if cmds[i][0] == "append":
            # print("APPENDING")
            result_list.append(int(cmds[i][1]))

        elif cmds[i][0] == "remove":
            result_list.remove(int(cmds[i][1]))

        elif cmds[i][0] == "pop":
            result_list.pop()

        elif cmds[i][0] == "print":
            print(result_list)

        elif cmds[i][0] == "sort":
            result_list.sort()

        elif cmds[i][0] == "reverse":
            result_list.sort(reverse=True)
