from pathlib import Path
path = Path("C:/Users/Дел/Documents/My_repo/GOIT-ALGO-HW-04/path")
def total_salary(path):
    total_salary = 0
    num_developers = 0
    
    try:
        with open('path', 'r', encoding='utf-8') as file:
            for line in file:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None
    
    if num_developers == 0:
        print("Файл порожній.")
        return None
    
    average_salary = total_salary / num_developers
    return total_salary, average_salary

result = total_salary("path/to/salary_file.txt")
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
