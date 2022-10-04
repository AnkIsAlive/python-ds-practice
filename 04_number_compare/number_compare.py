def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """

    if a > b:
        return "The first is greater"
    elif b > a:
        return "The second is greater"
    else:
        return "These are equal"
