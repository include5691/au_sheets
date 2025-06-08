# au_sheets

A Python library for automating Google Sheets operations with pandas DataFrame integration. Easily read from and write to Google Sheets tables using familiar DataFrame syntax.

## Features

- **Simple DataFrame Integration**: Read Google Sheets data directly into pandas DataFrames
- **Easy Data Writing**: Write DataFrames to Google Sheets with automatic formatting
- **Automatic Sheet Management**: Create new sheets automatically when needed
- **Multiple Credentials Support**: Handle multiple service account credentials with automatic rotation
- **Robust Error Handling**: Comprehensive logging and exception handling for reliable operations

## Installation

```bash
pip install .
```

## Prerequisites

- Python 3.8+
- Google Cloud Project with Sheets API enabled
- Service account credentials (JSON format)

## Setup

### 1. Credentials Configuration

Create a `.credentials` folder in your project root and place your Google service account JSON files there:

```
your_project/
├── .credentials/
│   ├── service-account-1.json
│   └── service-account-2.json
└── your_script.py
```

Alternatively, set the `GOOGLE_SHEETS_CREDENTIALS_PATH` environment variable:

```bash
export GOOGLE_SHEETS_CREDENTIALS_PATH=/path/to/your/credentials/folder
```

### 2. Obtain Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Create a new service account
3. Download the JSON key file
4. Place it in your `.credentials` folder

## Usage

### Basic Import

```python
from au_sheets import get_df, update_sheet
```

### Reading Data from Google Sheets

```python
import pandas as pd
from au_sheets import get_df

# Read data from an existing sheet
df = get_df(table_name="My Spreadsheet", sheet_name="Sheet1")
if df is not None:
    print(df.head())

# Create sheet if it doesn't exist
df = get_df(table_name="My Spreadsheet", sheet_name="New Sheet", create_sheet=True)
```

### Writing Data to Google Sheets

```python
import pandas as pd
from au_sheets import update_sheet

# Create sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Update existing sheet
update_sheet(df, table_name="My Spreadsheet", sheet_name="Sheet1")

# Create new sheet and update
update_sheet(df, table_name="My Spreadsheet", sheet_name="New Data", create_sheet=True)
```

## API Reference

### `get_df(table_name: str, sheet_name: str, create_sheet: bool = False) -> DataFrame | None`

Retrieves data from a Google Sheet and returns it as a pandas DataFrame.

**Parameters:**
- `table_name` (str): Name of the Google Spreadsheet
- `sheet_name` (str): Name of the worksheet within the spreadsheet
- `create_sheet` (bool, optional): Create the sheet if it doesn't exist. Default: False

**Returns:**
- `DataFrame | None`: DataFrame containing the sheet data, or None if an error occurs

**Example:**
```python
df = get_df("Sales Data", "Q4 2024")
```

### `update_sheet(df: DataFrame, table_name: str, sheet_name: str, create_sheet: bool = False) -> None`

Updates a Google Sheet with DataFrame values, replacing all existing content.

**Parameters:**
- `df` (DataFrame): pandas DataFrame to write to the sheet
- `table_name` (str): Name of the Google Spreadsheet
- `sheet_name` (str): Name of the worksheet within the spreadsheet
- `create_sheet` (bool, optional): Create the sheet if it doesn't exist. Default: False

**Example:**
```python
update_sheet(my_dataframe, "Sales Data", "Q4 2024", create_sheet=True)
```

## Error Handling

The library includes comprehensive error handling and logging:

- **Connection Issues**: Handles network connectivity problems
- **Authentication Errors**: Manages credential and permission issues
- **Sheet Not Found**: Gracefully handles missing spreadsheets or worksheets
- **Data Validation**: Validates DataFrame input and handles empty datasets

All errors are logged using Python's logging module. Enable debug logging to see detailed operation information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Multiple Credentials Support

If you have multiple service account files in your credentials folder, the library will automatically rotate between them to handle API rate limits and quota restrictions.

## Dependencies

- `pandas`: DataFrame operations
- `gspread`: Google Sheets API interaction
- `oauth2client`: Authentication handling
- `numpy`: Data processing support

## License

This project is open source. Please check the license file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.