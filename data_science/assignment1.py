emp ={}
def add_emp(emp_id, name, age, department, salary):
    if emp_id in emp:
        print("Employee ID already exists")
    else:
        emp[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}
        print("Employee added successfully")

def del_emp(emp_id):
    if emp_id in emp:
        del emp[emp_id]
        print("Employee deleted successfully")
    else:
        print("Employee ID not found")

def update_emp(emp_id, name, age, department, salary):
    if emp_id in emp:
        emp[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}
        print("Employee updated successfully")
    else:
        print("Employee ID not found")

def search_emp(emp_id):
    if emp_id in emp:
        print(emp[emp_id])
    else:
        print("Employee ID not found")

def display_emp():
    for emp_id, emp_info in emp.items():
        print(emp_id, emp_info)

while True:
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Display Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = int(input("Enter Employee Salary: "))
        add_emp(emp_id, name, age, department, salary)
    elif choice == 2:
        emp_id = int(input("Enter Employee ID: "))
        del_emp(emp_id)
    elif choice == 3:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = int(input("Enter Employee Salary: "))
        update_emp(emp_id, name, age, department, salary)
    elif choice == 4:
        emp_id = int(input("Enter Employee ID: "))
        search_emp(emp_id)
    elif choice == 5:
        display_emp()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
    