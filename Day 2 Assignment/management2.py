#2.3 Unique Skills Using Sets

# method 1

employee_skills = {"Python", "SQL", "Communication", "Teamwork"}#Create a set of employee skills

employee_skills.add("Leadership")
employee_skills.add("Time Management")#Add two new skills to the set

print(employee_skills)#Print the final set of skills

#method 2
employee_skills = {"Python", "SQL", "Communication", "Teamwork"}#Create a set of employee skills

employee_skills.update(['Leadership', 'Time Management'])#Add two new skills to the set

print(employee_skills)#Print the final set of skills

#method 3

employee_skills = {"Python", "SQL", "Communication"}#Create a set of employee skills

new_skills = ["Leadership", "Time Management"]

for skill in new_skills:
    employee_skills.add(skill)  # Add two new skills to the set

print(employee_skills)
