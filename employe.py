#creating  emp class

class Employee():

    def __init__(self, empno, empname, salary):
        self.empno = empno
        self.empname = empname
        self.salary = salary

    def get_emp_info(self):
        print("in emp info")
        return self.empno, self.empname, self.salary, self.get_emp_annual_salary(), self.emp_department_nor()

    def get_emp_annual_salary(self):
        print('in emp anual salary')
        return self.salary * 12

    def emp_department_nor(self):
        return 10




