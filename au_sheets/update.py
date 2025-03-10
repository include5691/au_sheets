import logging
import numpy as np
from pandas import DataFrame
from gspread.exceptions import APIError
from ._worksheet import get_worksheet

def _get_columns_addr(n: int) -> str:
    """Return column address by number"""
    if n < 26:
        return chr(65 + n)
    return _get_columns_addr(n // 26 - 1) + chr(65 + n % 26)

def update_sheet(df: DataFrame, table_name : str, sheet_name: str, create_sheet: bool = False) -> None:
    """Update Google Sheet with DataFrame values"""
    if not isinstance(df, DataFrame):
        logging.error("Invalid DataFrame")
        return
    df.infer_objects(copy=False)
    headers = df.columns.tolist()
    values = df.to_numpy().tolist()
    data = [headers] + values
    worksheet = get_worksheet(table_name, sheet_name, create_sheet)
    if not worksheet:
        logging.error(f"Error getting {sheet_name} with create sheet flag {create_sheet}")
        return
    try:
        worksheet.clear()
        worksheet.update(
            "A1:" + _get_columns_addr(len(headers) - 1) + str(len(data)),
            data,
            value_input_option="USER_ENTERED",
        )
    except APIError as e:
        logging.error(f"APIError: Error updating {sheet_name}: {e}")
        return
    except Exception as e:
        logging.error(f"Exception: Error updating {sheet_name}: {e}")
        return