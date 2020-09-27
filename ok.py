# prob 1:
#
# def split_and_join(line):
#     # write your code here
#     splitbaby=line.split(' ')
#     return '-'.join(splitbaby)
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
#prob 2
# def count_substring(string, sub_string):
#     count=0
#     for i in range(0,len(string)):
#         string_occurence=string.count(sub_string)
#     return
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
#prob 3
# def print_res(s):
#     print(any(c.isalnum() for c in s),any(c.isalpha() for c in s),any(c.isdigit() for c in s),any(c.islower() for c in s),any(c.isupper() for c in s),sep="\n")
#
#
# if __name__ == '__main__':
#     s = input()
#     print_res(s)
# prb 4
# def print_formatted(number):
#     # your code goes here
#     l=len(bin(n)[2:])
#     for i in range(1,n+1):
#         o=oct(i)[2:]
#         h=hex(i)[2:].upper()
#         b=bin(i)[2:]
#         print (str(i).rjust(l),str(o).rjust(l),str(h).rjust(l),str(b).rjust(l))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

#prob 5
def merge_the_tools(s, k):
    for i in range(0, len(s), k):

        r = ""
        for j in range(k):
            if i + j < len(s) and s[i + j] not in r:
                r = r + s[i + j]
        print(r)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

