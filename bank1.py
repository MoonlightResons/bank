class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Вы успешно пополнили баланс на: {amount}')
        print(f'Ваш текущий баланс: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Вы успешно сняли деньги с баланса на сумму: {amount}')
            print(f'Ваш текущий баланс равен: {self.balance}')
        else:
            print('Недостаточно средств на счете')

    def information(self):
        print(f'Имя владельца кошелька: {self.owner}')
        print(f'На данный момент баланс кошелька составляет: {self.balance}')        


choice = None #Здесь я пытался сохранить баланс после каждого выбора, немного по верстав интернет нашел такое решение, достаточно сильно замучался со всем этим что здесь было, после написания так же потратил 30-40м на оптемизацию кода, изначальный код снизу закоментирован
balance = 0

while True:
    move = int(input("Выберите, что вы хотите сделать:\n1 - Пополнить баланс\n2 - Снять деньги со счета\n3 - Проверить кошелек\n"))

    if choice is not None:
        print("Предыдущий выбор:", choice)

    if move == 1:
        deposit_amount = int(input("Введите сумму, на которую хотите пополнить баланс: "))
        account = BankAccount('Owner', balance)
        account.deposit(deposit_amount)
        balance = account.balance

    elif move == 2:
        withdraw_amount = int(input("Введите сумму, которую хотите снять со счета: "))
        account = BankAccount('Owner', balance)
        account.withdraw(withdraw_amount)
        balance = account.balance
        
    elif move == 3:
        name_of_owner = input("Введите ваше имя: ")
        account = BankAccount(name_of_owner, balance)
        account.information()

    return_choice = input("1 - Вернуться на главную, 0 - Выход: ")

    if return_choice == "0":
        break

    choice = move

# balance = 0

# class BankAccount:
#         def __init__(self, owner, balance, withdraw):
#             self.owner = owner
#             self.balance = balance
#             self.withdraw = withdraw

#         def deposit(self):
#             balance = 0 + deposit_balance
#             print(f'Вы успешно пополнили баланс на: {balance}')
#             print(f'Ваш нынешний баланс: {balance}')
#             return balance
        
#         def withdraw_balance(self):
#             balance = - withdraw
#             print(f'Вы успешно сняли деньги с баланса на сумму: {withdraw}')
#             print(f'Ваш нышний баланс равен: {balance}')

#         def information(self):
            
#             owner = name_of_owner
#             print(f"Имя владельца кошелька - {name_of_owner}")
#             print(f"На данный момент баланс кошелька составляет: {balance}")


# class Owner(BankAccount):
#     def __init__(self,owner,balance):
#         BankAccount.__init__(self,owner, balance, withdraw=balance)

# choice = None

# while True:
#     move = int(input("Выберите пожалуйста что вы хотите сделать: 1 - Пополнить баланс, 2 Снять деньги со счета, 3 Проверить кошелек: "))

#     if choice is not None:
#         print("Предыдущий выбор:", choice)


#     if move == 1:
#         deposit_balance = int(input("На сколько денег вы хотите пополнить баланс: "))
#         vana = Owner('Owner', 'balance')
#         vana.deposit()
#         vana.balance
        
#     if move == 2:
#         withdraw = int(input("Введите число денег которое вы хотели бы вывести: "))
#         vana = Owner('Owner' 'balance')
#         vana.withdraw_balance()
#         vana.balance

#     if move == 3:
#         name_of_owner = (input("Введите пожалуйста ваше имя: "))
#         vana = Owner(name_of_owner, 'balance')
#         vana.information()
#         vana.balance

#     return_choice = input("1 - Вернуться на главную, 0 - Выход: ")

#     if return_choice == "0":
#         break

# balance = 0 + deposit_balance


# choice = move and move2