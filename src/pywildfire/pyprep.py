import os
import requests
import zipfile
import pandas as pd
import shutil

def download_extract_data(url, output_path):
    """
    Download a zip file from a URL and extract the data it contains, storing it locally 
    in the specified directory.

    Parameters:
    ----------
    url: str
        The URL of the zip file to be read
    output_path: str
        The directory in which the zip file's contents will be extracted and stored

    Returns:
    -------
    str
        A message indicating whether the function execution was successful.
        
    Examples
    --------
    >>> ...
    """
    # Fetch URL and extract file name
    response = requests.get(url)
    _, filename = os.path.split(url)
    output_file_path = os.path.join(output_path, filename)

    # Check if URL exists; if not, raise an error
    if response.status_code != 200:
        raise ValueError("File download failed: the given URL does not exist.")

    # Check if the URL points to a zip file; if not, raise an error
    if not filename.endswith(".zip"):
        raise ValueError("File download failed: the given URL does not point to a zip file.")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    # Write the zip file to the specified output path
    with open(output_file_path, 'wb') as f:
        f.write(response.content)

    # Extract the zip file to the output path
    with zipfile.ZipFile(output_file_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()
        
        # Check if the zip file is empty; if yes, raise an error
        if not all_files:
            raise ValueError("Data extraction failed: the given zip file is empty.")

        zip_ref.extractall(output_path)

    # Remove zip file after data extracted
    os.remove(output_file_path)

    if not os.listdir(output_path):
        raise ValueError("No files were extracted from the given zip file.")

    return f"Data successfully downloaded and saved to {output_path}"

def get_csv(output_path, csv_file):
    """
    Returns a pandas DataFrame containing data from a csv file if it exists in the specified 
    directory, returns None if it does not exist.

    Parameters:
    ----------
    output_path: str
        The directory containing the csv file
    csv_file: str
        The name of the csv file containing the desired data

    Returns:
    ----------
    pandas.DataFrame or None
        A DataFrame containing data from the specified csv file if found, else None

     Examples
    --------
    >>> ...
    """
    files = [file for file in os.listdir(output_path)]
    if csv_file in files:
        csv_path = os.path.join(output_path, csv_file)
        data = pd.read_csv(csv_path)
        return data
    else:
        return None

def scale_numeric_df(data):
    """
    Scale the numeric columns of a DataFrame using StandardScaler()
    and return the modified DataFrame.
   
    Parameters:
    ----
    data: pandas.DataFrame
        Dataset with unscaled numeric columns.
    
    Returns:
    ------
    scaled_df: pandas.DataFrame
        Dataset with scaled columns.

     Examples
    --------
    >>> ...
    """
    # Check if df is empty
    if data.empty:
        return None  # Return None if input is empty
    
    # Check if any numeric columns exist in the df
    if not any(data.select_dtypes(include=['float64', 'int64'])):
        return None  # Return None if no numeric columns exist
    
    np.random.seed(238) #keep seeded to ensure reproducibility
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler() #create scaler
    scaled_data = scaler.fit_transform(numeric_df) #apply scaler
    scaled_df = pd.DataFrame(scaled_data, columns=numeric_df.columns)
    return scaled_df
