# if __name__ == '__main__':
#     x = []
#     y = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         x.append([name, score])
#         y.append(score)
#
# y = list(set(y))
# y.sort()
# max_2 = y[1]
# x = sorted(x)
# for names, scores in x:
#     if scores == max_2:
#         print(names)

n = int(input())
arr = list(map(int, input().split()))
print(max([i for i in arr if i != max(arr)]))

