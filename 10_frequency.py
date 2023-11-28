def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    term_frequency = 0

    for num in lst:
        if num == search_term:
            term_frequency += 1

    return term_frequency