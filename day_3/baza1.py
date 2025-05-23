# sql
# context manager - w przyjażniejszy sposób pozwala pracowac z plikami, z zasobami
import sqlite3


class SQLiteCM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    # wykona się przy starcie
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    # wykona się zawsze
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_name = 'sqlite_db.db'
with SQLiteCM(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))

print("Baza zamknięta")
