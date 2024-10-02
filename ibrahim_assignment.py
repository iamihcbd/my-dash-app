import pandas as pd

def prepare_data(file_path='gdp_1960_2020.csv'):
    """
    This function loads GDP data from a CSV file, cleans it, and prepares it for visualization.

    Args:
    file_path (str): The path to the CSV file containing GDP data (default is 'gdp_1960_2020.csv').

    Returns:
    pd.DataFrame: A cleaned DataFrame with relevant columns and formatted data.
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Select relevant columns (year, country, gdp) and drop rows with missing values
    df = df[['year', 'country', 'gdp']].dropna()
    
    # Convert the 'year' column to integers for consistency
    df['year'] = df['year'].astype(int)
    
    return df
