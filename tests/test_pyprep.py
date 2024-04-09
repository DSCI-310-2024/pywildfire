import os
import shutil
import responses
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pywildfire.pyprep import download_extract_data
from pywildfire.pyprep import get_csv
from pywildfire.pyprep import scale_numeric_df

# Test files setup

# setup empty directory for data files to be downloaded to
if not os.path.exists('tests/test_zip_data1'):
    os.makedirs('tests/test_zip_data1')

# setup directory that contains a file for data files to be downloaded to
if not os.path.exists('tests/test_zip_data2'):
    os.makedirs('tests/test_zip_data2')
with open('tests/test_zip_data2/test4.txt', 'w') as file:
    pass  # creates an empty file


test_dir_1 = 'tests/test_zip_data1'
test_dir_2 = 'tests/test_zip_data2'

test_files_txt_csv = ['test1.txt', 'test2.csv']
test_files_subdir = ['test1.txt', 'test2.csv', 'subdir/test3.txt']
test_files_2txt_csv = ['test1.txt', 'test2.csv', 'test4.txt']

# URL for Case 1 
url_txt_csv_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/test_files_txt_csv.zip'

# URL for Case 2 ('test1.txt', test2.csv and 'subdir/test3.txt')
url_txt_subdir_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/test_files_all.zip'

# URL for Case 3 (empty zip file)
url_empty_zip = 'https://raw.githubusercontent.com/FionaC124/dsci310-group-wildfire-predictor/abstract-download-data-script-to-fxns/tests/empty.zip'

# mock non-existing URL
@pytest.fixture
def mock_response():
    # Mock a response with a non-200 status code
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://example.com', status=404)
        yield


# DOWNLOAD_EXTRACT_DATA TESTS

# Case 1
# Test download_extract_data function can download and extract a zip file that 
# contains files with different formats
def test_download_extract_data_txt_csv():
    download_extract_data(url_txt_csv_zip, 'tests/test_zip_data1')
    # List of files you expect to find in the directory
    for file in test_files_txt_csv:
        file_path = os.path.join('tests/test_zip_data1', file)
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_txt_csv:
        if os.path.exists(file):
            os.remove(file)


# Case 2
# Test download_extract_data function can download and extract a zip file that 
# contains multiple files, including a file within a nested subdirectory
def test_download_extract_data_subdir():
    download_extract_data(url_txt_subdir_zip, 'tests/test_zip_data1')
    # List of files you expect to find in the directory
    for file in test_files_subdir:
        file_path = os.path.join('tests/test_zip_data1', file)
        print("Check file path:", file_path) # Print statement
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_subdir:
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists('tests/test_zip_data1/subdir'):
        shutil.rmtree('tests/test_zip_data1/subdir')


# Case 3
# Test download_extract_data function can download and extract a zip file that 
# contains two files into a directory that already contains a file
def test_download_extract_data_nested_subdir():
    download_extract_data(url_txt_csv_zip, 'tests/test_zip_data2')
    # List of files you expect to find in the directory
    for file in test_files_2txt_csv:
        file_path = os.path.join('tests/test_zip_data2', file)
        assert os.path.isfile(file_path)
    # clean up unzipped files
    for file in test_files_txt_csv:
        if os.path.exists(file):
            os.remove(file)


# Case 4 
# Test download_extract_data function raises an error if the zip file at the 
# input URL is empty
def test_download_extract_data_empty_zip():
    with pytest.raises(ValueError, match="Data extraction failed: the given zip file is empty."):
        download_extract_data(url_empty_zip, 'tests/test_zip_data1')


# Case 5
# Test download_extract_data function raises an error if the input URL is invalid 
def test_download_extract_data_error_on_invalid_url(mock_response):
    with pytest.raises(ValueError, match="File download failed: the given URL does not exist."):
        download_extract_data('https://example.com', 'tests/test_zip_data1')


# Case 6
# Test download_extract_data function throws an error if the URL is not a zip file
def test_download_extract_data_error_on_nonzip_url():
    with pytest.raises(ValueError, match="File download failed: the given URL does not point to a zip file."):
        download_extract_data('https://github.com/', 'tests/test_zip_data1')


# Case 7
# Test download_extract_data function creates the directory if the path 
# provided does not exist
def test_download_extract_data_create_dir():
    output_path = "tests/test_zip_data3"
    
    download_extract_data(url_txt_csv_zip, output_path)
    assert os.path.exists(output_path)
    # clean up unzipped files
    for filename in os.listdir(output_path):
        file_path = os.path.join(output_path, filename)
        os.remove(file_path)

    os.rmdir(output_path)


# GET_CSV TESTS

# Test get_csv function returns a pandas DataFrame if the csv file exists in the directory
def test_get_csv_file_exists():
    csv_file = 'test2.csv'
    output_path = test_dir_2
    result = get_csv(output_path, csv_file)
    assert result is not None
    assert isinstance(result, pd.DataFrame)


# Test get_csv function returns None if the csv file does not exist in the directory
def test_get_csv_file_does_not_exist():
    csv_file = 'fake.csv'
    output_path = test_dir_1
    result = get_csv(output_path, csv_file)
    assert result is None


# TEST_SCALED_DF TESTS

# Test if scaled df has the same shape (rows & columns) as the original df
def test_scaled_df_shape():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert data.shape == scaled_df.shape

# Test if scaled df has zero mean (is properly scaled) in each column
def test_scaled_df_zero_mean():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert np.allclose(np.mean(scaled_df, axis=0), 0)

# Test if scaled df has unit variance (variance = 1) for each column
def test_scaled_df_unit_variance():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert np.allclose(np.var(scaled_df, axis=0), 1)

# Test if scaled df values match data that's been manually scaled
def test_scaled_manual_values():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler()
    manual_scaled_data = scaler.fit_transform(numeric_df)
    manual_scaled_df = pd.DataFrame(manual_scaled_data, columns=numeric_df.columns)
    assert scaled_df.equals(manual_scaled_df)

#Test if function works when df entered is empty
def test_scaled_df_empty():
    data = pd.DataFrame()  # Empty DataFrame
    scaled_df = scale_numeric_df(data)
    assert scaled_df is None

# Test if the function returns None for non-numeric only df
def test_scaled_df_non_numeric():
    data = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']})  # non-numeric DataFrame
    scaled_df = scale_numeric_df(data)
    assert scaled_df is None
