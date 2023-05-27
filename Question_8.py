# Some neat tricks up her sleeve:
# Looking at the below code, write down the final values of A0, A1, ...An
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# A8 = map(lambda x: x*2, [1,2,3,4])
# A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

from functools import reduce

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# A0 is a dictionary created by zipping keys and values together
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
# A1 is a range object representing numbers from 0 to 9

A2 = sorted([i for i in A1 if i in A0])
# A2 is a sorted list comprehension that includes elements from A1 if they are present in A0
# In this case, A0 does not contain any elements from A1, so A2 is an empty list

A3 = sorted([A0[s] for s in A0])
# A3 is a sorted list comprehension that retrieves values from A0 based on its keys
# The values are sorted in ascending order
# [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
# A4 is a list comprehension that includes elements from A1 if they are present in A3
# Since A3 contains the values 1 to 5, which are all present in A1, A4 will include all elements of A1
# [1, 2, 3, 4, 5]

A5 = {i: i * i for i in A1}
# A5 is a dictionary comprehension that creates a dictionary with keys as elements from A1
# and values as the square of each element
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i, i * i] for i in A1]
# A6 is a list comprehension that creates a list of lists
# Each inner list contains an element from A1 and its square
# [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

A7 = reduce(lambda x, y: x + y, [10, 23, -45, 33])
# A7 is the result of applying the lambda function to the list using the reduce() function
# The lambda function sums all the elements in the list
# 21

A8 = list(map(lambda x: x * 2, [1, 2, 3, 4]))
# A8 is a list created by applying the lambda function to each element of the list using the map() function
# The lambda function doubles each element
# [2, 4, 6, 8]

A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))
# A9 is a list created by applying the lambda function to each element of the list using the filter() function
# The lambda function checks if the length of each string is greater than 3
# The resulting list includes only the strings with a length greater than 3
# ['want', 'learn', 'python']
