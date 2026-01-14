#Exception Handling

def safe_productivity_score(tasks_completed, hours_worked):
    try:
    
        tasks_completed = int(tasks_completed)
        hours_worked = float(hours_worked)
        
        score = tasks_completed / hours_worked
        return score

    except ValueError:
        return "Please enter valid numeric values"

    except ZeroDivisionError:
        return "Denominator cannot be zero"

    except TypeError:
        return "Invalid data type provided"

tasks = input("Enter number of tasks completed: ")
hours = input("Enter hours worked: ")

print(safe_productivity_score(tasks, hours))
print(safe_productivity_score([], 5))# TypeError
print(safe_productivity_score('abc', 5))# ValueError



