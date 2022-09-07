# Parent Class: User - Holds details about an user - has a function to show user details
# Child Class: Bank - Stores details about the account balance - Stores details about the amount -
# Allows for desposits, withdraw, view balance

# Parent class User
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Details')
        print('')
        print('Name ', self.name)
        print('Age ', self.age)
        print('Gender ', self.gender)


# Child Class Bank
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Account balance has been updated : €', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance available: €", self.balance)
        else:
            self.balance -= self.amount
            print('Account balance has been updated: €', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance is: €', self.balance)


