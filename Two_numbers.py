import time
def sum_func(arr,target):
    val = [-1,-1]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                val[0]=i
                val[1]=j
                return val
    return val

arr = list(map(int,input("Enter the array:").split()))
target = int(input("Enter the target value:"))
final_ans = sum_func(arr,target)
print(final_ans)
time.sleep(3)
