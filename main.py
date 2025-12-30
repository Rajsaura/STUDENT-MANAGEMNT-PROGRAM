from src.student_manager import add_student, edit_student, show_students, search_student_by_id
from src.analysis import class_performance, individual_student_performance


def main_menu():
    while True:
        print("\n===== SMART STUDENT ANALYTICS SYSTEM =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Edit student record")
        print("5. View class performance analysis")
        print("6. View individual student analysis")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student_by_id()

        elif choice == "4":
            edit_student()

        elif choice == "5":
            class_performance()

        elif choice == "6":
            sid = input("Enter Student ID: ")
            individual_student_performance(sid)

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



main_menu()








