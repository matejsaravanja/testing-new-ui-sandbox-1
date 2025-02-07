import sqlite3

def init_db():
    conn = sqlite3.connect("nft_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nfts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_wallet TEXT NOT NULL,
            nft_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()