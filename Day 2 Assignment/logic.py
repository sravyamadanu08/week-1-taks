# logic.py

# method 1
hours_worked = int(input("Enter number of hours worked: "))#Ask the user to input hours worked.

# Classify working hours using if / elif / else
if hours_worked < 20:
    print("Status: Underworked")# Underworked (<20 hours)
elif hours_worked >= 20 and hours_worked <= 40:
    print("Status: Normal")#Normal (20–40 hours)
else:
    print("Status: Overtime")#Overtime (>40 hours)

print("\nEmployee List:")

# List of employee names
employees = ["Sravya", "Ravi", "Anita", "Kiran"]

for employee in employees:# Use a for loop to print all employee names
    print(employee)

# Use a while loop to repeatedly ask for a task
while True:
    task = input("Enter task: ")
    if task == "done":
        print("Task entry completed.")
        break
    else:
        print(f"Task added: {task}")


#method 2


def classify_hours(hours):
    if hours < 20:
        return "Underworked"
    elif hours >= 20 and hours <= 40:
        return "Normal"
    else:
        return "Overtime"

hours_worked = int(input("Enter hours worked: "))
print("Status:", classify_hours(hours_worked)) #Ask the user to input hours worked.



employees = ["Sravya", "Ravi", "Anita", "Kiran"] # List of employee names

print("\nEmployee List:")
for name in employees: # Use a for loop to print all employee names
    print(name)

# Use a while loop to repeatedly ask for a task
tasks = []
user_input = ""

# Loop indefinitely until the break condition is met
while True:
    user_input = input("Enter a task : ")
    
    if user_input.lower() == 'done':# Exit the loop if the user types 'done'
        break 
    else:
        tasks.append(user_input)# Add the input to the tasks list

print("Tasks collected:", tasks)




