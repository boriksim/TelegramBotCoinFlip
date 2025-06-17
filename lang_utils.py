import sqlite3

DB_PATH = 'bot_languages.db'


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            lang TEXT DEFAULT 'en'
        )
        ''')
        conn.commit()


init_db()


def get_user_language(telegram_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT lang FROM users WHERE telegram_id = ?', (telegram_id,))
        row = cursor.fetchone()
        return row[0] if row else "en"


def set_user_language(telegram_id, lang):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (telegram_id, lang)
        VALUES (?, ?)
        ON CONFLICT(telegram_id) DO UPDATE SET lang=excluded.lang
        ''', (telegram_id, lang))
        conn.commit()
