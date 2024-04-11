import pandas as pd
import numpy as np

def relevant_features(correlation_matrix, target_variable):
    """
    Takes a correlation matrix and a target variable and returns a list of relevant features.

    Parameters
    ----------
    correlation_matrix: pandas.DataFrame
        Correlation matrix where rows and columns represent features, and values represent coefficients.
    target_variable: str
        Target variable for which relevant features will be identified.

    Returns
    -------
    pandas.Series
        List of relevant features, in descending order based on coefficient.
        
    Examples
    --------
    >>> from pywildfire.pyfeats import relevant_features
    >>> corr_matrix = pd.DataFrame({
    ...     'A': {'A': 1.0, 'B': -0.8, 'C': 1.0, 'D': -0.8},
    ...     'B': {'A': -0.8, 'B': 1.0, 'C': -0.8, 'D': 1.0},
    ...     'C': {'A': 1.0, 'B': -0.8, 'C': 1.0, 'D': -0.8},
    ...     'D': {'A': -0.8, 'B': 1.0, 'C': -0.8, 'D': 1.0}
    ... })
    >>> target_var = 'A'
    >>> relevant_features(corr_matrix, target_var)
    C    1.0
    B   -0.8
    D   -0.8
    Name: A, dtype: float64
    """
    # Check for empty inputs
    if target_variable not in correlation_matrix.columns:
        return None

    # Check if empty 
    if correlation_matrix.empty:
        return None

    # Check if any numeric columns exist in the df
    relevant_features = correlation_matrix[target_variable].sort_values(ascending=False)[1:]
    return relevant_features