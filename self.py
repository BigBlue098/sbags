class Employee:
    def employeeDetails(self):
        self.name = "Evan"
        print("Name = ", self.name)
        age = 30
        print("Age = ", age)
        
    def printEmployeeDetails(self):
        print("Print in another method")
        print("Name: ", self.name)
        print("Age: ", age)

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()