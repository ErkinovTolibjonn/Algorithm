def binary_search(array,item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid  = (low + high) //2
        middle = array[mid]
    
        if middle == item:
            return mid
        if middle > item:
            high = mid-1
        else:
            low = mid + 1
    return None
# we must be sort the array ,because function does't find the item in the array
array = ['apple','banana','cherry','orange','berry','raspberry','red apple','green apple']
array.sort()
item = 'orange'

func = binary_search(array,item)
print(func)
print(array)



