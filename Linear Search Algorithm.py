def linearSearch_largest(arr, low, high): 
    max = arr[low] 
    i = low 
    for i in range(high+1): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
arr = []
for i in range(10):
    inp=input("Enter a digit: ")
    arr.append(inp)
    print(arr)
    
n = len(arr) 
print ("The largest item is %s"% 
        linearSearch_largest(arr, 0, n-1)) 
