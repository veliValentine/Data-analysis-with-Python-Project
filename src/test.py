from collections import defaultdict
from itertools import product

import numpy as np
from numpy.random import choice
import re
import pandas as pd

# python
import pandas as pd
from statistics import stdev, variance
from math import sqrt
from scipy.stats import norm

def context_list(s, k):
    dic = dict()
    for start_i in range(len(s)-k + 1):
        substring = s[start_i:start_i+k+1]
        l = len(substring)
        if(l>k):
            key, value = substring[0:-1], substring[-1]
            print(substring, key, value)
            if(key not in dic.keys()):
                dic[key] = value
            else:
                dic[key] = dic[key] + value
    return dic

if __name__ == '__main__':
    k = 2
    s = 'TAGCGTATAATGTGGGAGTGTCTGCTGCCACCGGTGCTTACAGTTAGGCGTCTAGCCATGAAACTCCCGGAATCGGCAAAACATATTGGTCAAACTCACC'
    v = 'TGTGGAGGCGTCCTTCGAAGTCTGCAAGGCATTGTCCCAGAAGCGTATACTATACAGAAAGACCTTGCGTCACTGGTACCGTACGGTCATATC'
    #C     CA 2    AA 3  CC 1 
    # TA 1 AG 2 GG 2 CT 2 AT 1 GT 3 TC 1 TG 3 GC 2 AC 2 
    #print(s)
    #s = 'ATGATATCATCGACGATCTAG'
    d = context_list(s, 2)
    sum = 0
    
    for key in d.keys():
        print(key, d[key], len(d[key]))
        sum += len(d[key])
    print('sum', sum)

    s_dic = dict()
    for c in s:
        if(c not in s_dic.keys()):
            s_dic[c] = 0
        s_dic[c] = s_dic[c] + 1
    #print(s_dic)
    s_dic = dict()
    for c in v:
        if(c not in s_dic.keys()):
            s_dic[c] = 0
        s_dic[c] = s_dic[c] + 1
    #print(s_dic)
    #{'T': 24, 'A': 26, 'G': 25, 'C': 25}
    #{'T': 23, 'G': 24, 'A': 23, 'C': 23}