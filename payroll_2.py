#! /usr/bin/env Python3.10

Reg_Hours = 40
Overtime_Pay = 1.5
Holiday_Pay = 2
Holiday_OT = 3
# Overtime is 1.5x of hourly rate
# Holiday regular payrate is 2x of hourly rate
# Holiday OT is 3x of hourly rate
# Fed_tax = 15%
# State_tax = 10%
# FICA = 2%

total = 0
count = 0
employees = int(input("How many employees: "))
while employees < 1:
    total += employees
    count += 1

name = str(input("What is your name: "))
print(f"Welcome {name}, this system will print your weekly paycheck.\n"
      f"Our system only accepts real numbers as a valid input.\n"
      f"The sky is the limit for your pay rate!!!\n"
      f"We do know that you can't work more hours than there are in a week, so no funny business!!\n")

while True:
    try:
        hourly_rate = float(input("What is your desired hourly pay rate: $"))
    except ValueError:
        print("Error. Try again!")
        continue
    else:
        break

while True:
    try:
        hours = float(input("How many hours were worked: "))
    except ValueError:
        print("Error. Try again!")
        continue
    else:
        break
holiday_work = float(input("How many holiday hours worked: "))

print(f"Employee: ", name)
print(f"Hourly rate: $", hourly_rate)
print(f"Hours worked: ", hours)

if hours >= 40:
    regular = Reg_Hours * hourly_rate
else:
    regular = hours * hourly_rate

print(f"Regular Pay: $", '%.2f' % regular)

overtime = (hours-Reg_Hours) * (hourly_rate * Overtime_Pay)

if overtime <= 0:
    overtime = 0
else:
    overtime = (hours-Reg_Hours) * (hourly_rate * Overtime_Pay)
    
print(f"Overtime Pay: $", '%.2f' % overtime)
holiday_pay = (holiday_work * hourly_rate * 2)
print("Holiday Pay, If any: $", '%.2f' % holiday_pay)
total = regular + overtime + holiday_pay
print("Gross Pay: $", '%.2f' % total)
fed_tax = total * 0.15
print("Federal tax: $", '%.2f' % fed_tax)
state_tax = total * 0.10
print("State tax: $", '%.2f' % state_tax)
fica = total * 0.02
print("FICA: $", '%.2f' % fica)
net_pay = total - (fed_tax + state_tax + fica)
print("Net pay: $", '%.2f' % net_pay)
