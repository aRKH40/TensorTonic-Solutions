import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    pass
    import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Convert inputs to numpy arrays (handles different sizes automatically)
    real_scores = np.array(real_scores)
    fake_scores = np.array(fake_scores)
    
    # The loss formula is L = E[D(fake)] - E[D(real)]
    # In code, E (expectation) is simply the mean.
    loss = np.mean(fake_scores) - np.mean(real_scores)
    
    return float(loss)