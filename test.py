

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
        
    def has_name(self, search_name):
        return self.name.upper() == search_name.upper()   


student_list = []
average_age = 0
print("Hello")
start_buttom = True

while (start_buttom):
    print("1. Add student")
    print("2. List of students")
    print("3. Search up student")
    print("4. Agerage age of students")
    print("5. Quit")
    
    menu_input = input ("Choose 1-5: ")

    if menu_input == "1":
        student_name = input("Name: ")
        student_age = int(input("Age: "))
        student_dict = Student(student_name, student_age)
        student_list.append(student_dict)
        

        print("Student has been added: ")
        print(student_dict)
        
    elif menu_input == "2":
        if len(student_list) == 0:
            print("Student list is empty")
        else:
            for student in student_list:
                print(student)

    elif menu_input == "3":
        found = False
        search = input ("Type students name: ")
        for student in student_list:
            if student.has_name(search):
                found = True
                print("Student found in student list")
            else:
                print("Student was not found")    

    elif menu_input == "4":
        if len(student_list) > 0:
            total_age = 0
            for student in student_list:
                total_age = sum(student.age for student in student_list)
                average_age = total_age / len(student_list)
            print(f"Average age: {average_age}")
        else:
            print("There are no students. Add more with option 1")

    elif menu_input == "5":
        start_buttom = False
        
    else: 
        print("It has to be 1-5")