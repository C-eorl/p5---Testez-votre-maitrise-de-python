class BankAccount:
    def __init__(self, account_holder: str):
        self.account_holder = account_holder
        self.balance : float = 0.0

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Dépot de {amount} effectué")

    def withdraw(self, amount):
        if self.balance-amount < 0:
            print(f"Solde insuffisant")
            print(f"Solde disponible : {self.balance}")
        else:
            self.balance -=amount
            print(f"Retrait de {amount} effectué")

    def display_balance(self):
        print(f"Compte appartenant à {self.account_holder}")
        print(f"Solde : {self.balance}")

if __name__ == "__main__":
    b = BankAccount("Pierre")
    b.display_balance()
    b.withdraw(40.0)
    b.deposit(100.0)
    b.withdraw(20.0)
    b.display_balance()