from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

CODER_USERNAME = 'admin'
CODER_PASSWORD = 'password'

# SQLite database configuration
DB_FILE = 'hospital.db'

# Function to fetch patients from the database
def get_patients():
    """Fetch all patients from the database."""
    conn = sqlite3.connect(DB_FILE)  # Connect to the SQLite database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")  # Get all patients
    patients = cursor.fetchall()  # Fetch all records
    conn.close()  # Close the connection
    return patients

# Function to add a patient to the database
def add_patient(name):
    """Add a new patient to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def index():
    patients = get_patients()  # Fetch the patient list from the database
    if 'logged_in' in session and session['logged_in']:
        return render_template('admin_dashboard.html', patients=patients)  # Admin view
    else:
        return render_template('index.html', patients=patients)  # Normal user view

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == CODER_USERNAME and password == CODER_PASSWORD:
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed! Invalid username or password.', 'danger')
            return redirect(url_for('index'))  # Redirect to home page on failed login
    return render_template('login.html')  # Display login form on GET request

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove logged_in from the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))  # Redirect to home page after logout

# Add a new patient
@app.route('/add_patient', methods=['POST'])
def add_new_patient():
    patient_name = request.form['name']
    add_patient(patient_name)
    return redirect(url_for('index'))  # Redirect to home page after adding the patient

# Mark a patient as served (admin functionality)
@app.route('/serve_patient/<int:patient_id>')
def serve_patient(patient_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
    flash('Patient has been marked as served.', 'success')
    return redirect(url_for('index'))  # Redirect to home page after serving the patient

if __name__ == '__main__':
    app.run(debug=True)
