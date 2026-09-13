import sqlite3

filename = 'project.db'
connection = sqlite3.connect(filename)

cursor = connection.cursor()

#cursor.execute("DROP TABLE IF EXISTS Courses;")
#connection.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS Courses(
               Code TEXT PRIMARY KEY,
               Title TEXT,
               Semester TEXT,
               Year INTEGER,
               Grade TEXT
               )
""")

connection.commit()

while True:
    choice = int(input("""Enter 0 to terminate>
Enter 1 to view the table>
Enter 2 to insert>
Enter 3 to delete>
Enter 4 to update>
Enter 5 to view a specific course>
    """))

    if choice == 0:
        print("TERMINATING PROGRAM....")
        break

    elif choice == 1:  # View all
        viewAll = "SELECT * FROM Courses"
        cursor.execute(viewAll)
        tableData = cursor.fetchall()
        print()
        print("  Code                Title                  Semester          Year          Grade ")
        print("=====================================================================================")
        for course in tableData:
            print(f"{course[0]:<16} {course[1]:<28} {course[2]:<16} {course[3]:<14} {course[4]:<5}")
        print()

    elif choice == 2:  # Insert
        code = input("Enter the code: ")
        title = input("Enter the title: ")
        semester = input("Enter the semester: ")
        year = input("Enter the year: ")
        grade = input("Enter the grade: ")

        insert = f"INSERT INTO Courses VALUES ('{code}', '{title}', '{semester}', {year}, '{grade}')"
        cursor.execute(insert)
        connection.commit()
        print("\nCourse added successfully!\n")

    elif choice == 3:  # Delete
        delete_code = input("Enter the code of the course you want to delete: ").strip()

        cursor.execute("SELECT * FROM Courses WHERE Code = ?", (delete_code,))
        course = cursor.fetchone()

        if not course:
            print("\nInvalid course code. Please try again.\n")
        else:
            cursor.execute("DELETE FROM Courses WHERE Code = ?", (delete_code,))
            connection.commit()
            print(f"\nCourse {delete_code} deleted successfully!\n")

    elif choice == 4:  # Update
        update_code = input("Enter the code of the course you want to update: ").strip()

        cursor.execute("SELECT * FROM Courses WHERE Code = ?", (update_code,))
        course = cursor.fetchone()

        if not course:
            print("\nInvalid course code. Please try again.\n")
        else:
            print("\nPress Enter if you do not want to update a field.\n")

            new_title = input("Enter the new title or press Enter to skip: ").strip()
            new_semester = input("Enter the new semester or press Enter to skip: ").strip()
            new_year = input("Enter the new year or press Enter to skip: ").strip()
            new_grade = input("Enter the new grade or press Enter to skip: ").strip()

            updates = []
            values = []

            if new_title:
                updates.append("Title = ?")
                values.append(new_title)
            if new_semester:
                updates.append("Semester = ?")
                values.append(new_semester)
            if new_year:
                updates.append("Year = ?")
                values.append(int(new_year))
            if new_grade:
                updates.append("Grade = ?")
                values.append(new_grade)

            if updates:
                values.append(update_code)
                sql = f"UPDATE Courses SET {', '.join(updates)} WHERE Code = ?"
                cursor.execute(sql, values)
                connection.commit()
                print(f"\nCourse {update_code} updated successfully!\n")
            else:
                print("\nNo updates made.\n")

    elif choice == 5:  # View a specific course
        viewCourse = input("Enter the code of the course you want to view: ").strip()
        cursor.execute("SELECT * FROM Courses WHERE Code = ?", (viewCourse,))
        course = cursor.fetchone()

        if not course:
            print("\nInvalid course code. Please try again.\n")
        else:
            print()
            print("Code                Title                  Semester          Year          Grade ")
            print("=====================================================================================")
            print(f"{course[0]:<16} {course[1]:<28} {course[2]:<16} {course[3]:<14} {course[4]:<5}")
            print()

    else:
        print("Enter a valid choice")

connection.close()
