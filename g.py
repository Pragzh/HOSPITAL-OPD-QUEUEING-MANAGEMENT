from db_helper import create_db

# Initialize the database and tables
create_db()
print("Database and tables created.")

from db_helper import add_patient, get_patients

# Add patients
add_patient("John Doe")
add_patient("Jane Smith")

# Retrieve and print all patients
patients = get_patients()
print("All patients in the database:")
for patient in patients:
    print(f"Patient ID: {patient[0]}, Name: {patient[1]}")
