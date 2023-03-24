def binary_search(data,target):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1


values_sorted = [1,2,3,4,5,6]
values_unsorted = [45,55,87,1,3,2]
# target = 49
# print(binary_search(values, target))
# print(verify_sorted_recur(values_unsorted))
print(quick_sort(values_unsorted))

# print(recursion_sum(values_sorted))
