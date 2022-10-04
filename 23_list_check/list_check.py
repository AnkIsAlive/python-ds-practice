def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # Iterating through the list and checking if each item is a list. If it is not a list, it returns
    # False. If it is a list, it returns True.
    for item in lst:
        if not isinstance(item, list):
            return False

    return True
