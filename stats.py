'''
'''
from functools import reduce
def get_col_max(col):
    '''
    Docstring for get_col_max
    
    :param col: Description
    '''
    clean = [value for value in col if value is not None ]

    if not clean:
        return None
    
    max_val = reduce(lambda mx, x: x if x > mx else mx, clean, clean[0] )
    return max_val


def get_col_min(col):
    '''
    Docstring for get_col_min
    
    :param col: Description
    '''
    clean = [value for value in col if value is not None ]

    if not clean:
        return None
    
    min_val = reduce(lambda mn, x: x if x < mn else mn, clean, clean[0] )
    return min_val

def get_col_mean(col):
    '''
    Docstring for get_col_mean
    
    :param col: Description
    '''
    clean = [value for value in col if value is not None ]

    if not clean:
        return None
    
    sm, cnt = reduce(lambda acc, x: 
                                (acc[0]+x, acc[1]+1),
                                clean,
                                (0,0)
                                    )
    return sm/cnt

def get_col_median(col):
    '''
    Docstring for get_col_median
    
    :param col: Description
    '''
    clean = [value for value in col if value is not None ]
    if not clean:
        return None
    
    clean.sort()
    col_cnt = len(clean)
    med = col_cnt//2

    if col_cnt%2 == 0:
        median = (clean[med] + clean[med-1])/2
    else:
        median = (clean[med])

    return median
    
def get_col_mode(col):
    '''
    Docstring for get_col_mode
    
    :param col: Description
    '''
    clean = [value for value in col if value is not None ]
    if not clean:
        return None
    
    freq = {}

    for x in clean:
        freq[x] = freq.get(x, 0) + 1


    mode = reduce(lambda md, x: x if freq[x] > freq[md] else md, freq, clean[0])
    return mode

def get_stat(data : dict, dtype: dict, func = get_col_mode ):
    '''
    Docstring for get_stat
    
    :param data: Description
    :type data: dict
    :param dtype: Description
    :type dtype: dict
    :param func: Description
    :type func: function
    '''
    stats = {}
    cols = list(data.keys())
    for key in cols:
        if dtype[key] == "string":
            stats[key] = None
        else:
            stats[key] = func(data[key])

    return stats

    
