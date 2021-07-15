from abc import ABCMeta, abstractmethod
from random import seed
from random import randint


class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount:
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been successful. Your account number is ",self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentification Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentification Failed")
                return False
        else:
            print("Authentification Failed")
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdraw Successful")
            self.displayBalance()
            print()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()
        print()

    def displayBalance(self):
        print("Available balance: ", self.savingsAccounts[self.accountNumber][1])


savingsAccount = SavingsAccount()
while True:
    print()
    print("Enter 1 to create a new acount")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice == 2:
        print("Enter your name")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authentificationStatus = savingsAccount.authenticate(name, accountNumber)
        if authentificationStatus == True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menus")
                userChoice = int(input())
                if userChoice == 1:
                    print("Enter a withdrawl amount")
                    withdrawlAmount = int(input())
                    savingsAccount.withdraw(withdrawlAmount)
                elif userChoice == 2:
                    print("Enter the amount to be depositied")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccount.displayBalance()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
            quit()
