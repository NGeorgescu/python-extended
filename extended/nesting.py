def nest_while_list(f,expr,test,m=1,max_iter=None, n=0):
    """
    
    repeatedly applies f to expr until test yields False

    Parameters
    ----------
    f : function
        function to apply each time.
    expr : any
        starting expression.
    test : function
        test to continue applying f.
    m : int, optional
        if int: equivalent to [m,m]; if list: [m_min,m_last], Do the first 
        m_min iterations even if Test is False, and use last m_last as a list 
        for results for test.
    max_iter : int, optional
        iterates a maximum of max_iter number of times. The default is 1024.
    n : int, optional
        applies test n additional times after the completion. The default is 0.

    Returns
    -------
    out : list
        returns list of results for successive applications of f to expr
        
    Examples
    --------
    
    >>> xt.nest_while_list(lambda x:x/2, 123456, xt.even_q)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0]

    >>> xt.nest_while_list(lambda x:x/2, 123456, xt.even_q, m=[7,1], n=1)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0, 964.5, 482.25]

    >>> #The collatz conjecture with 19 as the starting point:
    >>> xt.nest_while_list(lambda x:[x//2,3*x+1][x%2], 19, lambda x: x!=1)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    L = [expr]
    i = 0
    try:
        iter(m)
    except:
        o=m
    else:
        m,o = m
    finally:
        assert isinstance(m,int)
    if max_iter and m:
        assert m < max_iter
    while ((test(*L[-o:]) if o else test(expr)) and
           (i < max_iter if max_iter else True)) or i<m:
        expr = f(expr)
        L.append(expr)
        i += 1
    if n>0:
        for i in range(n):
            expr = f(expr)
            L.append(expr)
    elif n<0:
        L=L[:n]
    return L
    

def nest_while(f,expr,test,m=1,max_iter=None, n=0):
    """
    
    repeatedly applies f to expr until test yields False

    Parameters
    ----------
    f : function
        function to apply each time.
    expr : any
        starting expression.
    test : function
        test to continue applying f.
    m : int, optional
        if int: equivalent to [m,m]; if list: [m_min,m_last], Do the first 
        m_min iterations even if Test is False, and use last m_last as a list 
        for results for test.
    max_iter : int, optional
        iterates a maximum of max_iter number of times. The default is 1024.
    n : int, optional
        applies test n additional times after the completion. The default is 0.

    Returns
    -------
    out : item
        returns results for successive applications of f to expr
        
    Examples
    --------
    
    >>> xt.nest_while(lambda x:x/2, 123456, xt.even_q)
    1929.0

    >>> xt.nest_while_list(lambda x:x/2, 123456, xt.even_q, m=[7,1], n=1)
    482.25

    """
    return nest_while_list(f,expr,test,m=0,max_iter=None, n=0)[-1]
