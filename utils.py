from View import View
v=View()
while True:
            print("\nWelcome to the program!")
            print("Choose an option:\n")
            print("1. Register as Faculty")
            print("2. Register as Student")
            print("3.  Faculty profile")
            print("4.  Student profile")
            print("5.exist\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                v.register_faculty()
            elif choice == "2":
               v.register_student()
            elif choice == "3":
                v.show_faculty_profile()
            elif choice == "4":
                v.show_student_profile()
            elif choice == "5":
                print("\nThank you for using the program!")
                break
            else:
                print("\nInvalid choice! Please try again.")

