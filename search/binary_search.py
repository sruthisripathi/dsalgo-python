def binary_search(input_array, value):
    # Questions to ask
    # 1. Will I get a sorted array or will I have to sort it?
    # 2. If I'm getting a sorted array, is it sorted in ascending order or in descending order?
    # 3. What type elements does the array contain?
    # 4. What to do when you can't find the element? What to return?
    """
    Finds the index of given value in given input array using binary search algorithm
    Args:
        input_array: Array in which value has to be searched for
        value: Value to be searched for
    Returns:
        index of where the given value is. Returns -1 if it's not found
    """
    p = 0
    q = len(input_array) - 1
    while p <= q: 
        # You initially did p<q only. It won't work when there is a sinle element array is left and it has the value
        mid = (p + q) // 2
        if input_array[mid] == value:
            return mid
        if input_array[mid] < value:
            p = mid + 1
        elif input_array[mid] > value:
            q = mid - 1
    return -1

def recursive_binary_search(input_array, value, start, end):
    # Questions to ask
    # 1. Will I get a sorted array or will I have to sort it?
    # 2. If I'm getting a sorted array, is it sorted in ascending order or in descending order?
    # 3. What type elements does the array contain?
    # 4. What to do when you can't find the element? What to return?
    """
    Finds the index of given value in given input array using binary search algorithm
    Args:
        input_array: Array in which value has to be searched for
        value: Value to be searched for
    Returns:
        index of where the given value is. Returns -1 if it's not found
    """
    mid = (start + end) // 2
    if start > end: # Base case 1
        return -1
    if input_array[mid] == value: # Base case 2
        return mid
    if input_array[mid] < value:
        return recursive_binary_search(input_array, value, mid + 1, end)
    if input_array[mid] > value:
        return recursive_binary_search(input_array, value, start, mid - 1)
