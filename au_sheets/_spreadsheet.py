import logging
from gspread import Client, Spreadsheet
from gspread.exceptions import SpreadsheetNotFound
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