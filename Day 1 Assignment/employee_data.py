# variables, datatypes concept

employee_id = 101 #int(Used to store whole numbers, Can be positive, negative, or zero)
name = 'sravya' # string(Used to store text, Written inside single quotes ' ' or double quotes " ", Can contain letters, numbers, and symbols, Numbers inside quotes are treated as text)
hourly_rate = 250.75 #float(Used to store decimal numbers, contains a decimal point)
is_active = True #boolean(Used to store True or False values, True = 1 , False = 0, If we use true or false instead of True or False, Python raises a NameError)

#Print values and their data types

print("Employee ID:", employee_id, type(employee_id))# print() - to display output
print("Name:", name, type(name))   #type() - to know the data type
print("Hourly Rate:", hourly_rate, type(hourly_rate))
print("Is Active:", is_active, type(is_active))


# Convert hourly_rate to integer

hourly_rate_int = int(hourly_rate) #int() converts a float to an integer by truncating the decimal part

print(hourly_rate_int, type(hourly_rate_int))

