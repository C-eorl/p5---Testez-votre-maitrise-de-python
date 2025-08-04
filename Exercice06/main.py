# Fonction calculate_average
def calculate_average(list_number: list[int]):
    return sum(list_number)/len(list_number)

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
