## Écrivez votre code ici !
class Person:
    """Représente une personne définie par son nom et son âge."""

    def __init__(self, name, age):
        """Initialise la personne.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.name = name
        self.age = age

    def display_details(self):
        """Affiche le nom et l'âge de la personne."""
        print(f"Nom : {self.name}, Âge : {self.age}")


class Employee(Person):
    """Représente un employé, qui est une Person avec un salaire en plus."""

    def __init__(self, name, age, salary):
        """Initialise l'employé.

        Args:
            name (str): Le nom de l'employé.
            age (int): L'âge de l'employé.
            salary (int or float): Le salaire de l'employé.
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """Affiche les détails de l'employé, salaire inclus."""
        super().display_details()
        print(f"Salaire : {self.salary}")


# Test
person = Person("Alice", 30)
person.display_details()

employee = Employee("Bob", 25, 3000)
employee.display_details()