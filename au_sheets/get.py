import logging
from pandas import DataFrame
from gspread.exceptions import GSpreadException
from ._worksheet import get_worksheet

def get_df(table_name: str, sheet_name: str, create_sheet: bool = False) -> DataFrame | None:
    """Get sheet data as a DataFrame"""
    worksheet = get_worksheet(table_name, sheet_name, create_sheet)
    if not worksheet:
        logging.error(f"Error getting {sheet_name} with create sheet flag {create_sheet}")
        return None
    try:
        values = worksheet.get_all_values()
        if not values:
            return None
        return DataFrame(values[1:], columns=values[0])
    except GSpreadException as e:
        logging.error(f"Error getting values from {sheet_name}: {e}")
        return None