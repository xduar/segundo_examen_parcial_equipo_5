"""Local development settings (not versioned).
Attempt to use SQL Server LocalDB for development on this machine.

Server: (localdb)\MSSQLLocalDB
Database: InventarioBD-G1

If LocalDB cannot be reached, fallback to SQLite by commenting the SQL Server block.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

# Named pipe discovered for the local instance when this file was edited on the dev machine.
# If the instance pipe name changes, update the NP string accordingly.
LOCALDB_NAMED_PIPE = r"\\.\pipe\LOCALDB#0BA82AC1\tsql\query"

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'InventarioBD-G1',
        # Use the named pipe to force a LocalDB connection
        'HOST': LOCALDB_NAMED_PIPE,
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            # use MARS? not required for migrations but left false
            'autocommit': True,
            # add TrustServerCertificate to reduce TLS/Encrypt issues on LocalDB
            'extra_params': 'TrustServerCertificate=yes;Encrypt=no;'
        },
    }
}

# Note: if this setup fails with pyodbc OperationalError, revert to SQLite by using:
# DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}
