class User:
    name = ''
    email = ''
    password = '38293'
    student_id = 0

    def getlogininfo(self):
        student_name = input("Enter your name: ")
        student_email = input("Enter your email: ")
        student_password = input("Enter your password: ")
        if (student_email == self.email and student_password == self.password):
            print("Welcome back, {}!".format(student_name))
        else:
            print("Wrong email or password")

class student(User):
    base_gpa = 3.5
    grade = '11th Grade'

    def getlogininfo(self):
        student_name = input("Enter your name: ")
        student_email = input("Enter your email: ")
        student_pin = input("Enter your pin: ")
        if (student_email == self.email and student_pin == self.pin):
            print("Welcome back, {}!".format(student_name))
        else:
            print("Wrong email or pin")

class student_info(User):
    address = '4848 leaf st'
    phone = '503-498-4827'
    
schoolwebsite = User()
schoolwebsite.getlogininfo()

onlineclass = student()
onlineclass.getlogininfo()
