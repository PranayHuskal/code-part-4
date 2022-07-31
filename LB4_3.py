#Q.3.Write a program which accept number from user and display all its non factors.
 
def non():
	n=int(input("enter a number: "))
	l=[]
	for i in range(1,n):
		if(n%i)!=0:
			l.append(i)
	print(l)
non()