from User import User
class Faculty(User):
    def __init__(self, id, username, password, designation, subject):
       super().__init__(id, username, password)
       self.username=username
       self.designation = designation
       self.subject = subject