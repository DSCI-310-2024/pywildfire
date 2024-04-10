import pytest
import numpy as np
import pandas as pd
from pywildfire.pyfeats import relevant_features

# Test when correlation matrix is empty
def test_empty_correlation_matrix():
    correlation_matrix = pd.DataFrame()
    target_variable = 'Estimated_fire_area'
    assert relevant_features(correlation_matrix, target_variable) is None

# Test when target variable is not found in correlation matrix
def test_target_variable_not_found():
    correlation_matrix = pd.DataFrame({
        'Feature1': [0.5, 0.3, 0.2],
        'Feature2': [0.2, 0.6, 0.8],
        'Feature3': [0.7, 0.1, 0.4]
    })
    target_variable = 'Nonexistent_variable'
    assert relevant_features(correlation_matrix, target_variable) is None