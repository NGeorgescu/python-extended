
def tally(L):
    D = {}
    for i in L:
        try:
            D[i]+=1
        except:
            D[i]=1
    return {k: v for k, v in sorted(D.items(), key=lambda item: item[1], reverse=True)}

def group_by(x,key=None,return_fn=None):
    d = {}
    for i in x:
        try:
            d[key(i)] += [i]
        except:
            d[key(i)] = [i]
    if return_fn:
        return [[return_fn(i) for i in j] for j in list(d.values())]
    else:
        return d

def gather_by(x, **kwargs):
    return list(group_by(x, **kwargs).values())

def counts_by(x, key=lambda x:x):
    return {k:len(v) for k,v in group_by(x,key=key).items()}

def rotate_right(input_list,n):
    input_list = list(input_list)
    n = -n
    if n ==0:
        return input_list
    else:
        if n<0:
            n = len(input_list)+n
        return input_list[n:]+input_list[:n]

def rotate_left(input_list,n):
    return rotate_right(input_list,-n)
            
def nest(arg,n_times,fn=lambda x:x):
    for n in range(n_times):
        arg = fn(arg)
    return arg

            
def nest_list(arg,n_times,fn=lambda x:x):
    end = []
    for n in range(n_times):
        arg = fn(arg)
        end.append(arg)
    return end

def nest_while(arg,fn=lambda x:x,test= lambda x:x,max_iterations=1024,fail='Exception'):
    i = 0
    while not test(arg) and i < max_iterations:
        arg = fn(arg)
        i += 1
        if i == max_iterations:
            if fail =='Exception':
                raise Exception('RecursionDepthError: maximum recursion depth reached')
            else:
                return fail
    return arg

def nest_while_list(arg,fn=lambda x:x,test= lambda x:x,max_iterations=1024,fail='Exception'):
    i = 0
    end = []
    while not test(arg) and i < max_iterations:
        arg = fn(arg)
        end.append(arg)
        i += 1
        if i == max_iterations:
            if fail =='Exception':
                raise Exception('RecursionDepthError: maximum recursion depth reached')
            else:
                return fail
    return end

def transpose(arr):
    return [[i[j] for i in arr] for j in range(max([len(i) for i in arr]))]


def first(x):
    return x[0]

def last(x):
    return x[-1]

def even_q(x):
    return x%2==0

def odd_q(x):
    return x%2==1



def partition(arr,n,upto=True):
    if upto:
        return [arr[n*i:n*i+n] for i in range(int(len(arr) / n) + (len(arr) % n > 0))]
    else:
        return [arr[n*i:n*i+n] for i in range(len(arr)//n)]


def delete_duplicates(x):
    return list(group_by(x,key=lambda x:x).keys())
