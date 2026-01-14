# Functions for Productivity Analysis

# method 1

def calculate_pay(hours, rate):
    return hours * rate
total = calculate_pay(8, 500)
print(total)  #calculate_pay(hours, rate) Return total pay

def employee_statistics(hours_list):
    max_hours = max(hours_list)
    min_hours = min(hours_list)
    avg_hours = sum(hours_list) / len(hours_list)
    return max_hours, min_hours, avg_hours
hours = [8, 6, 9, 7, 10]
result = employee_statistics(hours)
print(result) # employee_statistics(hours_list) Return max, min, and average hours.

def search_employee(employees, emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            return employee
    return "Employee not found"


employees = [
    {"id": 101, "name": "Sravya", "role": "Developer"},
    {"id": 102, "name": "Anil", "role": "Tester"},
    {"id": 103, "name": "Meena", "role": "HR"}
]
print(search_employee(employees, 101))
print(search_employee(employees, 105)) # search_employee(employees, emp_id) Return employee details if found, otherwise ""Employee not found"".



# method 2



def calculate_pay(hours, rate): #calculate_pay(hours, rate) Return total pay
    try:
        return hours * rate
    except TypeError:  # if hours or rate is not a number
        return "error"

print(calculate_pay(40, 500))
print(calculate_pay(4.4, 50.0))




def employee_statistics(hours_list):# employee_statistics(hours_list) Return max, min, and average hours.
    try:
        max_hours = max(hours_list)
        min_hours = min(hours_list)
        avg_hours = sum(hours_list) / len(hours_list)
        return max_hours, min_hours, avg_hours
    except ValueError:
        return "Error: Hours list is empty"
    except TypeError:
        return "Error: List should contain numbers only"

hours = [8, 6, 9, 7, 10]
print(employee_statistics(hours))
print(employee_statistics([]))
print(employee_statistics('sravya'))  



employees = [
    {"id": 101, "name": "Sravya", "role": "Developer"},
    {"id": 102, "name": "Anil", "role": "Tester"},
    {"id": 103, "name": "Meena", "role": "HR"}
]


def search_employee(employees, emp_id):# search_employee(employees, emp_id) Return employee details if found, otherwise ""Employee not found"".
    try:
        for employee in employees:
            if employee["id"] == emp_id:
                return employee
        return "Employee not found"
    except TypeError:
        return "Error: Invalid input"

print(search_employee(employees, 101))
print(search_employee("invalid", 102))
print(search_employee(employees, 104))

