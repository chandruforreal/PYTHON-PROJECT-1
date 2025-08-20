print("WELCOME TO ZLAZO ATM")

try:
  pin=int(input("ENTER YOUR PIN: "))
  if pin==1234:
    print("YOUR PIN GRANTED")
    
    balance=1000
    
    
    while True:
      print("\n atm menu")
      print("1.check balance")
      print("2.deposite money")
      print("3.withdraw money")
      print("4.exit")
      
      try:
        
        choice=int(input("ENTER A NUMBER FROM THE MENU: "))
        if choice==1:
          print("your balance is",balance)
        elif choice==2:
          deposite=int(input("ENTER YOUR AMOUNT: "))
          balance+=deposite
          print("YOUR FINAL BALANCE AFTER DEPOSITE",balance)
        elif choice==3:
          withdraw=int(input("ENTER THE AMOUNT TO WITHDARW: "))
          if withdraw<=balance:
            balance-=withdraw
            print("YOUR BALANCE AFTER WITHDAWR",balance)
          else:
            print("your balance is insufficient")
        elif choice==4:
          print("THANKS FOR VISTING COME AGAIN")
          break
        else:
          print("PLEASE ENTER THE RIGGHT NUMBER BETWEEN 1 - 4")
      except ValueError:
        print("ENTER A NUMBER BETWEEN 1-4 PLEASE")
          
            
  else:
    print("ENTER THE CORRECT PIN")
except ValueError:
  print("ENTER YOUR PIN")