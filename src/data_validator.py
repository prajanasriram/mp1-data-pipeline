import logging
import pandas as pd

logger = logging.getLogger(__name__)

def validate_dataframe(df, required_columns, numeric_columns):
    """Validate the DataFrame and return valid data.
    required_columns: a list of column names that must exist.
    numeric_columns: a list of column names whose values should be
    numeric."""

    initial_rows = len(df)

    for col in required_columns:
        if col not in df.columns:
            logger.error(f"Missing required column: {col}")
            raise ValueError(f"Missing required column: {col}")

    for col in numeric_columns:
        invalid_rows = []
        for i, value in df[col].items():
            if pd.notna(value):
                try:
                    float(value)
                except ValueError:
                    invalid_rows.append(i)
                    logger.warning(f"Invalid numeric value in column {col}, row {i}")
                    pass

        for index in invalid_rows:
            df = df.drop(index)

        #convert to a numeric data type
        df[col] = pd.to_numeric(df[col])

    rows_removed = initial_rows - len(df)
    logger.debug(f"Validation: {len(df)} valid rows, {rows_removed} removed rows")

    return df
    pass