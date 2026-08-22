## Écrivez votre code ici !
def square(n):
    """Calcule le carré d'un nombre.

    Args:
        n (int or float): Le nombre à mettre au carré.

    Returns:
        int or float: Le carré de n, ou None si n n'est pas un nombre.
    """
    if not isinstance(n, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return n ** 2


# Exemples d'utilisation
print(square(4))        # 16
print(square(2.5))      # 6.25
print(square("abc"))    # affiche l'erreur, puis None