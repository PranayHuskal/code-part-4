# Q.1.Write a program which accept number from user and display its multiplication of factors.

def multi():
	n=int(input('Enter a number: '))
	mult=1

	for i in range(1,n):
		if(n%i)==0:
			mult=mult*i
	print(mult)
multi()