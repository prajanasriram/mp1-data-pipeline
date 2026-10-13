This project is a data processing pipeline which begins by loading the data and then validating, cleaning, and saving data from the input file. Pipeline.py connects to the different modules. Data_loaders.py loads the inputted data and the configuration file and the utils.py handles the file validation an logging. Data_validator.py checks for the required columns and remoces rows that have invalid values. Data_processor.py cleans the data and removes duplicate rows, missing values, and also removes outliers based on predefined settings in the config.yaml file. The data_output.py file saves the cleaned dataframe as a csv file. 

An example command is: python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

This provides an output of:

20:19:17 INFO     src.utils — Input file validated: fixtures/sample_data.csv
20:19:17 INFO     src.utils — Input file validated: config/config.yaml
20:19:17 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
20:19:17 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
20:19:17 WARNING  src.data_validator — Invalid numeric value in column rating, row 94
20:19:17 WARNING  src.data_validator — Invalid numeric value in column rating, row 95
20:19:17 DEBUG    src.data_validator — Validation: 98 valid rows, 2 removed rows
20:19:17 INFO     __main__ — Validation complete: 100 -> 98 rows
20:19:17 DEBUG    root — The number of rows removed is: 2
20:19:17 DEBUG    src.data_processor — Number of rows removed: 2
20:19:17 DEBUG    src.data_processor — rating: method=iqr, threshold=1.5, removed=2
20:19:17 INFO     __main__ — Processing results: {'rows before': 98, 'rows after': 92, 'rows removed': 6, 'columns before': 5, 'columns after': 5, 'columns removed': 0}
20:19:17 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
20:19:17 INFO     __main__ — Cleaned data saved to: output/clean.csv
{'rows before': 98, 'rows after': 92, 'rows removed': 6, 'columns before': 5, 'columns after': 5, 'columns removed': 0}

