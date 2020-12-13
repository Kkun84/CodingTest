import itertools

inf = float('inf')

N, X, Y = [int(i) for i in input().split()]

A_list = [{'R': False, 'B': True}[i] for i in input()[::2]]
B_list = [{'R': False, 'B': True}[i] for i in input()[::2]]

if X < 2 * Y:
    cost_list = []
    replaced = True
    for index, (A, B) in enumerate(zip(A_list, B_list)):
        if A == B:
            replaced = False
            cost_list.append(0)
        elif replaced:
            cost_list.append(Y)
            replaced = False
        elif A_list[index - 1] == B and A == B_list[index - 1]:
            cost_list[-1] = 0
            cost_list.append(X)
            replaced = True
        else:
            cost_list.append(Y)
            replaced = False
else:
    cost_list = [0 if A == B else Y for A, B in zip(A_list, B_list)]

print(sum(cost_list))

pass