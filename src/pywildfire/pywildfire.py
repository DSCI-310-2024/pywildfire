import pandas as pd
import numpy as np

def calculate_rmse(observed, predicted):
    ### STILL MISSING DOCSTRING
    """
    ...

    Parameters:
    ----------
    observed: ...
        ...
    predicted: ...
        ...

    Returns:
    -------
    float
        ...

    Raises:
    -------
    ValueError
        ...
    
    Examples
    --------
    >>> ...
    """
    # Check for empty inputs
    if isinstance(observed, (list, tuple, np.ndarray, pd.Series)) and isinstance(predicted, (list, tuple, np.ndarray, pd.Series)):
        if len(observed) == 0 or len(predicted) == 0:
            raise ValueError("Inputs cannot be empty")
    
    # Check if observed and predicted have the same size
        if len(observed) != len(predicted):
            raise ValueError('Inputs must be the same size')
        # Convert inputs to NumPy arrays
        observed = np.array(observed)
        predicted = np.array(predicted)

        # Calculate squared differences
        squared_diff = np.square(observed - predicted)

        # Calculate mean of squared differences
        mean_squared_diff = np.mean(squared_diff)

        # Calculate square root of mean squared differences to get RMSE
        rmse_value = np.sqrt(mean_squared_diff)

        return rmse_value
    else:
        raise ValueError("Inputs must be of type list, tuple, or numpy array")