class Employee:

    def __init__(self, name, id, title, department):
        self.name = name
        self.id = id
        self.title = title
        self.department = department

    def display_details(self):
        print("**************")
        print("Employee name : ", self.name)
        print("Employee id : ", self.id)
        print("Employee title : ", self.title)
        print("Employee department : ", self.department)
        print("**************")

    def __repr__(self):
        return self.name+"_"+self.id

    
emp1 = Employee("Rajesh", "001", "Software Engineer", "Backend")
emp1.display_details()
print(emp1)
#######################################################################################################
employee1 = Employee("Sohel", "002", "QA", "Testing")
employee2 = Employee("Salman", "003", "Analyst", "BPS")
employee3 = Employee("Jadhav", "004", "Manager", "Head")

class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def __repr__(self):
        return self.dept_name

    def add_employees(self):
        self.employees.append(employee1)
        self.employees.append(employee2)  
        self.employees.append(employee3)

    def delete_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)

    def list_all_employees(self):
        for employee in self.employees:
            employee.display_details()

department1 = Department("IT Sector")
department1.add_employees()
department1.delete_employee(2)
department1.list_all_employees()
#######################################################################################################

company = {}
company[department1.dept_name] = department1

def add_department(dept_name):
    department = Department(dept_name)
    department.add_employees()
    company[department.dept_name] = department

def remove_department(dept_name):
    company.pop(dept_name)

def display_departments():
    for key, value in company.items():
        print(value)

add_department("HR")
add_department("Accounts")
remove_department("Accounts")
display_departments()
#######################################################################################################
#Menu based prompt choices
ch = int(input("Enter 1 for adding employee, 2 for removing employee, 3 for displaying department : "))
while ch < 4:
    if ch == 1:
        department1.add_employees()
        department1.list_all_employees()
    elif ch == 2:
        department1.delete_employee("007")
    elif ch == 3:
        display_departments()
    elif ch == 4:
        break
    else:
        ch = input("Enter 1 for adding employee, 2 for removing employee, 3 for displaying department : ")
#######################################################################################################





