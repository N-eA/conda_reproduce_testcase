"""
This script tests if the installed packages via conda are properly imported and usable
"""

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

#print(f'Scipy call: {csr_matrix([[1,0,2],[0,3,0]])}')

#print(f'Numpy call: {np.zeros(5)}')

#print(f'Pandas call: {pd.Series(["a","b","c","a"], dtype="category")}')

#print(f'Scipy call: {csr_matrix([[1,0,2],[0,3,0]])}')

#print(f'Numpy call: {np.zeros(5)}')

#print(f'Pandas call: {pd.Series(["a","b","c","a"], dtype="category")}')


def test_scipy():
    values =[[1,0,2],[0,3,0]] 

    matrix = csr_matrix(values).toarray()
    print(matrix)
    