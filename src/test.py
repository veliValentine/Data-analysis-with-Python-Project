from collections import defaultdict
from itertools import product

import numpy as np
from numpy.random import choice
import re
import pandas as pd

def get_codong_usage_table_as_data_frame():
    #1. We read the whole html page
    try:
        with open('codon_usage_table.html') as f:
            page = f.read()
    except FileNotFoundError:
        with open('src/codon_usage_table.html') as f:
            page = f.read()

    start_index = page.find('<pre>')+5
    end_index = page.find('</pre>')
#2. slice the information off the page (it is between <pre> and </pre> html-attributes)
    data = page[start_index:end_index].strip()
#3. get an array containing information per RNA-triplet. Example after the next line data[0] = UUU F 0.46 17.6 (714298)
    data = re.findall(r'[a-zA-Z]{3}\s[a-zA-Z|*]{1}\s[0-9]*.[0-9]*\s*[0-9]*.[0-9]*\s*\(\s?[0-9]*\)', data)
    # we split the data into 2 dimensional array
    data = [d.replace('( ', '(').split() for d in data]
    #4. put everythin into pandas dataframe
    df = pd.DataFrame(data, columns=['triplet', 'amino acid',  'fraction', 'frequency', 'number'])
    #5 Strip number column from parentheses
    df['number'] = df['number'].apply(lambda s: s[1:-1])
    #6 convert dtypes of fraction and frequency to float and number to int
    df = df.astype({'fraction':float, 'frequency':float, 'number':int})
    return df

get_codong_usage_table_as_data_frame()