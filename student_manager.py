import csv
import os
import pandas as pd
from src.analysis import class_performance, individual_student_performance

data = "data/students.csv"

#to add student 
def add_student():
    sid = input("STUDENT ID: ")
    name = input("NAME: ")
    std = input("CLASS: ")

    phy = float(input("Physics Marks: "))
    chem = float(input("Chemistry Marks: "))
    mat = float(input("Maths Marks: "))
    study_hours = float(input("Study Hours per day: "))

    file_exists = os.path.isfile(data)

    with open(data, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "student_id", "name", "class",
                "phy_marks", "chem_marks", "mat_marks",
                "study_hours"
            ])

        writer.writerow([
            sid, name, std,
            phy, chem, mat,
            study_hours
        ])
    print("Student added successfully!")


#to display student 
def show_students():
    if not os.path.isfile(data):
        print("NO DATA FOUND")
    else:
        print("\n---- STUDENT RECORD ----")
        print(pd.read_csv(data))
    while True:
        print("\nWhat do you want to do next?")
        print("1. View analysis (graph + summary)")
        print("2. Return to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            class_performance()
            break

        elif choice == "2":
            break

        else:
            print("Invalid choice. Try again.")

def edit_student():
    if not os.path.isfile(data):
        print("NO DATA FOUND")
        return

    df = pd.read_csv(data)

    sid = input("ENTER THE STUDENT ID: ")

    if sid not in df["student_id"].values:
        print("No student found")
        return

    student_index = df[df["student_id"] == sid].index[0]

    print("\n--- Student Found ---")
    print(df.loc[[student_index]].to_string(index=False))

    print("\nWhat do you want to edit?")
    print("1. Name")
    print("2. Physics marks")
    print("3. Chemistry marks")
    print("4. Maths marks")
    print("5. Study hours")

    choice = int(input("Enter choice: "))

    if choice == 1:
        new_val = input("Enter new name: ")
        df.at[student_index, "name"] = new_val

    elif choice == 2:
        new_val = float(input("Enter new Physics marks: "))
        df.at[student_index, "phy_marks"] = new_val

    elif choice == 3:
        new_val = float(input("Enter new Chemistry marks: "))
        df.at[student_index, "chem_marks"] = new_val

    elif choice == 4:
        new_val = float(input("Enter new Maths marks: "))
        df.at[student_index, "mat_marks"] = new_val

    elif choice == 5:
        new_val = float(input("Enter new study hours: "))
        df.at[student_index, "study_hours"] = new_val

    else:
        print("Invalid choice")
        return

    df.to_csv(data, index=False)
    print("Student record updated successfully!")





def search_student_by_id():
    
    if not os.path.isfile(data):
        print("NO DATA FOUND")
        return

    df = pd.read_csv(data)
    student_id = input("enter the student id: ")
    result = df[df["student_id"] == student_id]

    if result.empty:
        print("Student ID not found")
    else:
        print("\n--- Student Found ---")
        print(result.to_string(index=False))
    while True:
        print("\nWhat do you want to do next?")
        print("1. View analysis (graph + summary)")
        print("2. Return to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            individual_student_performance(student_id)
            break

        elif choice == "2":
            break

        else:
            print("Invalid choice. Try again.")