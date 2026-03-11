import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    pass
    import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Convert to numpy arrays to ensure vectorized operations
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)
    
    # Step 1: Accumulate squared gradients
    # G_t = G_{t-1} + g_t^2
    new_G = G + np.square(g)
    
    # Step 2: Parameter Update
    # w_t = w_{t-1} - (lr / sqrt(new_G + eps)) * g_t
    new_w = w - (lr / (np.sqrt(new_G + eps))) * g
    
    return new_w, new_G