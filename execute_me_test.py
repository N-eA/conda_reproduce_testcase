"""
This script tests if the installed packages via conda are properly imported and usable
"""

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

"""
This testscript creates some vanilla test examples by using the imported libraries, the goal is to
see all of the tests passing when migrating/recreating conda on different distributions
"""

def test_scipy():
    values = np.array([[1,0,2],[0,3,0]])
    expected_val = values
    ret_val = csr_matrix(values).toarray()
    # Nested arrays thus comparing only first elements for PoC
    assert all([a[0] == b[0] for a,b in zip(ret_val,expected_val)])

def test_numpy():
    expected_val =  [0., 0., 0., 0., 0.]
    ret_val = np.zeros(5)
    assert all([a == b for a,b in zip(ret_val,expected_val)])

def test_pandas():
    ages = pd.Series([22, 35, 58], name="Age")
    ret_val = ages.max()

    assert ret_val == 58