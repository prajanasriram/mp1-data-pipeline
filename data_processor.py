# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    inital_df = len (df)
    df = df.drop_duplicates()
    rows_removed = inital_df - len (df)
    logging.debug(f"The number of rows removed is: {rows_removed}")
    return df
    pass

def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""

    if axis == "rows":
        inital_rows = len(df)
        df = df.dropna(axis=0)
        rows_removed = inital_rows - len(df)
        logger.debug(f"Number of rows removed: {rows_removed}")

    elif axis == "columns":
        inital_columns = len(df.columns)
        df = df.dropna(axis=1)
        columns_removed = inital_columns - len(df.columns)
        logger.debug(f"Number of columns removed: {columns_removed}")

    else:
        logger.error(f"Unsupported axis: {axis}")
        raise ValueError(f"Unsupported axis: {axis}")

    return df

def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    
    if method != "iqr" and method != "zscore": 
        logger.error(f"Unsupported method")
        raise ValueError (f"Unsupported method")

    for column in columns:
        if column not in df.columns:
            logger.warning(f"Column does not exist")
            continue
        if not pd.api.types.is_numeric_dtype(df[column]):
            logger.warning(f"Column is not numeric: {column}")
            continue
        
        if method == "iqr":
            inital_df = len(df)
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
            rows_removed = inital_df - len(df)
        

        if method == "zscore":
            inital_df = len(df)
            avg = df[column].mean()
            standard_dev = df[column].std()
            if standard_dev == 0 or pd.isna(standard_dev):
                logger.debug(f"{column}: method={method}, threshold={threshold}, removed= 0")
                
                continue
            z_score = (df[column] - avg) / standard_dev
            df = df[abs(z_score) <= threshold]
            rows_removed = inital_df - len(df)

        logger.debug(f"{column}: method={method}, threshold={threshold}, removed={rows_removed}")


    return df 
    pass

def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    if config['processing']['remove_duplicates']:
        df = remove_duplicates(df)

    if config["processing"]["missing"]["enabled"]:
        df = handle_missing(df, axis=config["processing"]["missing"]["axis"])

    if config["processing"]["outliers"]["enabled"]:
        df = remove_outliers(
            df,
            config["processing"]["outliers"]["columns"],
            config["processing"]["outliers"]["method"],
            config["processing"]["outliers"]["threshold"]
        )
    return df
    pass

def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    rows_before = len (df_before)
    rows_after = len (df_after)
    rows_removed = rows_before - rows_after

    columns_before = len(df_before.columns)
    columns_after = len(df_after.columns)
    columns_removed = columns_before - columns_after

    summary = {
        "rows before": rows_before, 
        "rows after": rows_after, 
        "rows removed": rows_removed,
        "columns before": columns_before, 
        "columns after": columns_after, 
        "columns removed": columns_removed
        }

    return summary 
    pass