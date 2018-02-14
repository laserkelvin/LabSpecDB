
"""
    parser.py

    Routines for parsing the file formats in the catalog.
    Uses Pandas to parse the data.
"""

import pandas as pd

def read_entry(filepath):
    # Function for reading in a catalog entry in the catalog folder.
    if ".cat" in filepath:
        dataframe = read_cat(filepath)
    elif ".list" in filepath:
        dataframe = read_list(filepath)
    return dataframe


def read_cat(filepath):
    """
    Parses SPCAT output with fixed-width formatting.

    The quantum numbers are read in assuming hyperfine structure, and thus
    might not be accurate descriptions of what they actually are.
    """
    dataframe = pd.read_fwf(
        simulation_path,
        widths=[13,8,8,2,10,3,7,4,2,2,2,8,2,2],
        header=None
    )
    dataframe.columns = [
        "Frequency",
        "Uncertainty",
        "Intensity",
        "DoF",
        "Lower state energy",
        "Degeneracy",
        "ID",
        "Coding",
        "N'",
        "F'",
        "J'",
        "N''",
        "F''",
        "J''",
    ]
    return dataframe


def read_list(filepath):
    """
        Parses the list file extension, which may contain one or two column
        data for frequency or frequency/intensity.
    """
    dataframe = pd.read_csv(
        filepath,
        delim_whitespace=True,     # Flexible number of columns
        header=None
    )
    # Check the number of columns and name them appropriately
    if len(dataframe.columns) == 1:
        names = ["Frequency"]
    elif len(dataframe.columns) == 2:
        names = ["Frequency", "Intensity"]
    dataframe.columns = names
    return dataframe
