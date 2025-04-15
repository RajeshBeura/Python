import datetime

# In-memory data storage
patients = []
doctors = []
appointments = []

# Add a patient
def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    condition = input("Enter patient condition: ")
    patients.append({"Name": name, "Age": age, "Gender": gender, "Condition": condition})
    print(f"Patient {name} added successfully!")

# View patients
def view_patients():
    if not patients:
        print("No patients found.")
        return
    print("\nList of Patients:")
    for i, patient in enumerate(patients, 1):
        print(f"{i}. {patient}")

# Add a doctor
def add_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctor's specialty: ")
    doctors.append({"Name": name, "Specialty": specialty})
    print(f"Doctor {name} added successfully!")

# View doctors
def view_doctors():
    if not doctors:
        print("No doctors found.")
        return
    print("\nList of Doctors:")
    for i, doctor in enumerate(doctors, 1):
        print(f"{i}. {doctor}")

# Book an appointment
def book_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        appointments.append({"Patient": patient_name, "Doctor": doctor_name, "Date": date})
        print(f"Appointment booked successfully for {patient_name} with {doctor_name} on {date}.")
    except ValueError:
        print("Invalid date format.")

# Main Menu
def menu():
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            add_doctor()
        elif choice == '4':
            view_doctors()
        elif choice == '5':
            book_appointment()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
