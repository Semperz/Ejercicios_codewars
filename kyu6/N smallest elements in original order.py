#Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number n of smallest elements to return.

#Also:

#-the number of elements to be returned cannot be higher than the array/list/vector length;
#-elements can be duplicated;
#-in case of duplicates, just return them according to the original order (see third example for more clarity).


def first_n_smallest(arr ,n):
    smaller_number = []
    final_list = []
    for number in range(n):
        smaller_number.append(sorted(arr)[number])
    for position in range(len(arr)):
        if len(final_list) <= n - 1:
            if arr[position] in smaller_number:
                final_list.append(arr[position])
                smaller_number.remove(arr[position])
    return final_list