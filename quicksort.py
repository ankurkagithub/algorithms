def quick_sort(values):
    if len(values) <= 1:
        return values
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for value in values[1:]:   #<- there is where the recursion is reducing the size of input
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



values_sorted = [1,2,3,4,5,6]
values_unsorted = [45,55,87,1,3,2]
# target = 49
# print(binary_search(values, target))
# print(verify_sorted_recur(values_unsorted))
print(quick_sort(values_unsorted))

# print(recursion_sum(values_sorted))
