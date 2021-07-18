from employe import Employee

class Hr:
    def __init__(self):
        print("in no argument constructor")

    def get_hr_emprequested_info(self):
        emp1 = Employee(10,"sop",10000)
        return emp1.get_emp_info()


hr = Hr()
empno, empname, salary, anualsal, deptno = hr.get_hr_emprequested_info()
print('empno - ',empno)
print('empnoame - ',empname)
print('salary - ',salary)
print('amnualsal - ',anualsal)
print('deptno - ',deptno)