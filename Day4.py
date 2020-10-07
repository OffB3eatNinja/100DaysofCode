#problem 1
# N = int(input())
# setwa_ek=set([ int(i) for i in input().split()])
# M = int(input())
# setwa_2=set([ int(i) for i in input().split()])
# [print(i) for i in sorted(setwa_ek.symmetric_difference(setwa_2))]

N = int(input())
setwa_ek=set(input().split())
M = int(input())
setwa_2=set(input().split())
z=list(setwa_ek.symmetric_difference(setwa_2))
print(sorted(z))

#prob 2
# list_size = int(input())
# A = set(map(str, input().split()))
# num_lists = int(input())
# fin_lis = []
# for i in range(num_lists * 2):
#     fin_lis.append(list(map(str, input().split())))
# for i in range(len(fin_lis)):
#     if i%2 == 0:
#         if fin_lis[i][0] == "intersection_update":
#             A.intersection_update(set(fin_lis[i+1]))
#         elif fin_lis[i][0] == "update":
#             A.update(set(fin_lis[i+1]))
#         elif fin_lis[i][0] == "symmetric_difference_update":
#             A.symmetric_difference_update(set(fin_lis[i+1]))
#         if fin_lis[i][0] == "difference_update":
#             A.difference_update(set(fin_lis[i+1]))
# print(sum(list(map(int,A))))