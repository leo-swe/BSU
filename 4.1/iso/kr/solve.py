from itertools import permutations

A = [
    [9, 4, 3, 7],
    [4, 6, 5, 6],
    [5, 4, 7, 5],
    [7, 5, 2, 3],
    [10, 6, 7, 4],
]


n = 4
best = min(((sum(A[i][p[i]] for i in range(n)), p) for p in permutations(range(n))), key=lambda x: x[0])
cost, p = best

# (3, 1, 2, 4)

print()
print("Перестановка:", tuple(i + 1 for i in p))
print("Минимальная стоимость:", cost)

# # ###########################################


# # def hungarian(a):
# #     n = len(a)
# #     m = len(a[0])
# #     u = [0] * (n + 1)
# #     v = [0] * (m + 1)
# #     p = [0] * (m + 1)
# #     way = [0] * (m + 1)
# #     for i in range(1, n + 1):
# #         p[0] = i
# #         j0 = 0
# #         minv = [float("inf")] * (m + 1)
# #         used = [False] * (m + 1)
# #         while True:
# #             used[j0] = True
# #             i0 = p[j0]
# #             delta = float("inf")
# #             j1 = 0
# #             for j in range(1, m + 1):
# #                 if not used[j]:
# #                     cur = a[i0 - 1][j - 1] - u[i0] - v[j]
# #                     if cur < minv[j]:
# #                         minv[j] = cur
# #                         way[j] = j0
# #                     if minv[j] < delta:
# #                         delta = minv[j]
# #                         j1 = j
# #             for j in range(0, m + 1):
# #                 if used[j]:
# #                     u[p[j]] += delta
# #                     v[j] -= delta
# #                 else:
# #                     minv[j] -= delta
# #             j0 = j1
# #             if p[j0] == 0:
# #                 break
# #         while True:
# #             j1 = way[j0]
# #             p[j0] = p[j1]
# #             j0 = j1
# #             if j0 == 0:
# #                 break

# #     ans = [-1] * n
# #     for j in range(1, m + 1):
# #         if p[j] != 0:
# #             ans[p[j] - 1] = j - 1
# #     cost = sum(a[i][ans[i]] for i in range(n))
# #     return cost, ans


# # A = [
# #     [9, 4, 3, 7],
# #     [4, 6, 5, 6],
# #     [5, 4, 7, 5],
# #     [7, 5, 2, 3],
# #     [10, 6, 7, 4],
# # ]

# # cost, assignment = hungarian(A)

# # print()
# # print("Перестановка:", tuple(x + 1 for x in assignment))
# # print("Минимальная стоимость:", cost)
