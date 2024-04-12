# pywildfire

Predict wildfire intensity!

## Installation

```bash
$ pip install pywildfire
```

## Usage

`pywildfire` can be used visualizate, preprocess, and plot regression models. 

``` 
from pywildfire.pywildfire import calculate_rmse 
from pywildfire.pyfeats import relevant_features
from pywildfire.pyprep import download_extract_data 

# Read a url online and download to files

url = "https://example.com/data.zip"
download_extract_data("url", "./data")

# Identify relevant features based on correlation coefficients.

corr_matrix = pd.DataFrame({
    'A': {'A': 1.0, 'B': -0.8, 'C': 1.0, 'D': -0.8},
    'B': {'A': -0.8, 'B': 1.0, 'C': -0.8, 'D': 1.0},
    'C': {'A': 1.0, 'B': -0.8, 'C': 1.0, 'D': -0.8},
    'D': {'A': -0.8, 'B': 1.0, 'C': -0.8, 'D': 1.0}
})
target_var = 'A'
relevant_features(corr_matrix, target_var)

# Calculate the Root Mean Squared Error (RMSE) between observed and predicted values.

observed = [4, 8, 5, 3, 7]
predicted = [16, 4, 7, 9, 3]
calculate_rmse(observed, predicted)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pywildfire` was created by Pahul Brar, Fiona Chang, Lillian Milroy, & Darwin Zhang. It is licensed under the terms of the MIT license.

## Credits

`pywildfire` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
