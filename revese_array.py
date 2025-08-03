n=int(input("enter length of array:"))
num = []
for i in range(n):
    p = int(input("enter number :"))
    num.append(p)
print("your array :",num)
num[::-1]
print("reverse array",num)
