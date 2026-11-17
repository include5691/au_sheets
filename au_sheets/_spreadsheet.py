import os
import logging
from requests import Session
from google.auth.transport.requests import AuthorizedSession, Request
from gspread import Client, Spreadsheet
from gspread.exceptions import SpreadsheetNotFound, APIError, GSpreadException
from gspread.utils import convert_credentials
from ._creds import get_creds

TIMEOUT = (10, 60)


def _proxied_session(session: Session, proxy: str) -> Session:
    session.proxies = {"http": proxy, "https": proxy}
    return session


def _get_client(creds) -> Client:
    proxy = os.getenv("GOOGLE_PROXY")
    session = None
    if proxy:
        auth_request = Request(_proxied_session(Session(), proxy))
        session = _proxied_session(AuthorizedSession(convert_credentials(creds), auth_request=auth_request), proxy)
    client = Client(auth=creds, session=session)
    client.set_timeout(TIMEOUT)
    return client

def get_spreadsheet(table_name: str) -> Spreadsheet | None:
    """Get Spreadsheet by table name"""
    creds = get_creds()
    if not creds:
        logging.error("Credentials not found")
        return None
    client = _get_client(creds)
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