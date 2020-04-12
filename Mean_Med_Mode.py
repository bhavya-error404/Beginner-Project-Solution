#function for mean
def mean(n,length):
    r = int(input("Enter the number of decimal places to be rounded off for the mean: "))
    Sum = sum(n)
    print("Mean is:",round(Sum/length , r))
    return()

#Function for meadian
def median(n,length):
    print("Median is:",end=" ")
    n.sort()
    if length%2 == 0:
        print(n[(length//2)-1],end=" ")
        print(n[(length//2)])
    else :
        print(n[length//2])

#function for mode
def mode(n):
    print("Mode is:",end=" ")
    freq = {}
    
#Calculating frequencies
    
    for i in n:
        if i in freq:
            freq[i] += 1
        else :
            freq[i] = 1
    x = freq.values()
    max_value = max(x)
    
#Printing Mode
    
    for i,j in freq.items():
        if j == max_value:
            print(i,end = " ")



#driving code
n = list(map(int,input("Enter the numbers in a row:").split()))
length = len(n)

mean(n,length)
median(n,length)
mode(n)



