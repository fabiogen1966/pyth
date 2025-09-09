import cx_Oracle
from tabulate import tabulate

# Configura la connessione al database
DB_USER = "AQADM"
DB_PASSWORD = "AQADM"

def get_dba_errors(ambiente, package_name):
    query = """
        SELECT OWNER, NAME, TYPE,SEQUENCE, LINE, POSITION, TEXT, ATTRIBUTE,MESSAGE_NUMBER
        FROM DBA_ERRORS
        WHERE UPPER(NAME) = UPPER(:package_name)
        ORDER BY LINE, POSITION
    """

    try:
        # Connessione al database
        with cx_Oracle.connect(DB_USER, DB_PASSWORD, ambiente) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, {"package_name": package_name.upper()})
                rows = cursor.fetchall()

                if rows:
                    headers = ["OWNER", "NAME", "TYPE", "SEQUENCE", "LINE",
                               "POSITION", "TEXT", "ATTRIBUTE", "MESSAGE_NUMBER"]
                    print(tabulate(rows, headers=headers, tablefmt="grid"))
                else:
                    print("Nessun errore trovato per il package.")
    except cx_Oracle.DatabaseError as e:
        print("Errore di database:", e)


