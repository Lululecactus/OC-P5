def calculate_average(numbers):
    """Calcule la moyenne d'une liste de nombres.

    Args:
        numbers (list): Une liste de nombres (int ou float).

    Returns:
        float: La moyenne des nombres. Renvoie 0 si la liste est vide.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)