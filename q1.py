import numpy as np


def normip(v, p):
    """
 function to compute the natural norm of an input vector.
 Inputs: v - a numpy array (n dim vector), p – real number >=1
 Outputs: p norm of v
 """
    return np.sum(np.abs(v)**p)**(1/p)


# a
v = np.array([1, 2 * 1j, -3, 1, 7], dtype='complex')
print("norm 2: ", normip(v, 2), "\nnorm 5: ", normip(v, 5))

# b
v = np.array([1, 5, 3 * 1j, -1 + 1j, 2], dtype='complex')
v_norm = normip(v, 2)
normalize_v = v / v_norm
print("unit vector in direction of v : ", normalize_v)

# c
v = np.array([6, 7, 1j, 2 * 1j, 7])
u = np.array([2, 1, -2 * 1j, -3, 8])
print("distance between v and u is (p=2):", normip(v - u, 2))
print("distance between v and u is (p=3):", normip(v - u, 3))
