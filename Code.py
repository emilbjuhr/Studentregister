
student_list = []

print("Hello")
Startknapp = True

while (Startknapp):
    print("1. Add student")
    print("2. List of students")
    print("3. Quit")
    
    menu_input = input ("Choose 1-3: ")

    if menu_input == "1":
        student_name = input("Name: ")
        student_age = input("Age: ")
        student_dict = {"name": student_name, "age": student_age}
        student_list.append(student_dict)

        print("Student skapad: ")
        print(f"name: {student_dict["name"]}, age: {student_dict['age']}")
        

    elif menu_input == "2":
        for student in student_list:
            print(f"name: {student["name"]}, age: {student["age"]}")
            

    elif menu_input == "3":
        Startknapp = False
        
    else: 
        print("It has to be 1-3")
        
