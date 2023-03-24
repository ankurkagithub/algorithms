def recursion_sum(values):
    if not values:
        print("Base case called. Empty List: ", values)
        return 0
    print("Recursion call. Input:", values)
    remaining_sum = recursion_sum(values[1:])
    print(f"Calling to sum {values}, returning {values[0]} + {remaining_sum}")
    sum = values[0] + remaining_sum
    return sum



values_sorted = [1,2,3,4,5,6]
values_unsorted = [45,55,87,1,3,2]
# target = 49
# print(binary_search(values, target))
# print(verify_sorted_recur(values_unsorted))
print(quick_sort(values_unsorted))

# print(recursion_sum(values_sorted))
