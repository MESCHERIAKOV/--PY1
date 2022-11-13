import random
def get_unique_list_numbers() -> list[int]:
    list1 = [i for i in range(-10, 11, 1)] 
    random.shuffle(list1, random.random)
    random_values = list1[:15]
    return random_values

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

