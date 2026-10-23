import sqlite3
from datetime import datetime

DATABASE_NAME = 'phishing_detector.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            result TEXT NOT NULL,
            risk_score INTEGER,
            reasons TEXT,
            scan_date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def add_scan_record(url, result, risk_score, reasons):
    """Add a new scan record to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    scan_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    reasons_str = ', '.join(reasons) if reasons else ''
    
    cursor.execute('''
        INSERT INTO scan_history (url, result, risk_score, reasons, scan_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (url, result, risk_score, reasons_str, scan_date))
    
    conn.commit()
    conn.close()

def get_scan_history(limit=50):
    """Retrieve scan history from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT url, result, risk_score, reasons, scan_date
        FROM scan_history
        ORDER BY scan_date DESC
        LIMIT ?
    ''', (limit,))
    
    records = cursor.fetchall()
    conn.close()
    
    return records

def clear_scan_history():
    """Clear all scan history from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM scan_history')
    
    conn.commit()
    conn.close()

def get_scan_count():
    """Get the total number of scans in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) as count FROM scan_history')
    count = cursor.fetchone()['count']
    
    conn.close()
    return count
