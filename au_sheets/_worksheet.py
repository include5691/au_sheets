import logging
from gspread import Worksheet
from gspread.exceptions import WorksheetNotFound, GSpreadException
from ._spreadsheet import get_spreadsheet

def get_worksheet(table_name: str, sheet_name: str, create_sheet: bool = False) -> Worksheet | None:
    """Get Worksheet by table name and sheet name"""
    spreadsheet = get_spreadsheet(table_name)
    if not spreadsheet:
        logging.error(f"Spreadsheet '{table_name}' not found")
        return None
    try:
        gsheet = spreadsheet.worksheet(sheet_name)
        return gsheet
    except WorksheetNotFound:
        if create_sheet:
            gsheet = spreadsheet.add_worksheet(title=sheet_name, rows=10, cols=10)
            logging.debug(f"Sheet '{sheet_name}' created")
            return gsheet
        else:
            logging.debug(f"Existing sheet '{sheet_name}' not found")
            return None
    except ConnectionError as e:
        logging.error("ConnectionError: " + str(e))
        return None
    except GSpreadException as e:
        logging.error("GSpreadException: " + str(e))
        return None
    except Exception as e:
        logging.error("Error: " + str(e))
        return None