import sqlite3

# tebles and db create
def initialize_db():
    conn = sqlite3.connect('email_sender.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS email_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database and tables created successfully.")
