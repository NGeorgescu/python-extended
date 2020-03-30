def tally(expr, test=lambda x:x):
    """
    tallies all items in expr using test as the criteria.  The default test is none; just
    tally the items in the list.

    Parameters
    ----------
    expr : list
        list of items to be tallied
    test : function
        test to be applied to each item to determine if the items are tallied together
    
    Returns
    -------
    list
        list of lists with the items tallied up.  If you use a nested list,
        the items get returned as a tuple.  If you use a dictionary, you'll
        only get the keys.  
    
    Examples
    --------
    >>> wl.tally(['a','a','b','a','c','b','a'])
    [['a', 4], ['b', 2], ['c', 1]]
    
    >>> # you can use objects as tallied items
    >>> import sympy as sp
    >>> sp.var('a b c')
    >>> wl.tally([a,a,b,a,c,b,a])
    [[a, 4], [b, 2], [c, 1]]
    
    >>> # if you nest in a list, it gets returned as a tuple
    >>> wl.tally([[1,2],[3,4],[3,4]])
    [[(1, 2), 1], [(3, 4), 2]]

    >>> # numpy arrays behave just like lists
    >>> wl.tally([np.array([1,2]),np.array([3,4]),np.array([1,2])])
    [[(1, 2), 2], [(3, 4), 1]]
        
    
    >>> # tests of items return just the 
    >>> wl.tally([[1,2],[2,3],[1,2],[1,1]],test=wl.first)
    [[[1, 2], 3], [[2, 3], 1]]
    
    >>> # it's not recommended to use on dicts or sets or other unordered collections
    >>> # since the order upon exit cannot be guaranteed. Turn these into lists first
    >>>  tally([{'a','b','c'}])
    [[('b', 'c', 'a'), 1]]
    """

    D = {} #stores the tallies
    E = {} #stores the test definitions
    for i in expr:
        try:
            try:
                D[test(i)]+=1
            except KeyError:
                E[test(i)] = i
                D[test(i)] = 1           
        except TypeError: #it's an unhashable
            i=tuple(i)            
            try:
                D[test(i)]+=1
            except KeyError:
                E[test(i)] = i
                D[test(i)] = 1           
    return [[E[k],v] for k,v in D.items()]


def first(expr, defer=None):
    """
    returns the first item from the collection

    Parameters
    ----------
    expr : iterable
        the list
    defer : any type, optional
        what is returned when nothing is provided in the iterable. The default is None.

    Returns
    -------
    item
        first item in the array

    Examples
    --------
    >>> first(['a','b'])
    'a'
    
    >>> first([])
    None

    """
    iter(expr)
    try:        
        return expr[0]
    except IndexError:
        return defer


def last(expr, defer=None):
    """
    returns the last item from the collection

    Parameters
    ----------
    expr : iterable
        the list
    defer : any type, optional
        what is returned when nothing is provided in the iterable. The default is None.

    Returns
    -------
    item
        last item in the array

    Examples
    --------
    >>> last(['a','b'])
    'b'
    
    >>> first([])
    None

    """
    iter(expr)
    try:        
        return expr[-1]
    except IndexError:
        return defer
        
    


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
#%%


def nest_while_list(f,expr,test,m=0,max_iter=None, n=0):
    """
    
    repeatedly applies f to expr until test yields False

    Parameters
    ----------
    f : function
        function to apply each time.
    expr : any
        starting expression.
    test : function
        test to continue.
    m : int, optional
        Do the first m iterations even if Test is False. The default is 0.
    max_iter : int, optional
        iterates a maximum of max_iter number of times. The default is 1024.
    n : int, optional
        applies test n additional times after the completion. The default is 0.


    Returns
    -------
    list
        returns list of results for successive applications of f to expr
        
        
    Examples
    --------
    
    >>> nest_while_list(lambda x:x/2, 123456, wl.even_q)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0]

    >>> nest_while_list(lambda x:x/2, 123456, wl.even_q, m=7)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0, 964.5]

    >>> nest_while_list(lambda x:x/2, 123456, wl.even_q, m=7, n=1)
    [123456, 61728.0, 30864.0, 15432.0, 7716.0, 3858.0, 1929.0, 964.5, 482.25]

    """
    L = [expr]
    i = 0
    if max_iter and m:
        assert m < max_iter
    while (test(expr) and (i < max_iter if max_iter else True)) or i<m:
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




#%%



    
# counts

# def group_by(x,key=None,return_fn=None):
#     d = {}
#     for i in x:
#         try:
#             d[key(i)] += [i]
#         except:
#             d[key(i)] = [i]
#     if return_fn:
#         return [[return_fn(i) for i in j] for j in list(d.values())]
#     else:
#         return d

# def gather_by(x, **kwargs):
#     return list(group_by(x, **kwargs).values())

# def counts_by(x, key=lambda x:x):
#     return {k:len(v) for k,v in group_by(x,key=key).items()}

# def rotate_right(input_list,n):
#     input_list = list(input_list)
#     n = -n
#     if n ==0:
#         return input_list
#     else:
#         if n<0:
#             n = len(input_list)+n
#         return input_list[n:]+input_list[:n]

# def rotate_left(input_list,n):
#     return rotate_right(input_list,-n)
            
# def nest(arg,n_times,fn=lambda x:x):
#     for n in range(n_times):
#         arg = fn(arg)
#     return arg

            
# def nest_list(arg,n_times,fn=lambda x:x):
#     end = []
#     for n in range(n_times):
#         arg = fn(arg)
#         end.append(arg)
#     return end

# def nest_while_list(arg,fn=lambda x:x,test= lambda x:x,max_iterations=1024,fail='Exception'):
#     i = 0
#     end = []
#     while not test(arg) and i < max_iterations:
#         arg = fn(arg)
#         end.append(arg)
#         i += 1
#         if i == max_iterations:
#             if fail =='Exception':
#                 raise Exception('RecursionDepthError: maximum recursion depth reached')
#             else:
#                 return fail
#     return end

# def transpose(arr):
#     return [[i[j] for i in arr] for j in range(max([len(i) for i in arr]))]





# def partition(arr,n,upto=True):
#     if upto:
#         return [arr[n*i:n*i+n] for i in range(int(len(arr) / n) + (len(arr) % n > 0))]
#     else:
#         return [arr[n*i:n*i+n] for i in range(len(arr)//n)]


# def delete_duplicates(x):
#     return list(group_by(x,key=lambda x:x).keys())
