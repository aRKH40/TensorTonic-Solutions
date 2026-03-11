import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    pass
    import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    
    # 1. Numerical Stability: Subtract the max across the last axis
    # keepdims=True is vital for 2D arrays to subtract row-wise correctly
    z = x - np.max(x, axis=-1, keepdims=True)
    
    # 2. Exponentiate the stabilized values
    exp_z = np.exp(z)
    
    # 3. Divide by the sum across the last axis
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)