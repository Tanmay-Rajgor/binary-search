


def binarySearch(arr, target):

    left = 0
    right = len(arr)-1
    
    while(left<=right):
        mid = (left+right)//2

    if(arr[mid] == target):
        return target
    elif(arr[mid] < target):
        left = mid + 1
    else:
        right = mid - 1
    return -1               



arr = [21,22,23,24,25]
target = 21

result = binarySearch(arr, target)

if result != -1:
    print("Target is present at %d", result)
else:
    print("Target is not present in the array.")    