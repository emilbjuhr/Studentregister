
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
        student_dict = {"name": student_name, "age": student_age}
        student_list.append(student_dict)
        

        print("Student has been added: ")
        print(f"name: {student_dict["name"]}, age: {student_dict['age']}")
        
    elif menu_input == "2":
        for student in student_list:
            print(f"name: {student["name"]}, age: {student["age"]}")

    elif menu_input == "3":
        found = False
        search = input ("Type students name: ")
        for student in student_list:
            if search.upper() == student["name"].upper():
                found = True
                print("Student found in studentlist")
            else:
                print("Student was not found")    

    elif menu_input == "4":
        if len(student_list) > 0:
            total_age = 0
            for student in student_list:
                total_age += student["age"]
                average_age = total_age / len(student_list)
            print(f"Average age: {average_age}")
        else:
            print("There are no students. Add more with option 1")

    elif menu_input == "5":
        start_buttom = False
        
    else: 
        print("It has to be 1-5")
        
