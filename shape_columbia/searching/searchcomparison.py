import random
import time

def get_user_input(message, datatype):
    """
    Prompts the user to enter a value of the specified data type until no errors
    occur and a value is obtained.

    Arguments:
    message -- the prompt that is seem by the user
    data type -- the type of data the value is expected to be; either int, float,
    or string


    Returns:
    A value

    """

    while True:
        str_input = input(message).strip()
        try:
            return datatype(str_input)
        except:
            print("Error: Input '"+str_input+"' is not of type " + datatype.__name__ + ".")



def create_list_of_random_ints(length, a, b, sort=False):
    """ Creates a list of random integers
    
    Arguments:
    length  -- the length of the list to create
    a       -- the minimum value in the list
    b       -- the maximum value in the list
    sort    -- whether to sort the list or not, default is False
    
    Returns:
    A list of random integers
    
    """

    random_list = []
    for _ in range(length):
        random_list.append(random.randint(a, b))
    if sort:
        random_list.sort()
    return random_list

def linear_search(lst, key):
    """
    Searches the given list for the given key.

    Arguments:
    lst         --- the list to search
    key         --- the key to search for

    Returns:
         The index of the first occurrence of the given key in the list
         -1 if not found
    """

    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

def binary_search(lst, key):
    """
    Searches the given list for the given key.

    Arguments:
    lst         --- the sorted list to search
    key         --- the key to search for

    Returns:
        An index of the given key in the list, if present,
        else -low-1. THe caller of the function can convert index = -low-1 to a
        nonnegative index indicating where the key should be inserted by using the
        value -ind-1
    """
    low = 0
    high = len(lst)-1
    while high >= low:
        mid = low + (high-low)//2
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -low-1

def main():
    print("---Linear/Binary Search Comparison---")
    list_size = get_user_input("Enter list size: ", int)
    num_keys = get_user_input("Enter number of keys: ", int)
    lst = create_list_of_random_ints(list_size, 0, 1000000, True)
    keys = create_list_of_random_ints(num_keys, 0, 1000000)


    start_time_ = time.perf_counter()

    for key in keys:
        linear_search(lst, key)

    end_time_ = time.perf_counter()

    execution_time = end_time_ - start_time_
    print(f"Execution time: {execution_time:.6f} seconds")

    start_time_ = time.perf_counter()

    for key in keys:
        binary_search(lst, key)

    end_time_ = time.perf_counter()

    execution_time = end_time_ - start_time_
    print(f"Execution time: {execution_time:.6f} seconds")


if __name__ == '__main__':
    main()