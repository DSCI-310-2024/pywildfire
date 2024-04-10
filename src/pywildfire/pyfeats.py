import pandas as pd
import numpy as np

def relevant_features(correlation_matrix, target_variable):
    ### STILL MISSING DOCSTRING
    """
    ...

    Parameters
    ----------
    correlation_matrix: ...
        ...
    output_path: ...
        ...

    Returns
    -------
    pandas.Series
        ...
        
    Examples
    --------
    >>> ...
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