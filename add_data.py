import sqlite3

def add_email_account(email, password):
    conn = sqlite3.connect('email_sender.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO email_accounts (email, password) VALUES (?, ?)', (email, password))
    conn.commit()
    conn.close()
    print(f"Added email account: {email}")

def add_recipient(email):
    conn = sqlite3.connect('email_sender.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO recipients (email) VALUES (?)', (email,))
    conn.commit()
    conn.close()
    print(f"Added recipient: {email}")

if __name__ == "__main__":
    email_accounts = [
        ("example@mail.ru", "examplepassword"),
    ]
    for email, password in email_accounts:
        add_email_account(email, password)

    # receiver 
    recipient = "example@gmail.com"
    add_recipient(recipient)
