#Q.2.Write a program which accept number from user and display its factors in decreasing order.
def dec():
	n=int(input('Enter a number: '))
	b=[]
	for i in range(1,n):
		if(n%i)==0:
			b.append(i)
	print(b)
	b.reverse()
	print(b)
dec()
