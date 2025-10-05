def factorial(sum1,x):
	sum1 = sum1
	if x==0 or x==1:
		sum1 = sum1*1
		print(sum1)
	else:
		sum1 = sum1*x
		factorial(sum1,x-1)

factorial(1,10)
