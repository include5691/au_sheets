import os
import logging
from pathlib import Path
from oauth2client.service_account import ServiceAccountCredentials

iter = 0

def get_creds() -> ServiceAccountCredentials | None:
    """
    Get the credentials from the JSON file
    If there are more than one file in the credentials folder, iterate through them
    """
    path_var = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
    if path_var:
        creds_path = Path(path_var)
    else:
        creds_path = Path(__file__).parent.parent / ".credentials"
    if not creds_path.exists():
        logging.error("Credentials folder not found")
        return None
    creds_files = list(creds_path.glob("*.json"))
    if not creds_files:
        logging.error("No credentials file found")
        return None
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    if len(creds_files) == 1:
        return ServiceAccountCredentials.from_json_keyfile_name(filename=creds_files[0], scopes=scopes)
    global iter
    iter = (iter + 1) % len(creds_files)
    return ServiceAccountCredentials.from_json_keyfile_name(filename=creds_files[iter], scopes=scopes)
