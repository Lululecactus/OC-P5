class Rectangle:
    """Représente un rectangle défini par sa largeur et sa longueur."""

    def __init__(self, width, length):
        """Initialise le rectangle.

        Args:
            width (int or float): La largeur du rectangle.
            length (int or float): La longueur du rectangle.
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """Calcule l'aire du rectangle.

        Returns:
            int or float: L'aire (largeur * longueur).
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            int or float: Le périmètre (2 * (largeur + longueur)).
        """
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
rectangle = Rectangle(5, 3)  # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())