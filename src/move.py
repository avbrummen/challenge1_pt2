import pandas as pd
import numpy as np

def vector_hash(vector):
    """returns the hash of a vector using pandas

    Parameters
    ----------
    vector : array-like
        A vector or series of numbers
  
    Returns
    -------
    hash array
        Honestly don't really know what this is besides that it is a pandas function
    
    """

    hash = pd.util.hash_array(vector, encoding='utf8', hash_key='0123456789123456', categorize=True)

    return hash

if __name__ == "__main__":
    vector_hash(np.array([1, 2, 3]))
