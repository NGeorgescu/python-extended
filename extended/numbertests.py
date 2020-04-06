
def even_q(expr):
    """
    Returns True if number is even else returns False

    Parameters
    ----------
    expr : numeric
        number to be tested

    Returns
    -------
    bool
        True if divisible by 2, False otherwise.

    Examples
    --------
    >>> even_q(2)
    True    

    >>> even_q(1)
    False
    
    >>> # a departure from wolfram, even_q works for floats 
    >>> even_q(2.0)
    True
    
    >>> # even_q works for non-integer numbers, returns false
    >>> even_q(0.4)
    False

    """
    assert float(expr)
    return expr%2==0


def odd_q(expr):
    """
    Returns True if number is odd else returns False

    Parameters
    ----------
    expr : numeric
        number to be tested

    Returns
    -------
    bool
        True if expr+1 is divisible by 2, False otherwise.

    Examples
    --------
    >>> odd_q(1)
    True    

    >>> odd_q(2)
    False
    
    >>> # a departure from wolfram, odd_q works for floats 
    >>> odd_q(1.0)
    True
    
    >>> # odd_q works for non-integer numbers, returns false
    >>> odd_q(0.4)
    False

    """
    assert float(expr)
    return expr%2==1
