#Q. Write a program which accept one number and display below pattern.
#Input : 5
#Output :  *
#          * *  
#          * * * 
#          * * * * 
#          * * * * *
#          * * * * 
#          * * * 
#          * *
#          *

def pattern(n):
    for i in range(1,n+1):
        print("* "*i)
    for i in range(n-1,0,-1):       # (n-1) is taken for n number of * line should not printed twice in middle portion.
        print("* "*i)
        
def main():
    no= int(input("Enter a number:"))
    pattern(no)
    
if __name__ == "__main__":  
    main()
   