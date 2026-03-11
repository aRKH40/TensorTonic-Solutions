import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    pass
    import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Convert input to a numpy array (handles scalars, lists, or arrays)
    x = np.array(x)
    
    # Fully vectorized: return the maximum of 0 and x for each element
    return np.maximum(0, x)