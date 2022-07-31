#Q. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

def pattern(n):
    for i in range(n):
        print("* "*n)
        
def main():
    no= int(input("Enter a number:"))
    pattern(no)
    
if __name__ == "__main__":  
    main()
    