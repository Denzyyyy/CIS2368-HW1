import creds
import database
from database import create_connection, list_values, create_vault, retrieve_vault

def menu():
    while True:
        print("\nBank Management System:")
        print("1. List vaults")
        print("2. Create vault")
        print("3. Retrieve vault")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            list_values()
        elif choice == 2:
            create_vault()
        elif choice == 3:
            retrieve_vault()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
            
menu()

