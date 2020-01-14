'''
    functions to work with google sheets using gspread library
    ( https://gspread.readthedocs.io/en/latest/ )
'''

def login_to_google_sheets(credentials_file):
    '''
    returns authenticated client object that we can use
    with gspread library.

    arguments:
        1. credentials -json file of login credentials
    '''
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials as SAC

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = SAC.from_json_keyfile_name(
                        credentials_file, scope)

    client = gspread.authorize(credentials)

    return client
