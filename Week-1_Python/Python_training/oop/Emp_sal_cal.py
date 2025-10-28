from oop.Employee import Employee

emp_id= int(input("Enter employee id: "))
e_name = input("Enter employee name: ")
bp = float(input("Enter Basic pay: "))

employee = Employee(emp_id,e_name,bp)

print(f'Employee ID: {employee.emp_id}\nEmployee Name: {employee.e_name}\nBasic pay: {employee.bp}\n'
      f'Gross pay: {employee.cal_grosspay()}\nNet pay: {employee.cal_netpay()}')
