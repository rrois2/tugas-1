import sqlite3

DATABASE_NAME = 'dealer.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS kendaraan(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                merk TEXT NOT NULL,
                model TEXT NOT NULL,
                tahun INTEGER NOT NULL,
                harga REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Tersedia'
            )''')
    conn.commit()
    conn.close()

def tambah_kendaraan_db(merk, model, tahun, harga):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("" 
            "INSERT INTO kendaraan (merk, model, tahun, harga) VALUES (?, ?, ?, ?)",
            (merk, model, int(tahun), float(harga))
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Gagal menambah ke DB : {e}")
        return False
    
def get_semua_kendaraan_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kendaraan ORDER BY tahun DESC")
    kendaraan_list = cursor.fetchall()
    conn.close()
    return kendaraan_list

def update_status_db(kendaraan_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE kendaraan SET status = ? WHERE id = ?", (status, kendaraan_id))
    conn.commit()
    conn.close()
