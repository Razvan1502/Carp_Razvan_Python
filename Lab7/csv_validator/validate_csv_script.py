from csv_validator.validator import CSVValidator
from csv_validator.config_parser import parse_config

# Define your validation rules in a JSON file (e.g., validation_config.json)
config_file = 'validation_config.json'
config = parse_config(config_file)

# Create an instance of CSVValidator
file_path = 'your_data.csv'
validator = CSVValidator(file_path, config)

# Read the CSV file
df = validator.read_csv()

# Validate the CSV file based on user-defined rules
validator.validate(df)
