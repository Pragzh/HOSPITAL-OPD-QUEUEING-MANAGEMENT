import sqlite3

DB_FILE = "hospital.db"  # SQLite database file

def create_db():
    """Create tables in the SQLite database."""
    conn = sqlite3.connect(DB_FILE)  # Connect to the database
    cursor = conn.cursor()

    # Create the Patients table
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )''')

    # Create the Inventory table
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        item_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        threshold INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

def add_patient(name):
    """Add a new patient to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_patients():
    """Retrieve all patients from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()  # Returns a list of tuples (id, name)
    conn.close()
    return patients
