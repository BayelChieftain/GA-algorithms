
def sum(arr):

    total = 0
    for x in arr:
        total += x
    return total

print(sum([23,1,4,3,7,9,56,6]))

def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return qsort(less) + [pivot] + qsort(greater)

print(qsort([10,5,2,3,34,23,4,44,33]))
