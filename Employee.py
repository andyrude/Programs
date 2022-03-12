class Employee:
    no_of_leavees = 8

    def printDetails(self):
        return f"{ self.name} has { rohan.salary} and { self.role} and { self.no_of_leavees}"

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 500
harry.role = 85

rohan.name = "Harry"
rohan.salary = 500
rohan.role = 85

if __name__ == '__main__':
    harry = Employee()
    rohan = Employee()

    harry.name = "Harry"
    harry.salary = 500
    harry.role = 85

    rohan.name = "Harry"
    rohan.salary = 500
    rohan.role = 85
    print( rohan.printDetails())