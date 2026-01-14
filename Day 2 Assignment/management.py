# 2.1 List of Employees

# method 1
employees = [
    {"id": 101, "name": "Ravi", "role": "Developer"},
    {"id": 102, "name": "Anu", "role": "Tester"},
    {"id": 103, "name": "Kiran", "role": "Manager"}] # Create a list of employee dictionaries

employees.append([{"id": 104, "name": "Sita", "role": "HR"}]) # Add a new employee to the list

employees.remove(employees[1])#Remove an employee from the list

print(len(employees))#Print the total number of employees

print(employees)# printing total employees


# method 2

employees = [] # Using a loop to create a list of dictionaries
for i in range(3):
    employees.append({"name": f"Person {i+1}", "age": 20 + i})  # Create a list of employee dictionaries
print(employees)

employees.extend([{"name": "Person 4", "age": 28}]) # Add a new employee to the list

employees.pop(0)#Remove an employee from the list

print(len(employees))#Print the total number of employees

print(employees)# printing total employees

# method 3

names = ["Sravya", "Anjali", "Rahul"]
employees = [{"name": names[i], "age": 20 + i} for i in range(3)] # Using list comprehension to create a list of dictionaries
print(employees )

employees.insert(1, {"name": "Kavya", "age": 30}) # Add a new employee to the list

for emp in employees:
    if emp["name"] == "Sravya": #Remove an employee from the list
        employees.remove(emp)
        
print(len(employees))#Print the total number of employees

print(employees)# printing total employees

# method 4

names = ["Bhavya", "Tharun", "Sindu"]
ages = [24, 26, 28]

employees = [{"name": name, "age": age} for name, age in zip(names, ages)] # Using zip() method
print(employees)

employees = [emp for emp in employees if emp["name"] != "Tharun"]#Remove an employee from the list


print(len(employees))#Print the total number of employees

print(employees)# printing total employees



