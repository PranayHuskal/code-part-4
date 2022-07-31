#Q.2. Write a program which accept number from user and print even factors of that number.

def even_fact(n):
	for i in  range(1,n-1):
		if(n%i)==0:
			if i%2==0:
				print(i,end=' ')

n= int(input('enter a number'))
even_fact(n)