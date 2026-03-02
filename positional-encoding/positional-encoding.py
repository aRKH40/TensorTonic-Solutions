import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pass
    import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    positions = np.arange(seq_len)[:, np.newaxis]          # (seq_len, 1)
    i = np.arange(d_model)[np.newaxis, :]                  # (1, d_model)
    
    # For each dim index, compute the pair index (floor divide by 2)
    pair_idx = (i // 2)                                     # (1, d_model)
    
    angles = positions / (base ** (2 * pair_idx / d_model)) # (seq_len, d_model)
    
    PE = np.where(i % 2 == 0, np.sin(angles), np.cos(angles))
    
    return PE.astype(float)