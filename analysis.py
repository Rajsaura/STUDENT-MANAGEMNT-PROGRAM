import pandas as pd
import os
import matplotlib.pyplot as plt

data = "data/students.csv"

def class_performance():
    if not os.path.isfile(data):
        print("NO DATA FOUND")
        return

    df = pd.read_csv(data)

    if df.empty:
        print("No student records available")
        return

    # ---------- CALCULATIONS ----------
    avg_phy = df["phy_marks"].mean()
    avg_chem = df["chem_marks"].mean()
    avg_mat = df["mat_marks"].mean()

    med_phy = df["phy_marks"].median()
    med_chem = df["chem_marks"].median()
    med_mat = df["mat_marks"].median()

    df["avg_marks"] = (df["phy_marks"] + df["chem_marks"] + df["mat_marks"]) / 3
    pass_count = (df["avg_marks"] >= 40).sum()
    fail_count = (df["avg_marks"] < 40).sum()

    # ---------- PLOT ----------
    subjects = ["Physics", "Chemistry", "Maths"]
    averages = [avg_phy, avg_chem, avg_mat]

    fig, ax = plt.subplots()
    ax.bar(subjects, averages)
    #ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Marks")
    ax.set_title("Overall Class Performance")

    
    # ---------- TABLE ----------
    table_data = [
        ["Mean", round(avg_phy, 2), round(avg_chem, 2), round(avg_mat, 2)],
        ["Median", round(med_phy, 2), round(med_chem, 2), round(med_mat, 2)],
        ["Passed", pass_count, pass_count, pass_count],
        ["Failed", fail_count, fail_count, fail_count]
    ]

    table = plt.table(
        cellText=table_data,
        colLabels=["Metric", "Physics", "Chemistry", "Maths"],
        loc="bottom",
        cellLoc="center",
        bbox=[0.0, -0.45, 1, 0.3]  

    )

    table.scale(1, 1.3)
    plt.subplots_adjust(bottom=0.35)

    plt.show()



def individual_student_performance(student_id):
    if not os.path.isfile(data):
        print("NO DATA FOUND")
        return

    df = pd.read_csv(data)
    student = df[df["student_id"] == student_id]

    if student.empty:
        print("Student not found")
        return

    phy = student["phy_marks"].values[0]
    chem = student["chem_marks"].values[0]
    mat = student["mat_marks"].values[0]

    avg_marks = round((phy + chem + mat) / 3, 2)
    result = "PASS" if avg_marks >= 40 else "FAIL"

    # ---------- PLOT ----------
    subjects = ["Physics", "Chemistry", "Maths"]
    marks = [phy, chem, mat]

    fig, ax = plt.subplots()
    ax.bar(subjects, marks)
    ax.set_title(f"Performance of Student {student_id}")
    ax.set_ylabel("Marks")

    # ---------- TABLE ----------
    table_data = [
        ["Marks", phy, chem, mat],
        ["Average", avg_marks, avg_marks, avg_marks],
        ["Result", result, result, result]
    ]

    table = plt.table(
        cellText=table_data,
        colLabels=["Metric", "Physics", "Chemistry", "Maths"],
        cellLoc="center",
        loc="bottom",
        bbox=[0, -0.55, 1, 0.35]
    )

    table.scale(1.5, 1.4)
    plt.subplots_adjust(bottom=0.45)


    plt.show()
