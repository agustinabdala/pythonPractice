from itertools import permutations


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_perm = [x for x in range(x+1)]
    y_perm = [y for y in range(y+1)]
    z_perm = [z for z in range(z+1)]
    
    total_perms = [[x,y,z] for x in x_perm for y in y_perm for z in z_perm if (x+y+z)!=n]

    print(total_perms)
