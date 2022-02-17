import numpy as np
from scipy.spatial.distance import cosine

# data to be hashed
x = np.array([3,4,5,6])
y = np.array([4,3,2,1])

# random hyperplanes
z1 = np.array([0.16,-0.26,-1.12,0.01])
z2 = np.array([1.08, -1.14, 0.8, -0.8])
z3 = np.array([1.94, 0.08, 1.83, 0.17])
z4 = np.array([-0.88, -1.01, 1.36, -0.07])

def h(x, z):
    """
    Hashing function that returns binary output.
    
    """
    return 1 if np.dot(x, z) >= 0 else 0

def hamming_dist(x, y):
    """
    Compute the hamming distance between two binary vectors.
    
    """
    return np.sum(np.where(x != y))

def hash_data(x, z_lst):
    """
    Generate hashed data based on locality-sensitive hashing.

    params:
        x: a vector to be hashed
        z_lst: a list of hyperplanes
    return:
        hashed_x: hashed vector

    """
    b = len(z_lst)
    hashed_x = np.zeros(b)
    for i, z in enumerate(z_lst):
        hashed_x[i] = h(x, z)
    return hashed_x

def err(x, y, z_lst):
    """
    Compute the error of the result, defined as |1 - cos(h/b*pi) - d_cos(x,y)|
        h is the hamming distance between x_hashed and y_hashed
        b is the number of hyperplanes used

    """
    x_hashed = hash_data(x, z_lst)
    y_hashed = hash_data(y, z_lst)
    b = len(z_lst)
    h = hamming_dist(x_hashed, y_hashed)
    return np.abs(1 - np.cos(h / b * np.pi) - cosine(x, y))

z_lst = [z1, z2, z3, z4]
print(err(x, y, [z1]))
print(err(x, y, z_lst))
      
        
