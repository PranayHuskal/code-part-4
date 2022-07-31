#Q. Write a program which accept one number and display below pattern.
#Input : 5
#Output : *  
#         * * 
#         * * * 
#         * * * * 
#         * * * * *

def pattern(n):
    for i in range(1,n+1):
        print("* "*i)
        
def main():
    no= int(input("Enter a number:"))
    pattern(no)
    
if __name__ == "__main__":  
    main()
    