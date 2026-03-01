import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    pass
    import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    N = len(seqs)
    if N == 0:
        return np.empty((0, 0), dtype=int)
    
    L = max_len if max_len is not None else max(len(seq) for seq in seqs)
    
    result = np.full((N, L), pad_value, dtype=int)
    
    for i, seq in enumerate(seqs):
        trunc = seq[:L]  # truncate if longer than L
        result[i, :len(trunc)] = trunc
    
    return result