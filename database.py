import sqlite3

db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    purchases INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(
    name TEXT PRIMARY KEY,
    value TEXT
)
""")

db.commit()

cursor.execute(
    "INSERT OR IGNORE INTO settings(name, value) VALUES(?, ?)",
    ("price", "150")
)

cursor.execute(
    "INSERT OR IGNORE INTO settings(name, value) VALUES(?, ?)",
    ("vpn_link", "https://raw.githubusercontent.com/s68181791-bit/-santizz/main/LTE.txt")
)

db.commit()


def add_user(user_id, username, full_name):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users(user_id, username, full_name)
        VALUES(?, ?, ?)
        """,
        (user_id, username, full_name)
    )
    db.commit()


def get_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def add_purchase(user_id):
    cursor.execute(
        """
        UPDATE users
        SET purchases = purchases + 1
        WHERE user_id=?
        """,
        (user_id,)
    )
    db.commit()


def get_purchases(user_id):
    cursor.execute(
        """
        SELECT purchases
        FROM users
        WHERE user_id=?
        """,
        (user_id,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return 0


def get_price():
    cursor.execute(
        "SELECT value FROM settings WHERE name='price'"
    )
    return int(cursor.fetchone()[0])


def set_price(price):
    cursor.execute(
        """
        UPDATE settings
        SET value=?
        WHERE name='price'
        """,
        (str(price),)
    )
    db.commit()


def get_link():
    cursor.execute(
        "SELECT value FROM settings WHERE name='vpn_link'"
    )
    return cursor.fetchone()[0]


def set_link(link):
    cursor.execute(
        """
        UPDATE settings
        SET value=?
        WHERE name='vpn_link'
        """,
        (link,)
    )
    db.commit()
db = sqlite3.connect("database.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    purchases INTEGER DEFAULT 0
)
""")

db.commit()


def add_user(user_id, username, full_name):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id, username, full_name) VALUES(?,?,?)",
        (user_id, username, full_name)
    )
    db.commit()


def get_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()


def users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


def add_purchase(user_id):
    cursor.execute(
        "UPDATE users SET purchases = purchases + 1 WHERE user_id=?",
        (user_id,)
    )
    db.commit()


def get_purchases(user_id):
    cursor.execute(
        "SELECT purchases FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else 0 
