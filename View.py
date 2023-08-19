from Controller import Controller
class View:
    def __init__(self):
        self.faculty_controller = Controller()
        self.student_controller = Controller()

    def register_faculty(self):
        username=input("enter username:")
        password=input("enter password:")
        designation = input("Enter designation: ")
        subject = input("Enter your subject: ")
        if self.faculty_controller.register_faculty(username,password, designation, subject):
            print("\nRegistration successful!")
        else:
            print("\nRegistration failed! Please try again.")
    def register_student(self):
        username=input("enter username:")
        password=input("enter password:")
        semester= input("Enter a semester: ")
        cgpa = float(input("Enter your cgpa: "))
        major = input("Enter your Major: ")
        if self.student_controller.register_student(username,password, semester, cgpa, major):
            print("\nRegistration successful!")
        else:
            print("\nRegistration failed! Please try again.")

    def authenticate_faculty(self):
        id = int(input("\nEnter your id: "))
        password = input("Enter your password: ")
        faculty = self.faculty_controller.authenticate_faculty(id, password)
        if faculty:
            self.show_faculty_profile(faculty)
        else:
            print("\nAuthentication failed! Please try again.")

    def authenticate_student(self):
        id = input("\nEnter your id: ")
        password = input("Enter your password: ")
        student = self.student_controller.authenticate_student(id, password)
        if student:
            self.show_student_profile(student)
        else:
            print("\nAuthentication failed! Please try again.")

    def show_faculty_profile(self):
        print("\nWelcome !")
        while True:
            print("\nChoose an option:\n")
            print("1. View profile")
            print("2. Edit profile")
            print("3. Delete profile")
            print("4. Logout\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n" + str(self))
            elif choice == "2":
                id= int(input("\nEnter  id: "))
                designation = input("Enter designation: ")
                subject = input("Enter your subject: ")
                
                if self.faculty_controller.update_faculty(self.id, id,designation, subject):
                    print("\nProfile updated successfully!")
                    self.designation = designation
                    self.subject = subject
            elif choice=="3":
                id=int(input("enter id:"))
                if  self.faculty_controller.delete_faculty(self.id):
                   print("\nProfile  deleted successfully!")

    def show_student_profile(self, student):
        print("\nWelcome, " + student.id + "!")
        while True:
            print("\nChoose an option:\n")
            print("1. View profile")
            print("2. Edit profile")
            print("3. Delete profile")
            print("4. Logout\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n" + str(student))
            elif choice == "2":
                id= int(input("\nEnter  id: "))
                username=input("enter username:")
                password=input("enter password:")
                semester= input("Enter a semester: ")
                cgpa = float(input("Enter your cgpa: "))
                major = input("Enter your Major: ")
                
                if self.student_controller.update_student(student.id,id, username,password,semester,cgpa,major):
                    print("\nProfile updated successfully!")
                    student.id = id
                    student.username = username
                    student.password = password
                    student.semester = semester
                    student.cgpa = cgpa
                    student.major = major
            elif choice=="3":
                 id=int(input("enter id:"))
                 if  self.student_controller.delete_faculty(student.id,id):
                   print("\nProfile  deleted successfully!")

