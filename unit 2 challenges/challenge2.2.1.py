class BankAccount:

  def __init__(self,account_number,account_holder_name,initial balance =0.0):

    self.__account_number = account_number

    self.__account_holder_name = account_holder_name

    self.__account_balance = initial_balance

  def deposit(self, amount):

    if amount > 0

      self.__acount_balance += amount

      print("Deposited ₹{}. New balance: ₹{}".format(amount,self,.__account_balance))

    else:

      print("Invalid deposit amount. Please deposit a positive amount.")

  def wothdraw(self,amount):

    if amount > 0 and amount <= self.__account_balance:

      self.__account_balance -= amount

      print("withdraw ₹{}. New balance: ₹{}".format(amount, self.__account_balance))

    else:

      print("Invalid withdrawl amount or insufficient balance.")

  def display_balance(self):

      print("Account balance for {} (Account #{}".format(

        self.__account_holder-name, self.__account_number,

        self.__account_balance))

 

account = BankAccount(account_number="987654321",

                     accounth_holder_name="Ramya",

                     account_balance= 1000.0)

 

account.display_balance()

account.deposit(500.0)

account.withdraw(100.0)

account.display_balance()