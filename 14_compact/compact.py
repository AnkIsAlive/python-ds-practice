def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # It's a list comprehension. It's a compact way of writing a for loop that appends to a list.
    return [val for val in lst if val]
