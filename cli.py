from opd_queue_management import OPDQueue

def add_patient_from_user_input(opd_queue):
    """Prompt the user for patient name and add them to the queue."""
    patient_name = input("Enter the patient's name: ")
    opd_queue.add_patient_to_queue(patient_name)
    
def view_opd_queue(opd_queue):
    """Display all patients in the OPD queue."""
    opd_queue.view_queue()

def serve_patient(opd_queue):
    """Serve the first patient in the queue."""
    opd_queue.serve_patient()

def main():
    """Main loop for the user to interact with the system."""
    opd_queue = OPDQueue()  # Initialize the OPDQueue
    
    while True:
        print("\nHospital Management System - OPD Queue")
        print("1. Add Patient to OPD Queue")
        print("2. View OPD Queue")
        print("3. Serve Next Patient")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_patient_from_user_input(opd_queue)
        elif choice == '2':
            view_opd_queue(opd_queue)
        elif choice == '3':
            serve_patient(opd_queue)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
