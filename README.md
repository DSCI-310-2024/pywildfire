# pywildfire
Authors: Pahul Brar, Fiona Chang, Lillian Milroy, & Darwin Zhang

Predict wildfire intensity!

## Installation

```bash
$ pip install pywildfire
```

## Usage

`pywildfire` can be used to:

- Download a zip file from a provided URL to extract data and store it in a local directory
- Returns a list of relevant features from a correlation matrix and a target variable
- Calculate the Root Mean Squared Error (RMSE) given observed and predicted values
- Scale numeric values in a dataframe

Example Usage of pywildfire

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pywildfire.pyprep import scale_numeric_df

# Create sample data
sample_data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7],
    'D': [4, 5, 6, 7, 8]
})

# Scale numeric columns
scaled_data = scale_numeric_df(sample_data)

# Print scaled data
print(scaled_data)
```
Further usage can be found in our package documentation. TODO

## Package Ecosystem

PyWildfire is among the robust Python packages for data preprocessing and analysis for regression, though our package focuses on wildfire-related datasets. While scikit-learn and pandas are other general preprocessing libraries, pywildfire differentiates itsself with functionalities centered around wildfire data.


## Contributing

Are you looking to contribute? Please view our contributing guidelines in CONTRIBUTING.md. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pywildfire` was created by Pahul Brar, Fiona Chang, Lillian Milroy, & Darwin Zhang. It is licensed under the terms of the MIT license.

## Credits

`pywildfire` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
