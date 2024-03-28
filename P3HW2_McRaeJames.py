##James McRae
##3/26/24
##P3HW2
##Calculating the pay of an employee with or without overtime.
employee=input("Enter employee's name: ")
hrs = float(input("Enter number of hours worked: "))
rate= float(input("Enter employee's pay rate: "))
print('-'*37)
print("Employee name:" + employee)

print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-"*80)

if hrs >40:
    reg_pay=rate*40
    ovt_hrs=hrs-40
    ovt_rate=1.5*rate
    ovt_pay=ovt_hrs*ovt_rate
    gross_pay= reg_pay + ovt_pay
else:
 ovt_hrs=0
 ovt_pay=0
 reg_pay=rate*hrs
 gross_pay= reg_pay + ovt_pay

print(f'{hrs:<15.1f}' f'{rate:<10.1f}' f'{ovt_hrs:<12.1f}' f'{ovt_pay:<15.2f}' f'{reg_pay:<15.2f}' f'{gross_pay:<15.2f}')
#Enter Employee's name, hrs worked, and work rate.
#If hrs are over 40 then the overtime rate will be calculated.
