n = int(input("Enter the number:"))
length = len(str(n))
k = 0
temp = n
while(n>0):
    a = n%10
    k = k + pow(a,length)
    n = n//10

if temp == k:
    print(" The given number is an armstrong number.")
else :
    print(" The given number is not an armstrong number.")
