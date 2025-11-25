def get_loan_info(loan_id):
    loans = [
        {
            "loan_id": 1,
            "student_name": "Alex Green",
            "student_id": "S12345",
            "device_type": "Laptop",
            "device_id": "L-001",
            "date_out": "2025-11-24",
            "due_back": "2025-12-01",
            "returned": False
        }
    ]
    for loan in loans:
        print(f"Loan ID: {loan['loan_id']}, Student Name: {loan['student_name']}, student ID: {loan['student_id']}, Device Type: {loan['device_type']}, Device ID: {loan['device_id']}, Date Out: {loan['date_out']}, Due Back: {loan['due_back']}, Returned: {loan['returned']}")

def add_loan():
    input("Enter Student ID: ")
    input("Enter Student Name: ")
    input("Enter Student ID")
    input("Enter Device Type: ")
    input("Enter Device ID: ")
    input("Enter Date Out (YYYY-MM-DD): ")
    input("Enter Due Back (YYYY-MM-DD): ")
    input("Has the device been returned? (yes/no): ")
    if input().lower() == 'yes':
        returned = True
    else:
        returned = False
    print("Loan added successfully.")

def update_loan(loan_id):
    input("Enter new Student ID: ")
    input("Enter new Student Name: ")
    input("Enter new Device Type: ")
    input("Enter new Device ID: ")
    input("Enter new Date Out (YYYY-MM-DD): ")
    input("Enter new Due Back (YYYY-MM-DD): ")
    input("Has the device been returned? (yes/no): ")
    if input().lower() == 'yes':
        returned = True
    print(f"Loan {loan_id} updated successfully.")
def delete_loan(loan_id):
    confirmation = input(f"Are you sure you want to delete loan {loan_id}? (yes/no): ")
    if confirmation.lower() == 'yes':
        print(f"Loan {loan_id} deleted successfully.")
    else:
        print("Deletion cancelled.")

def search_loans():
    search_term = input("Enter search term (Student Name, Student ID, Device Type, Device ID): ")
    loans = [
        {
            "loan_id": 1,
            "student_name": "Alex Green",
            "student_id": "S12345",
            "device_type": "Laptop",
            "device_id": "L-001",
            "date_out": "2025-11-24",
            "due_back": "2025-12-01",
            "returned": False
        }
    ]
    for loan in loans:
        if (search_term.lower() in loan['student_name'].lower() or
                search_term.lower() in loan['student_id'].lower() or
                search_term.lower() in loan['device_type'].lower() or
                search_term.lower() in loan['device_id'].lower()):
            print(f"Loan ID: {loan['loan_id']}, Student Name: {loan['student_name']}, Student ID: {loan['student_id']}, Device Type: {loan['device_type']}, Device ID: {loan['device_id']}, Date Out: {loan['date_out']}, Due Back: {loan['due_back']}, Returned: {loan['returned']}")
    
def main():
    while True:
        print("\nDevice Loan Manager")
        print("1. View Loan Information")
        print("2. Add New Loan")
        print("3. Update Existing Loan")
        print("4. Delete Loan")
        print("5. Search Loans")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            get_loan_info(None)
        elif choice == '2':
            add_loan()
        elif choice == '3':
            loan_id = int(input("Enter Loan ID to update: "))
            update_loan(loan_id)
        elif choice == '4':
            loan_id = int(input("Enter Loan ID to delete: "))
            delete_loan(loan_id)
        elif choice == '5':
            search_loans()
        elif choice == '6':
            print("Exiting Device Loan Manager.")
            break
        else:
            print("Invalid choice, please try again.")
main()