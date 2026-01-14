#2.2 Task Dictionary

# method 1

employees = {
    101: ["Design", "Code Review"],
    102: ["Testing", "Bug Fixing"],
    103: ["Documentation","Review"]}#Create a dictionary where keys are employee IDs and values are lists of assigned tasks.

employees[101].append("Client Meeting")#Add a task to an employee.

employees[102].remove("Testing")#Remove a task from an employee

for emp_id, tasks in employees.items():
    print(f"Employee {emp_id} tasks: {tasks}")#Print all tasks for all employees
    

#method 2

employee_ids = [101, 102, 103]
tasks = [
    ["Prepare report"],
    ["Fix bugs", "Deploy code"],
    ["Design UI", "Client call"]
]

employee_tasks = {}

for i in range(len(employee_ids)):
    employee_tasks[employee_ids[i]] = tasks[i]

print(employee_tasks)#Create a dictionary where keys are employee IDs and values are lists of assigned tasks.

employee_tasks[102] = employee_tasks[102] + ["meeting"] #Add a task to an employee.

employee_tasks[102].pop(0)#Remove a task from an employee

for emp_id in employee_tasks:
    print(f"Employee {emp_id} tasks: {employee_tasks[emp_id]}")#Print all tasks for all employees


