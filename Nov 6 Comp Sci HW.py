>>> def every_other_new(list1):
	"""
	Return list with every other element of list1 starting with the first
	>>>every_other_new([5,"pencil", "book", 5])
	[5, "book"]
	"""
	return list1[::2]

>>> def every_other_modify(list2):
	"""
	Modify list2 so that every other element starting with the first is removed
	>>>list2=[1,2,3,6]
	>>>every_other_modify(list2)
	>>>list2
	[2,6]
	"""
	for item in list2[::2]:
		list2.remove(item)

		
>>> def sum_of_even(list3):
	"""
	Return sum of all even numbers in list3
	>>>sum_of_even([1,2,3,4])
	6
	"""
	r=0
	for i in list3:
		if i%2==0:
			r=r+i
	return r

>>> def collect_strings(list4):
	"""
	Return a list containing the strings from list4
	>>>collect_strings(["book", "five", 5, "phone"]
	["book", "five", "phone"]
	"""
	s=""
	for item in list4:
		if type(item)==str:
			s=s+item
	return s

>>> def count_int(list5):
        """
        Return the number of integers in list5
        >>>count_int([4,2,"book", 6])
        3
        """
        num=0
        for i in list5:
                if type(i)== int:
                        num=num+1
        return num

>>> def remove_strings_modify(list6):
        """
        Modify list6 so it does not contain strings
        >>>lis=[5, "goat", 4, "lemonade"]
        >>>remove_string_modify(lis)
        >>>lis
        [5,4]
        """
        for i in list6:
                if type(i)==str:
                        list6.remove(i)
                        
