#creating  emp class

class Employee():

    def __init__(self, empno: int, empname: str, salary: float, managers: list):
        print("employee constructor")
        self.empno = empno
        self.empname = empname
        self.salary = salary
        self.managers = managers

    def get_emp_info(self):
        print("in emp info")
        output_managers = []
        for mgr in self.managers:
            temp = str.capitalize(mgr)
            output_managers.append(temp)

        print('output_managers - ', output_managers)
        return self.empno, self.empname, self.salary, output_managers, self.get_emp_annual_salary(), self.emp_department_nor()

    def get_emp_annual_salary(self):
        print('in emp anual salary')
        return self.salary * 12

    def emp_department_nor(self):
        print("in departnor")
        return 10




