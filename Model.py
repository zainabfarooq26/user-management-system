import pymysql
from Faculty import Faculty
from Student import Student

class Model:
    def __init__(self):
        self.db = pymysql.connect( host="localhost",user="root",password="amnamai126", database="fcit"
        )
        self.cursor = self.db.cursor()

    def register_faculty(self,username,password, designation, subject ):
        sql = "INSERT INTO user (username,password) VALUES (%s, %s)"
        val = (username, password)
        sql1 ="INSERT INTO faculty(designation, subject) VALUES(%s,%s)"
        self.cursor.execute(sql, val)
        vals = (designation,subject)
        self.cursor.execute(sql1, vals)
        self.db.commit()
        
        sql = "INSERT INTO faculty (username,password, designation, subjectt) VALUES (%s,%s, %s,%s)"
        val = ()
        self.cursor.execute(sql, val)
        self.db.commit()
        
    def register_student(self, username,password,semester,cgpa,major):
        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (username.username, password.password)
        sql1 ="INSERT INTO student(semester,cgpa,major) VALUES(%s,%s,%s)"
        self.cursor.execute(sql, val)
        vals = (semester,cgpa,major)
        self.cursor.execute(sql1, vals)
        self.db.commit()
       
        sql = "INSERT INTO student (semester, cgpa, major) VALUES (%s, %s, %s)"
        val = (semester, cgpa, major)
        self.cursor.execute(sql, val)
        self.db.commit()
        
    def get_faculty(self, username, password):
        sql = "SELECT  user.username, user.password, faculty.designation, faculty.subject FROM user JOIN Faculty ON user.id = Faculty.user_id WHERE user.username = %s AND user.password = %s"
        val = (username, password)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is not None:
            faculty = Faculty(result[0], result[1], result[2], result[3], result[4])
            return faculty
        else:
            return None
        
    def get_student(self, username, password):
        sql = "SELECT user.id, user.username, user.password, student.semester, student.cgpa, student.major FROM user JOIN student ON user.id = student.user_id WHERE user.username = %s AND user.password = %s"
        val = (username, password)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is not None:
            student = Student(result[0], result[1], result[2], result[3], result[4], result[5])
            student.id = result[0]
            return student
        else:
            return None
    def update_faculty(self, faculty):
        self.cursor.execute("UPDATE user SET username = ?, password = ? WHERE id = ?", (faculty.username, faculty.password, faculty.id))
        self.cursor.execute("UPDATE student SET semester = ?, cgpa = ?, major = ? WHERE user_id = ?", (faculty.semester, faculty.cgpa, faculty.major, faculty.id))
        self.connection.commit()
    def update_student(self, student):
        self.cursor.execute("UPDATE user SET username = ?, password = ? WHERE id = ?", (student.username, student.password, student.id))
        self.cursor.execute("UPDATE student SET semester = ?, cgpa = ?, major = ? WHERE user_id = ?", (student.semester, student.cgpa, student.major, student.id))
        self.connection.commit()
    def delete_faculty(self, id):
        self.cursor.execute("DELETE FROM user WHERE id = ?", (id,))
        self.connection.commit()
    def delete_student(self, id):
        self.cursor.execute("DELETE FROM User WHERE id = ?", (id,))
        self.connection.commit()
