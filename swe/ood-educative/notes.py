def add(p1, p2):
    sum = p1 + p2
    return sum

print(add(2,4))

class MyClass:
    pass

obj = MyClass() # creating a MyClass Object
print(obj)

class Employee:
    ID = 3790
    salary = 2500
    department = "Human Resouces"

Steve = Employee()
print("ID =", Steve.ID)
print("Salary =", Steve.salary)
print("Department:", Steve.department)

# Creating Properties Outside a Class 
class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None
# cerating an object of the Employee class
Steve = Employee()

# assign values to properties of Steve
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# printing properties of Steve
print("ID =", Steve.ID)
print("Salary =", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)

# initializers
class Employee:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

# creating an object of Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resouces")
# printing properties of Steve
print("ID =", Steve.ID)
print("Salary =", Steve.salary)
print("Department:", Steve.department)

class Player:
    teamName = 'Liverpool'

    def __init__(self, name) -> None:
        self.name = name
p1 = Player('Mark')
p2 = Player('Steve')
print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)