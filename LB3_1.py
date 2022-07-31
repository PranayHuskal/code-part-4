#Q.1.Write a program which accept one number from user and print that number of even numbers on screen.

def even(n):
	for i in  range(n):
		print(2*(i+1),end=' ')

n= int(input('enter a number'))
even(n)

