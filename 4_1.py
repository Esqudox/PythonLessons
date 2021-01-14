from sys import argv

file_name, salary, time, bonus = argv

def salary_calc():

    salary = int(salary)
    time = int(time)
    bonus = int(bonus)
    total_salary = salary * time + bonus
    print(f'Total salary for this month is - {total_salary}')


salary_calc()