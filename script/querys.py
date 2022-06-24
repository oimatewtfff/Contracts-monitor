from googleAPI import *
from config import *
from __init__ import current_rate


create_test_table = """
CREATE TABLE IF NOT EXISTS contracts_contracts (
    id integer NOT NULL,
    contract integer NOT NULL,
    PRICE_USD integer NOT NULL,
    PRICE_RUB real NOT NULL,
    DATE date
);
"""

clear_all_rows = 'DELETE FROM contracts_contracts;'

def create_query():
    """
    Один большой SQL запрос сформированый циклом
    """
    insert_all_rows_table = 'INSERT INTO contracts_contracts (id,contract,PRICE_USD,PRICE_RUB,date) VALUES'

    wks = get_sheet(creds_file, 'test')
    usd = current_rate(crb_url)

    for row in wks:
        insert_all_rows_table += f"({int(row[0])},{row[1]},{row[2]},{float(row[2]) * usd},'{row[3].replace('.', '-')}'::date),"
    insert_all_rows_table = insert_all_rows_table[:-1]

    return insert_all_rows_table
