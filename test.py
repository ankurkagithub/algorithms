def binary_search(values, target):
    left_index = 0
    right_index = len(values) - 1

    # adjust these index values to calculate mid value until target is found
    while left_index <= right_index:
        print(f"left: {left_index}, value: {values[left_index]} ")
        print(f"right: {right_index}, value: {values[right_index]}")
        mid_index = (left_index + right_index) // 2
        print(f"mid: {mid_index} value: {values[mid_index]}")
        if values[mid_index] == target:
            return mid_index
        elif values[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    # otherwise return None
    return -1


test = [1,3,4,5,6,6,7,8,9,10,22,33,44,55,66,77,88,99,222]

print(binary_search(test,22))
