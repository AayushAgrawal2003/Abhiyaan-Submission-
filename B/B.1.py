import sys
r = [int(x) for x in sys.stdin.readline().split()]
m = r[0]
n = r[1]
k = int(input())

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
arr = []
for i in range(m):
    arr += [int(x) for x in sys.stdin.readline().split()]
    
result = binarySearch(arr, 0, len(arr)-1, k)
result += 1 

if result != 0:
    print(True)
    if result%n == 0:
        print(result//n -1,n,sep = " ")
    else:
        print(result//n ,(result%n)-1,sep = " ")
else:
    print("False")







    





