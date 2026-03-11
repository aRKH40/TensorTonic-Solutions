import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    pass
    import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape
    
    # Calculate output dimensions (Valid padding: H_out = H - KH + 1)
    H_out = H - KH + 1
    W_out = W_in - KW + 1
    
    # Initialize output array
    y = np.zeros((N, C_out, H_out, W_out))
    
    # Loop over each sample in the batch
    for n in range(N):
        # Loop over each output channel (filter)
        for cout in range(C_out):
            # Loop over each input channel
            for cin in range(C_in):
                # Spatial convolution
                for i in range(H_out):
                    for j in range(W_out):
                        # Extract patch and multiply by kernel
                        patch = x[n, cin, i:i+KH, j:j+KW]
                        y[n, cout, i, j] += np.sum(patch * W[cout, cin])
            
            # Add bias for the current output channel
            y[n, cout] += b[cout]
            
    return y