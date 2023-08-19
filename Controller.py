from Model import Model
class Controller:
    def __init__(self):
        self.db = Model()
    def register_faculty(self,username,password, designation, subject):
        self.db.register_faculty(username,password, designation, subject)
    def register_student(self,id,semester,cgpa,major):
        self.db.register_student(id,semester,cgpa,major)
    def authenticate_faculty(self, username, password):
        faculty = self.db.get_faculty(username, password)
        if faculty:
            return True
        else:
            return False
    def authenticate_student(self, username, password):
        student = self.db.get_student(username, password)
        if student:
            return True
        else:
            return False

    def update_faculty(self, faculty_id, updated_data):
        self.db.update_faculty(faculty_id, updated_data)

    def update_student(self, student_id, updated_data):
        self.db.update_student(student_id, updated_data)

    def delete_faculty(self, faculty_id):
        self.db.delete_faculty(faculty_id)

    def delete_student(self, student_id):
        self.db.delete_student(student_id)
