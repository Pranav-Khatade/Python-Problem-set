'''Wordle
Chef invented a modified Wordle.

There is a hidden word S and a guess word T, both of length 5.

Chef defines a string M to determine the correctness of the guess word. For the i<sup>th</sup> index:

If the guess at the i<sup>th</sup> index is correct, the i<sup>th</sup> character of M is G.
If the guess at the i<sup>th</sup> index is wrong, the i<sup>th</sup> character of M is B.
Given the hidden word S and guess T, determine string M.

Input Format
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains two lines of input:
First line contains the string S - the hidden word.
Second line contains the string T - the guess word.
Output Format
For each test case, print the value of string M.

You may print each character of the string in uppercase or lowercase (for example, the strings BgBgB, BGBGB, bgbGB, and bgbgb will all be treated as identical).

Constraints
1 ≤ T ≤ 1000
|S| = |T| = 5
S, T contain uppercase English alphabets only.

INPUT:
3  
ABCDE  
EDCBA  
ROUND  
RINGS  
START  
STUNT  

OUTPUT:
BBGBB  
GBBBB  
GGBBG  


---------END-------------
'''

p=int(input(""))
for i in range(0,p):
 S=input("")
 T=input("")
 M=""
 j=0
 while(j<5):
     
    if(S[j]==T[j]):
        M+="G"
    else:
        M+="B"
    j=j+1    
 print(M)
