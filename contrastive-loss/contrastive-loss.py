import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    pass
    import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)
    y: array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    """
    # Convert inputs to numpy arrays for safety
    a = np.array(a)
    b = np.array(b)
    y = np.array(y)
    
    # 1. Compute Euclidean Distance d_i = ||a_i - b_i||_2
    # axis=-1 handles both (D,) and (N,D) shapes via broadcasting
    distances = np.sqrt(np.sum((a - b)**2, axis=-1))
    
    # 2. Calculate loss components
    # For similar pairs (y=1): loss is d^2
    similar_loss = y * np.square(distances)
    
    # For dissimilar pairs (y=0): loss is max(0, m - d)^2
    dissimilar_loss = (1 - y) * np.square(np.maximum(0, margin - distances))
    
    # 3. Total loss per sample
    total_loss = similar_loss + dissimilar_loss
    
    # 4. Apply reduction
    if reduction == "mean":
        return float(np.mean(total_loss))
    elif reduction == "sum":
        return float(np.sum(total_loss))
    else:
        raise ValueError("reduction must be 'mean' or 'sum'")