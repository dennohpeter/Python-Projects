def array_left_rotation(a, n, k):
    a.pop(0)
    print(a)

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
#print(*answer, sep=' ')
