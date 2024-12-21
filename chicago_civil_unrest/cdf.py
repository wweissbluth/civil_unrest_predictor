import numpy as np
import pandas as pd
# Load the data from the CSV file
data = pd.read_csv('reindex_data.csv')

def cdf(data, value):
    """
    Computes the CDF of a given value from a data series.

    Parameters:
    data (iterable): A sequence or array of numerical values.
    value (float): The value for which to calculate the CDF.

    Returns:
    float: The CDF value of the given value.
    """
    data_sorted = np.sort(data)  # Sort the data
    cdf = np.sum(data_sorted <= value) / len(data_sorted)  # Proportion of values <= value
    return cdf
