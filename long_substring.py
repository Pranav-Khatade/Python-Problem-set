string = str(input("Enter The string :"))
n = len(string)
new_s = ""
count = 0
done = False
for i in range(n):
	for j in range(i,n):
		if string[j] not in new_s:
			if string[i] != string[j+1]:
				new_s += string[j]
		else:
			done = True
			break
	if done:
		break

print(new_s)

#longest substring problem