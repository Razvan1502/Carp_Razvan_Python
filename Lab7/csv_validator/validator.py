import pandas as pd

class CSVValidator:
    def __init__(self, file_path, config):
        self.file_path = file_path
        self.config = config

    def read_csv(self):
        # Read CSV file using pandas
        df = pd.read_csv(self.file_path)
        return df

    def validate(self, df):
        # Apply user-defined rules for validation
        for column, rules in self.config.items():
            # Check for missing values
            if "check_missing" in rules and rules["check_missing"]:
                if df[column].isnull().any():
                    print(f"Missing values found in column '{column}'")

            # Check data types
            if "expected_dtype" in rules:
                expected_dtype = rules["expected_dtype"]
                if not df[column].dtype == expected_dtype:
                    print(f"Invalid data type in column '{column}'. Expected '{expected_dtype}', found '{df[column].dtype}'")

