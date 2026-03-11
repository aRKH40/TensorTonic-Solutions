import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    pass
    import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Ensure inputs are numpy arrays
    p = np.array(p)
    q = np.array(q)
    
    # 1. Add epsilon to q to prevent division by zero or log(0)
    q_stable = q + eps
    
    # 2. Compute KL Divergence: sum(P * log(P / Q_stable))
    # We use np.where to handle cases where p_i = 0
    # Because lim_{p->0} p * log(p) = 0, these elements contribute 0 to the sum.
    mask = p > 0
    kl_div = np.sum(p[mask] * np.log(p[mask] / q_stable[mask]))
    
    return float(kl_div)