def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2, 2, 2, 100])
        2
    """
    number_frequency = {}
    curr_highest_frequency = 0
    curr_most_common_num = 0
    # number_frequency.get(1,0)
    for num in nums:
        if num in number_frequency:
            number_frequency[num] += 1
        else:
            number_frequency[num] = 1

    for key in number_frequency: #using max here will accomplish the same thing
        if number_frequency[key] > curr_highest_frequency:
            curr_highest_frequency = number_frequency[key]
            curr_most_common_num = key

    return curr_most_common_num

# https://www.w3schools.com/python/ref_dictionary_get.asp
# implementing more python methods:  using max function