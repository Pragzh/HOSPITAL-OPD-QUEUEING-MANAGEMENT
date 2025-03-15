from db_helper import add_patient, get_patients

class OPDQueue:
    def __init__(self):
        self.load_patients()
        self.served_patients = []  # List for served patients
        self.ongoing_patient = None  # Variable to store the ongoing patient

    def load_patients(self):
        """Load patients from the database into the queue."""
        self.queue = [patient[1] for patient in get_patients()]

    def add_patient(self, patient_name):
        """Add a new patient to the queue and the database."""
        add_patient(patient_name)
        self.queue.append(patient_name)
        print(f"\n{patient_name} has been added to the queue.")

    def serve_patient(self):
        """Serve the first patient in the queue."""
        if self.queue:
            self.ongoing_patient = self.queue.pop(0)  # The first patient in the queue becomes the ongoing patient
            print(f"\n{self.ongoing_patient} is now being served.")
        else:
            print("\nNo patients in the queue.")

    def complete_service(self):
        """Complete the service for the ongoing patient and add them to the served list."""
        if self.ongoing_patient:
            self.served_patients.append(self.ongoing_patient)  # Add the ongoing patient to the served list
            print(f"\n{self.ongoing_patient} has been served and added to the served list.")
            self.ongoing_patient = None  # Reset the ongoing patient to None
        else:
            print("\nNo patient is currently being served.")

    def get_served_patients(self):
        """Get all served patients."""
        return self.served_patients

    def get_ongoing_patient(self):
        """Get the ongoing (currently served) patient."""
        return self.ongoing_patient

    def get_queue_length(self):
        """Get the number of people in the queue."""
        return len(self.queue)
