'''DNA Storage
For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:
00 is replaced with A
01 is replaced with T
10 is replaced with C
11 is replaced with G

'''

t = int(input())

while t > 0:
    n = int(input())
    s = input()
    t -= 1
