from employe import Employee

class Hr:
    def __init__(self):
        print("in no argument constructor")

    def get_hr_emprequested_info(self):
        emp1 = Employee(10,"sop",10000,["raghu","arun"])
        return emp1.get_emp_info()


hr = Hr()
empno, empname, salary, first_manager,second_manager, anualsal, deptno = hr.get_hr_emprequested_info()
print('empno - ',empno)
print('empnoame - ',empname)
print('salary - ', salary)
print('first_manager - ',first_manager)
print('second_manager -', second_manager)
print('amnualsal - ',anualsal)
print('deptno - ',deptno)