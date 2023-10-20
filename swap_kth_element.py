def swapKth(arr, n, k):
   arr[k-1], arr[-k] = arr[-k], arr[k-1]
   return(arr)
arr=[1,2,3,4,5,6,7,8]
n=len(arr)
k=3
print(swapKth(arr,n,k))
   
