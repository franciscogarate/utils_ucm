import importlib
from typing import Any, Callable, List
import numpy as np
import pandas as pd

def clean_cols(cols):
    """
    Clean column names.

    This function cleans column names by applying a series of string transformations. The transformations include:
    - Converting all characters to lowercase.
    - Replacing any non-word character (anything other than a letter, number or underscore) with an underscore.
    - Replacing multiple consecutive underscores with a single underscore.
    - Removing any trailing underscores.
    - Normalizing the string using the NFKD (Normalization Form KC: Compatibility Composition) method, which replaces all compatibility characters with their equivalents.
    - Encoding the string to ASCII format, ignoring any errors.
    - Decoding the string from ASCII format back to a string.

    Args:
    cols : pandas.Index
        A pandas Index object containing the column names to be cleaned.

    Returns:
    pandas.Index
        A new pandas Index object with cleaned column names.
    """
    return (
        cols.str.lower()
        .str.replace(r"\W", "_", regex=True)
        .str.replace("_+", "_", regex=True)
        .str.replace("_$", "", regex=True)
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )


def clean_df_cols(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=dict(zip(df.columns, clean_cols(df.columns))))

pd.DataFrame.clean_cols = clean_df_cols
