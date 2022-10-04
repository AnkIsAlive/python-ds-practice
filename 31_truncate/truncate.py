def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate("Hello World", 6)
        'Hel...'

        >>> truncate("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    # This is a conditional statement that checks if the length of the phrase is less than 3. If it
    # is, it returns a message. If it is not, it checks if the length of the phrase is greater than
    # the length of the phrase plus 2. If it is, it returns the phrase. If it is not, it returns the
    # phrase with the last 3 characters replaced with "...".
    if n < 3:
        return "Must be atleast 3 characters."

    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."
