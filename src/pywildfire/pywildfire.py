import pandas as pd
import numpy as np

def calculate_rmse(observed, predicted):
    """
    Calculate the Root Mean Squared Error (RMSE) between observed and predicted values.

    Parameters
    ----------
    observed: array-like
        List, tuple, numpy array, or pandas.Series containing the observed values.
    predicted: array-like
        List, tuple, numpy array, or pandas.Series of the same length as `observed`, 
        containing the predicted values.

    Returns
    -------
    float
        The RMSE between observed and predicted values.

    Raises
    ------
    ValueError
        If `observed` or predicted` is empty.
        If `observed` and predicted` have different lengths.
        If `observed` or predicted` is not of type list, tuple, numpy array, or pandas.Series.
    
    Examples
    --------
    >>> from pywildfire.pywildfire import calculate_rmse
    
    >>> observed = pd.Series([4, 8, 5, 3, 7])
    >>> predicted = pd.Series([16, 4, 7, 9, 3])
    calculate_rmse(observed, predicted)
    6.572670690061994
    
    >>> observed = [4, 8, 5, 3, 7]
    >>> predicted = [16, 4, 7, 9, 3]
    calculate_rmse(observed, predicted)
    6.572670690061994

    >>> observed = np.array([4, 8, 5, 3, 7])
    >>> predicted = np.array([16, 4, 7, 9, 3])
    calculate_rmse(observed, predicted)
    6.572670690061994
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