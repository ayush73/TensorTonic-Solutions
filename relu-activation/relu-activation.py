import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    
    gm = np.asarray(x)
    ans = 0
    size = len(gm.flat)

    for i in range(0, size):
        if gm.flat[i] < 0: 
            gm.flat[i] = 0

    return gm