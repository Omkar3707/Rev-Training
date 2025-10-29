from ArithCalculations import ArithCalculations
from AgeNotEnoughError import AgeNotEnoughError

n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
age=int(input("enter the age: "))
calc=ArithCalculations(n1,n2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.mul()}')

try:
    #Zero Division error
    if n2==0:
        raise ZeroDivisionError("Division by zero")

    if age<18:
        raise AgeNotEnoughError("You are Minor")

    l1=[1,3,5,6]
    val=l1[2]
    res=calc.div()
    print(val)
    print(f'Division  ={res}')

except ZeroDivisionError as e:
    print(f'Error: {e}')
except IndexError as e:
    print(f'Error: {e}')
except AgeNotEnoughError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Something went wrong: {e}')

else:
    print("All Operations executed successfully")

finally:
    print("Done!!")
