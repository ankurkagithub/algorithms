def merge_sort(alist):
    '''
    this takes an unsorted list of values and returns a sorted list in asceding
    order.
    '''
    if len(alist) <= 1:
        return alist

    # Divide the problem
    left_list, right_list = split(alist)

    # Conquer the problem
    left_sort = merge_sort(left_list)
    right_sort = merge_sort(right_list)

    # Combine
    return merge(left_sort,right_sort)



def split(alist):
    '''
    This function takes input of list data type and splits the list half and
    and returns left and right halves
    Halves are equal weights if even number otherwise not.
    '''
    middle_index = len(alist) // 2
    left_alist = alist[:middle_index]
    right_alist = alist[middle_index:]
    return left_alist,right_alist

def merge(left_list,right_list):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1
    sorted_list += left_list[i:]
    sorted_list += right_list[j:]

    return sorted_list


alist = [2,3,4,5,100,456,34,2356,456,78,98,34,12,34,98,34,65]
print(merge_sort(alist))
