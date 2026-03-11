import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Convert inputs to numpy arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Use advanced indexing to grab the probability of the correct labels
    # np.arange(len(y_true)) gives row indices [0, 1, 2...]
    # y_true gives the column indices for the correct classes
    correct_probs = y_pred[np.arange(len(y_true)), y_true]
    
    # Calculate the mean of the negative log probabilities
    loss = -np.mean(np.log(correct_probs))
    
    return loss