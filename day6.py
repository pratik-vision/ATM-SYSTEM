pincode=1234
balance=10000
def check_balance(balance):
    print(balance)
def deposite(balance,amount):
    o=amount+balance
    print(o)
def withdraw(balance,amount):
    if amount > balance:
        print('insufficent fund ')
    else:
        o=amount-balance
        print('succesful')
        print('Current balance=',o)
while True:
    print('-------💳WELCOME TO MY ATM SYSTEM💳-----------------')





    i=int(input('.Enter the 4 digit pincode🔒='))
    if i == pincode:
      print('select 1.check balance\n2.deposiste\n3.withdraw')
      op=int(input('enter the choice='))
      if op == 1:
                check_balance(balance)
      elif op ==2:
                amount=int(input('enter amount='))
                deposite(balance,amount)
      elif op ==3:
                amount=int(input('enter amount='))
                withdraw(balance,amount)
      else:
                print('invalid try again')
    else:
            print('incorrect pincode❌ try again')
