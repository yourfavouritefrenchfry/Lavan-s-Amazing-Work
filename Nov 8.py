def all_squares(max_number):
    """
    Return a list of all the squares from 1 to max_number
    >>>all_squares(26)
    [1,4,9,16,25]
    """
    new_list=[]
    for j in range(1,max_number):
        if j*j<=max_number:
            new_list.append(j*j)
    return new_list

def largest(list1):
    """
    Return the largest number in the list
    >>>largest([1,2,3,4])
    4
    """
    for j in range(list1[-1]):
        if j>list1[-1]:
            return j
    return list1[-1]

def remove_duplicates(list2):
    """
    Return a copy of new_list with all the elements of list2 with no duplicates
    >>>remove_duplicates([1,2,2,3,4,3])
    [1,2,3,4]
    """
    new_list=[]
    for e in list2:
        if e not in new_list:
            new_list.append(e)
    return new_list

def common_element(L1,L2):
    """
    Return True if there is at least one common element in both L1 and L2
    >>>common_element([1,2,3],[2,4,6])
    True
    """
    for item in L1:
        if item in L2:
            return True
    return False

def mystery_12(list_of_numbers, upper_limit):
    """
    Return True if upper_limit is greater than or equal to numbers in list_of_numbers
    >>>mystery12([1,2,3,4],3)
    False
    """
    b=True
    for e in list_of_numbers:
        if e>upper_limit:
            b=False
    return b

def items_in_common(List1, List2):
    """
    Return a list of all the common elements from List1 and List2
    >>>items_in_common([1,2,3,4,5,6],[2,4,6,8,10])
    [2,4,6]
    """
    new_list=[]
    for item in List1:
        if item in List2:
            new_list.append(item)
    return new_list

def list_to_string(list4):
    """
    Return a string with all the elements in list4
    >>>list_to_string([2,3,"cow","food"]
    "23cowfood"
    """
    new_string=""
    for item in list4:
        new_string.append(item):
    return new_string


    
    
    


