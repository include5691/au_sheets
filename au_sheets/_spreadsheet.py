import logging
from gspread import Client, Spreadsheet
from gspread.exceptions import SpreadsheetNotFound, APIError, GSpreadException
from ._creds import get_creds

def get_spreadsheet(table_name: str) -> Spreadsheet | None:
    """Get Spreadsheet by table name"""
    creds = get_creds()
    if not creds:
        logging.error("Credentials not found")
        return None
    client = Client(auth=creds)
    try:
        spreadsheet = client.open(table_name)
        return spreadsheet
    except SpreadsheetNotFound as e:
        logging.error("Error while opening table: " + str(e))
        return None
    except APIError as e:
        logging.error("APIError: " + str(e))
        return None
    except GSpreadException as e:
        logging.error("GSpreadException: " + str(e))
        return None
    except Exception as e:
        logging.error("Error: " + str(e))
        return None