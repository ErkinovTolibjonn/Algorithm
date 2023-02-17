# This to the function use enumerate function to find the index of the element item
def linear_search(array,item):
    for i,idx in enumerate(array):
        if idx == item :
            return i
        else:
            continue
array = ['apple','banana','chery','orange','bery']
item = 'apple'
func = linear_search(array,item)
print(func)

# This to the function use range function to find the index of the item

def linear_search(array,item):
    for i in range(len(array)):
        if array[i] == item:
            return i
        else:
            continue
func = linear_search(array,item)
print(func)