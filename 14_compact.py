def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    true_lst = [truthy for truthy in lst if truthy] # val would work better for truthy since we are not sure if everything is truthy

    return true_lst