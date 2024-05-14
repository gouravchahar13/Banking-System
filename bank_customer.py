from banking_system import bank

print("Welcome to Gourav's Bank :)")
print("We are happy to serve you")

#Registration
print('Lets begin wiith User Registration')
name=input("Enter your name:\t")
age=int(input("Enter your age:\t"))
city=input("Enter your city:\t")
Amt=int(input("Enter your Intial Amount:\t"))

#saving
Bk=bank.Bank(name,age,city,Amt)
Bk.save()

while(True):
    print("Welcome to Gourav's Bank :)")
    print('''Services we provide:
          1.Deposit Money
          2.Transact Money
          3.Display Amount
          4.Take Loan
          5.Make Fixed deposit
          6.Update details
          7.Exit
        ''')
    try:
        choice=(input("Enter your choice: "))
    except Exception as e:
        print(e)
        print("Invalid choice enter again")
        choice=(input("Enter your choice: "))
    choice=int(choice)
    match(choice):
        case 1:
            amt=int(input("Enter amount to be deposited:"))
            Bk.deposit(amt)
            continue
        case 2:
            amt=int(input("Enter amount to be taken out:"))
            Bk.transact(amt)
            continue
        case 3:
            Bk.display()
            continue
        case 4:
            print("Enter Loan amt,Interest Rate,Time")
            amt,IR,Time=(list(input().split(",")))
            Bk.Loan(amt,IR,Time)
            continue
        case 5:
            print("Enter F.D amt ")
            amt=(input())
            if(input("T>1?: ").lower()=="yes"):
                time=int(input("enter time in years:"))
                if(input("IR other than 7.5%: ").lower()=="yes"):
                    Ir=int(input("enter Ir in %: "))
                    Bk.Fixed_Deposit(amount=amt,Time=time,IR=Ir)
                else:
                    Bk.Fixed_Deposit(amount=amt,Time=time)
            else:
                Bk.Fixed_Deposit(amt)
            continue
        case 6:
            print("Currently under development")
            continue
        case 7:
            Bk.save()
            print("Thank you for using Gourav's Bank")
            print("Have a pleasent Day")
            print("Exiting.....\nHope to meet you soon")
            break