# OOPs 
class Employee:
    #Constructor
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")

emp1 = Employee("John Doe", "Software Engineer")
emp1.display_info()

# Inheritance
class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

mgr1 = Manager("Jane Smith", "Project Manager", "IT")
mgr1.display_info()