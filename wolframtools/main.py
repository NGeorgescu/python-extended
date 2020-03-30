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

#%%
    
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
    iter(expr)
    try:        
        return expr[0]
    except IndexError:
        return defer

def even_q(x):
    return x%2==0

def odd_q(x):
    return x%2==1



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

# def nest_while(arg,fn=lambda x:x,test= lambda x:x,max_iterations=1024,fail='Exception'):
#     i = 0
#     while not test(arg) and i < max_iterations:
#         arg = fn(arg)
#         i += 1
#         if i == max_iterations:
#             if fail =='Exception':
#                 raise Exception('RecursionDepthError: maximum recursion depth reached')
#             else:
#                 return fail
#     return arg

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
