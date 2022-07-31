#Q. Write a program which accept one number and display below pattern.
#Input : 4
#Output : * * * *  * * * *    
#          * * *    * * *  
#           * *      * *
#            *        *              

def pattern(n):
    for i in range(n,0,-1):  
        print(" "*(n-i)+"* "*i,"  "*(n-i)+"* "*i)
        
def main():
    no= int(input("Enter a number:"))
    pattern(no)
    
if __name__ == "__main__":  
    main()
    