
students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        students.append({"name": name, "roll": roll})
        print("Student added successfully")

    elif choice == 2:
        if not students:
            print("No students found")
        else:
            print("Student List:")
            for s in students:
                print("Name:", s["name"], "| Roll:", s["roll"])

    elif choice == 3:
        roll = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s["roll"] == roll:
                print("Student Found:", s["name"])
                found = True
                break
        if not found:
            print("Student not found")

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
