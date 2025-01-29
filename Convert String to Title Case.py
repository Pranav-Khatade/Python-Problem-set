'''
Convert String to Title Case

Given a string S consisting of only lowercase and uppercase English letters and spaces, your task is to convert it into title case. In title case, the first letter of each word is capitalized while the rest are in lowercase, except for words that are entirely in uppercase (considered as acronyms), which should remain unchanged.

Note:
Words are defined as contiguous sequences of English letters separated by spaces.
Acronyms are words that are entirely in uppercase and should remain unchanged.
Assume the input does not contain leading, trailing, or multiple spaces between words.
Input Format
The first line contains a single integer T, the number of test cases.
Each of the next T lines contains a string S.
Output Format
For each test case, print a single line containing the string S converted into title case.

Constraints
1 ≤ T ≤ 100
1 ≤ |S| ≤ 1000, where |S| is the length of the string.
'''

def is_acronym(word):
    return word.isupper()

def title_case(s):
    words = s.split()
    result = []
    
    for word in words:
        if is_acronym(word):
            result.append(word)
        else:
            result.append(word.capitalize())
    
    return " ".join(result)

T = int(input())

for _ in range(T):
    S = input()
    print(title_case(S))
