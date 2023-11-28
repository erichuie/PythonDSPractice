def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # iterate through the phrase, search for the to_swap, swap case

    swapped_phrase = ''

    for char in phrase:
        if to_swap.lower() == char.lower():
            if char.islower():
                swapped_phrase += char.upper()
            else:
                swapped_phrase += char.lower()
        else:
            swapped_phrase += char

    return swapped_phrase
