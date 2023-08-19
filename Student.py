from User import User

class Student(User):
    def __init__(self, id, username, password, semester, cgpa, major):
        super().__init__(id, username, password)
        self.semester = semester
        self.cgpa = cgpa
        self.major = major