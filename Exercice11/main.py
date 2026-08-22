## Écrivez votre code ici !
class BankAccount:
    """Représente un compte bancaire simple."""

    def __init__(self, account_holder, balance=0.0):
        """Initialise le compte bancaire.

        Args:
            account_holder (str): Le nom du titulaire du compte.
            balance (float): Le solde initial du compte (par défaut 0).
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Dépose de l'argent sur le compte.

        Args:
            amount (float): Le montant à déposer. Doit être positif.
        """
        if amount <= 0:
            print("Le montant du dépôt doit être positif.")
            return
        self.balance += amount
        print(f"Dépôt de {amount} effectué avec succès.")

    def withdraw(self, amount):
        """Retire de l'argent du compte.

        Args:
            amount (float): Le montant à retirer. Doit être positif
                et inférieur ou égal au solde disponible.
        """
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
            return
        if amount > self.balance:
            print("Fonds insuffisants pour ce retrait.")
            return
        self.balance -= amount
        print(f"Retrait de {amount} effectué avec succès.")

    def display_balance(self):
        """Affiche le solde et le nom du titulaire du compte."""
        print(f"Compte de {self.account_holder} - Solde : {self.balance}")


# Test
account = BankAccount("Alice", 100)
account.display_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)  # refusé : fonds insuffisants
account.display_balance()