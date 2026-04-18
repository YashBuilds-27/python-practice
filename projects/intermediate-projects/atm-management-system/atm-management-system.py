# M O D U L E S
import json
import datetime as dt

# U T I L I T Y      F U N C T I O N S

def load_accounts():
    global accounts
    try:
        with open("accounts.json",'r') as file:
            accounts=json.load(file)
    except FileNotFoundError:
        print("\nNO ACCOUNTS EXISTS...CREATE ONE FIRST!\n")
        accounts={}

def check(acc,pin):
    if len(acc)==10 and len(pin)==4:
            return True
    else:
        print("\n(X)    INVALID DETAILS ENTERED    (X)\n")

def trans(acc,msg,amount):
    time=f"{dt.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} | {msg}: Rs. {amount}\n"
    with open(acc+'.txt','a') as file:
        file.write(time)

def save_bal(acc):
    with open('accounts.json','w') as file:
        json.dump(acc,file)

# L O G I N      F U N C T I O N S

def balance(acc):
    print(f"\nAvailable balance: Rs. {accounts[acc]['bal']}\n")
    trans(acc,"Balance checked",accounts[acc]['bal'])
    
def deposit(acc):
    try:
        amt=float(input("Enter amount (Rs.):"))
        if amt<=0:
            print("\nZero or No Ammount Entered\n")
        else:
            accounts[acc]['bal']+=amt
            save_bal(accounts)
            print(f"\nRs. {amt} deposited to Account No. {acc}\n")
            trans(acc,"Amount Deposited",amt)
    except ValueError:
        print("\nINVALID AMOUNT ENTERED\n")

def withdraw(acc):
    try:
        amt=float(input("Enter amount (Rs.):"))
        if amt<=0:
            print("\nZero or No Ammount Entered\n")
        elif amt > accounts[acc]["bal"]:
            print("\nInsufficient Balance\n")
        else:
            accounts[acc]["bal"]-=amt
            save_bal(accounts)
            print(f"\nRs. {amt} withdrawn from Account No. {acc}\n")
            trans(acc,"Amount Withdrawn",amt)
    except ValueError:
        print("\nINVALID AMOUNT ENTERED\n")

def history(acc):
    try:
        with open(acc + '.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                print("\nNo transactions found.\n")
            else:
                print("\nLast Transactions:\n")
                for line in lines[-5:]:
                    print(line)
    except FileNotFoundError:
        print("\nNo transaction history found.\n")

# M E N U    F U N C T I O N S

def create():
    try:
        print("""\n**********NOTE**********
1. ACCOUNT NUMBER MUST BE OF "10" DIGITS
2. PIN MUST BE OF "4" DIGITS\n""")
        name=input("Enter account holder's name:")
        account=input("Enter account number:")
        pin=input("Entered 4 digit pin:")
        if check(account,pin) and account not in accounts :
            with open("accounts.json",'w') as file:
                new_account={account:{"pin":pin,"name":name,"bal":0.0}}
                accounts.update(new_account)
                json.dump(accounts,file)
            print("\nACCOUNT CREATED SUCCESSFULLY\n")
            return load_accounts()
        else:
            print("\nACCOUNT ALREADY EXITS\n")
    except ValueError:
        print("\n(X)    INVALID DETAILS ENTERED    (X)\n")

def login():
    try:
        account=input("\nEnter account number:")
        pin=input("Entered 4 digit pin:")
        if check(account,pin) and accounts[account]["pin"]==pin:
            print("\nLOGIN SUCCESSFUL\n")
            while True:
                print(f"""======= {accounts[account]['name']}'s Account =======
1. Check Balance
2. Add money
3. Withdraw money
4. Transaction History
5. Log out
==============================""")
                ch=input("Enter choice:")
                if ch=='1':
                    balance(account)
                elif ch=='2':
                    deposit(account)
                elif ch=='3':
                    withdraw(account)
                elif ch=='4':
                    history(account)
                elif ch=='5':
                    print("\nLOGOUT SUCCESSFUL   (* ^ *)\n")
                    break
                else:
                    print("\n(X)  INVALID CHOICE  (X)\n")
    except ValueError:
        print("\n(X)    INVALID ACCOUNT NUMBER ENTERED    (X)\n")
        return menu()
    
# A T M     M E N U

def menu():
    while True:
        print("""========== ATM MENU ==========
1. Create new account
2. Login
3. Exit
==============================""")
        ch=input("Enter choice:")
        if ch=='1':
            create()
        elif ch=='2':
            login()
        elif ch=='3':
            print("\nThankyou for visiting us   (* ^ *)")
            break
        else:
            print("\n(X)  INVALID CHOICE  (X)\n")

load_accounts()
menu()
