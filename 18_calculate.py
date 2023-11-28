import math
def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, raise error:

        >>> calculate('foo', 2, 3)
        Traceback (most recent call last):
          ...
        ValueError: Invalid Operation
    """
    if operation == "add":
        if make_int:
            result = math.floor(a+b)
            return f"{message} {result}"
        else:
            result = a+b
            return f"{message} {result}"
    elif operation == "subtract":
        if make_int:
            result = math.floor(a-b)
            return f"{message} {result}"
        else:
            result = a-b
            return f"{message} {result}"
    elif operation == "multiply":
        if make_int:
            result = math.floor(a*b)
            return f"{message} {result}"
        else:
            result = a*b
            return f"{message} {result}"
    elif operation == "divide":
        if make_int:
            result = a // b
            return f"{message} {result}"
        else:
            result = a / b
            return f"{message} {result}"
    else:
        raise ValueError("Invalid Operation")

    # move the return f here instead of repeating
    # same thing with the make_int at the end to see

    # python has an int() method -> chops off the right of the decimal place