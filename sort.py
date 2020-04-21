from random import random

def swap(array, left, right):
    array[left] = array[left]^array[right]
    array[right] = array[left]^array[right]
    array[left] = array[left]^array[right]


def merge_sort(array, left, size, depth):
    if (size % 2) == 0:
        mid_point = int(size / 2) + left
        left_size = right_size = int(size / 2)
    else:
        mid_point = int(size / 2) + left + 1
        left_size = int(size / 2) + 1
        right_size = int(size / 2)
    # print(f'merge_sort... size: {size} left_size:{left_size} right_size:{right_size} left:{left}')

    if size == 2:
        if array[left] > array[left+1]:
            #swap em
            swap(array, left, left+1)
        # print(f'leaf: {array[left]}, {array[left+1]}')
        return # left, right
    elif size == 1:
        # print(f'leaf: {array[left]}')
        return # left, right

    # print(f'recursing left:{left}...{left_size} right:{mid_point}...{right_size}')
    merge_sort(array, left, left_size, depth + 1)
    merge_sort(array, mid_point, right_size, depth + 1)

    merge_index = 0
    left_index = left
    right_index = mid_point
    merge_array = list(array[left: left + size])
    # print(f'merging: left: {array[left: left + left_size]} right:{array[mid_point: mid_point+right_size]}')
    while merge_index < len(merge_array):
        # print(f'   merge_index:{merge_index} left_index:{left_index} right_index:{right_index}')
        if left_index >= mid_point:
            # print(f'... adding  array[right_index]:{array[right_index]} exhausted left_index')
            merge_array[merge_index] = array[right_index]
            right_index+=1
        elif right_index >= left + size:
            # print(f'... adding  array[left_index]:{array[left_index]} exhausted right_index')
            merge_array[merge_index] = array[left_index]
            left_index+=1 
        elif left_index < mid_point and array[left_index] < array[right_index]:
            # print(f'... adding  array[left_index]:{array[left_index]}')
            merge_array[merge_index] = array[left_index]
            left_index+=1 
        else:
            # print(f'... adding  array[right_index]:{array[right_index]}')
            merge_array[merge_index] = array[right_index]
            right_index+=1
        merge_index+=1

    # print(f'merge_array: {merge_array}')
    array[left: left + size] = merge_array    
            
        

    


def quick_sort(array, left_i, right_i):
    # choose pivot to be in the middle of left and right
    pivot = int((left_i + right_i) / 2)
    pivot_val = array[pivot]

    # print(f'array before: {array[left_i:right_i+1]}')
    # print(f'array before: {array}')

    i = left_i
    while i < pivot:
        # print(f'array i:{i} pivot:{pivot} pivot_val: {pivot_val} consider left: {array}')
        val = array[i]
        if val > pivot_val:
            for j in range(i, pivot):
                array[j] = array[j+1]
            array[pivot] = val
            pivot-=1
            array[pivot] = pivot_val
        else:
            i+=1
    i = pivot + 1
    while i <= right_i:
        # print(f'array i:{i} pivot_val: {pivot_val} consider right: {array}')
        val = array[i]
        if val < pivot_val:
            array[pivot] = val
            for j in range(i, pivot, -1):
                array[j] = array[j-1]   
            pivot+=1
            array[pivot] = pivot_val
        i+=1

    # print(f'recurse array pivot:{pivot} if {pivot - 1} > {left_i} left_i:{left_i} {array}')
    if (pivot - 1) > left_i:
        quick_sort(array, left_i, pivot-1)
    # print(f'recurse array pivot:{pivot} if {pivot + 1} < {right_i} right_i:{right_i} {array}')
    if (pivot + 1) < right_i:
        quick_sort(array, pivot + 1, right_i)




for i in range(0,255):
    array1 = [int(random()*1000) for j in range(0,255)]
    # array1 = list([5, 7, 8, 2, 3, 10, 11, 3, 4])
    array2 = list(array1)
    # print(f'ARRAY SUM BEFORE: {sum(array1)}')
    print(f'quick_sort... {array1}')
    quick_sort(array1, 0, len(array1) - 1)
    print(array1)
    # print(f'ARRAY SUM AFTER: {sum(array1)}')
    
    # print(f'MERGE SORT ARRAY SUM BEFORE: {sum(array2)} {array2}')
    print(f'merge_sort... {array2}')
    merge_sort(array2, 0, len(array2), 0)
    print(array2)
    # print(f'MERGE SORT ARRAY SUM AFTER: {sum(array2)} {array2}')
    assert(array1 == array2)
