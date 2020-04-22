import time
#recursion function is used to print a sample fibonacci series upto 10 terms
def recursion(a,b,i,n):
    if i<n:
        c=a+b
        i+=1
        print(c,end=" ")
        recursion(c,a,i,n)
    else:
        return 0
#loop is used to find the nth positioned number in the fibonacci
def loop(n):
    a=0
    b=1
    i=1
    while(i<n):
        c=a+b
        a=b
        b=c
        i+=1
    print(c)
    return(0)

n = int(input("Enter the term number you want to search : "))
print("Sample fibonacci is : ",end="")
recursion(0,1,0,10)
print("\nThe {}th position is: ".format(n),end="")
loop(n)
time.sleep(10)
