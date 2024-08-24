#list in which task will be stored as the user input the task
attendance = []

#function that will add the task
def add_attendance():
    P = input("Please enter the attendee name you want to add : ")
    attendance.append(P)

#function that will check the the user prompt and will remove the task if found 
def remove_from_attendance():
    if not attendance:
        print("No attendance to remove.")
        return
    print("Attendance:",attendance)
    for i, task in enumerate(attendance, 1):
        print(f"{i}. {task}")
    a_index = int(input("Enter the attendee number to remove: ")) - 1
    if 0 <= a_index < len(attendance):
        removed_attendee = attendance.pop(a_index)
        print(f"Attendee '{removed_attendee}' is removed.")
    else:
        print("Enter a valid index number")

#function that will show the task if the task are available 
def view_attendance():
    if not attendance:
        print("No task to view")
        return
    print('\nAttendance is \n', attendance)

while True:
    print("1. Add to attendance sheet")
    print("2. Remove from attendance sheet")
    print("3. View attendance")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_attendance()
    elif choice == 2:
        remove_from_attendance()
    elif choice == 3:
        view_attendance()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")