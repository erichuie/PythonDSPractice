def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    counter = 0
    for char in word:
        if(char.lower() == letter.lower()):
            counter += 1
    return counter

# look up count method in py

# word.lower().count(letter.lower())
