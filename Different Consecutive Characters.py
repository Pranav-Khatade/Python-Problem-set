'''Problem Statement
Chef has a binary string 
𝑆
S of length 
𝑁
N. Chef can perform the following operation on 
𝑆
S:

Insert any character (0 or 1) at any position in 
𝑆
S.
The goal is to find the minimum number of operations Chef needs to perform so that no two consecutive characters in 
𝑆
S are the same.

Input Format
The first line contains a single integer 
𝑇
T — the number of test cases.
For each test case:
The first line contains an integer 
𝑁
N — the length of the binary string 
𝑆
S.
The second line contains a binary string 
𝑆
S of length 
𝑁
N consisting of 0s and 1s.
Output Format
For each test case, output the minimum number of operations Chef needs to perform so that no two consecutive characters in 
𝑆
S are the same. Print each result on a new line.

Constraints
1
≤
𝑇
≤
100
1≤T≤100
1
≤
𝑁
≤
1000
1≤N≤1000
'''
t=int(input(""))

for i in range (0,t):
    n=int(input(""))
    p=input("")
    c=0
    for j in range(0,n-1):
        if(p[j]==p[j+1]):
            c+=1
        else:
            continue
    print(c)
