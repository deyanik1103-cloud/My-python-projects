balance=1000

print ("Welcome to the ATM")
while True:
    print("Please select an option: ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        print("Your balance is:", balance)
    elif choice=="2":
        amount=float(input("Enter the amount to deposit:"))
        balance+=amount
        print("Your new balance is:",balance)
    elif choice=="3":
        amount=float(input("Enter the amount to withdraw: "))
        if amount<=balance:
            balance-=amount
            print("Your new balance is:", balance)
        else:
            print("Insufficient funds")
    elif choice=="4":
        print("Thank you for using the ATM. Goodbye!")
        break