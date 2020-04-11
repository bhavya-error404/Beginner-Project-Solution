n = int(input())
temp = n
k = 0
while(n>0):
    d = n%10
    k = k*10 + d
    n = n//10
if temp == k:
    print("The given number is palindrome.")
else:
    print("The given number is not palindrome.")
