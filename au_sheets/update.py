import logging
import numpy as np
from pandas import DataFrame
from gspread.exceptions import APIError
from ._worksheet import get_worksheet

def update_sheet(df: DataFrame, table_name : str, sheet_name: str, create_sheet: bool = False) -> None:
    """Update Google Sheet with DataFrame values"""
    if not isinstance(df, DataFrame) or df.empty:
        logging.error("Invalid DataFrame")
        return
    df_clean = df.replace({np.nan: ''})
    headers = df_clean.columns.tolist()
    values = df_clean.to_numpy().tolist()
    data = [headers] + values
    worksheet = get_worksheet(table_name, sheet_name, create_sheet)
    try:
        worksheet.clear()
        worksheet.update(
            "A1:" + chr(65 + len(headers) - 1) + str(len(data)),
            data,
            value_input_option="USER_ENTERED",
        )
    except APIError as e:
        logging.error(f"Error updating {sheet_name}: {e}")
        return