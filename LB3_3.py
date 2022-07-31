#Q.3. Write a program which accept number from user and print even factors of that number.
def even_fact(n):
	i=1
	while(i<=n):
		if(n%i)==0:
			if(i%2)==0:
				print(i,end=' ')
		i=i+1


n= int(input('enter a number'))
even_fact(n)

