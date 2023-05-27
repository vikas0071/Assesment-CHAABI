# Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def get_every_other_sublist(lst, start, end):
    return lst[start:end+1:2]
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

sub_list = get_every_other_sublist(input_list, start_index, end_index)
print(sub_list)
