import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    pass
    import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Convert input to a numpy array for consistency
    x = np.array(x)
    
    # Apply the formula: x if x >= 0, else alpha * x
    # np.where(condition, value_if_true, value_if_false) is highly efficient
    return np.where(x >= 0, x, alpha * x)