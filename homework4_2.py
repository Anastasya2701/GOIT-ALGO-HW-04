from pathlib import Path
path = Path("C:/Users/Дел/Documents/My_repo/GOIT-ALGO-HW-04/cats_file.txt")

def get_cats_info(path):

  try:
    with open(path, 'r') as file:
      cats_info = []
      for line in file:
        cat_info = line.strip().split(',')
        cat_dict = {
          "id": cat_info[0],
          "name": cat_info[1],
          "age": cat_info[2]
        }
        cats_info.append(cat_dict)
      return cats_info
  except FileNotFoundError as e:
    print(f"Помилка! Файл не знайдено: {e}")
    return []
  except Exception as e:
    print(f"Помилка! Неочікувана помилка: {e}")
    return []
cats_info = get_cats_info("C:/Users/Дел/Documents/My_repo/GOIT-ALGO-HW-04/cats_file.txt")
print(cats_info)
