
from .iterable import tally, counts, counts_by
from .indexing import first, last
from .numbertests import even_q, odd_q
from .nesting import nest_while_list, nest_while




#%%

# class up_to(int):
#     pass


# def partition(arr,n):
#     if isinstance(n,up_to):
#         return [arr[n*i:n*i+n] for i in range(int(len(arr) / n) + (len(arr) % n > 0))]
#     else:
#         return [arr[n*i:n*i+n] for i in range(len(arr)//n)]


# partition([1,2,3,4,5], up_to(2))
#%%
    

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





# def delete_duplicates(x):
#     return list(group_by(x,key=lambda x:x).keys())
