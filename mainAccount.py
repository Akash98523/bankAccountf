import datetime

class Account:
    pin =0000
    balance = 0
    pin_data=[1111,2222,3333,4444]

    def __init__(self,_pin):
        self._pin=_pin
        #self.balance=0

    def Validate_pin(self):
        flag=0
        for x in self.pin_data:
            if x == self._pin:
                flag=1
                return True
                break
        if flag==0:
            return False


    def deposit(self,amount):
        self.amount=amount
        self.balance += amount 
        print("amount deposited:",amount)
        x=Transaction_History("Money deposite")
        x.Record_tr_details(amount)
        tr=Transaction_History("")
        self.balance=tr.read_bankdata()
        new_balance=int(self.balance)+amount
        file=open("bankdata.txt","w")
        file.write(str(new_balance))
        print("Transition completed")

    def withdraw(self,amount):
        tr=Transaction_History("")
        self.balance=tr.read_bankdata()
        self.amount= amount
        
        if int(self.balance)>= int(amount):
            current_balance=int(self.balance)
            current_balance -=amount
            #self.balance-= amount
            print("amount withdrawn:",amount)
            x=Transaction_History("Money withdrawn")
            x.Record_tr_details(amount)
            tr=Transaction_History("")
            self.balance=tr.read_bankdata()
            new_balance=int(self.balance)-amount
            file=open("bankdata.txt","w")
            file.write(str(new_balance))
            print("Transition completed")
        else:
            print("insufficient balance")

    def check_balance(self):
        tr=Transaction_History("")
        self.balance=tr.read_bankdata()
        print("Current balance:",self.balance)
        print("Transition complete")
        

class CheckingAccount(Account):
    def __init__(self,_pin):
        super(CheckingAccount,self).__init__(_pin)
        
    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def check_balance(self):
        return super().check_balance()

class SavingAccount(Account):
    def __init__(self,_pin):
        super(SavingAccount,self).__init__(_pin)

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def check_balance(self):
        return super().check_balance()
        

class BusinessAccount(Account):
    def __init__(self,_pin):
        super(BusinessAccount,self).__init__(_pin)

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def check_balance(self):
        return super().check_balance()

    
class Transaction_History:
    current_time_date =""
    transaction_mode=""
    def __init__(self,tr_mode):
        self.current_time_date=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.transction_mode=tr_mode
        #self.amount=amount

    def Record_tr_details(self,amount):
        file=open("Tr_history.txt","a+")
        file.write("Date Time:" + str(self.current_time_date)  + " " + "Transction_mode:" + self.transaction_mode + " " + str(amount) +"\n" )

    def Show_transaction_history(self):
        file=open("Tr_history.txt","r")
        data=file.read()
        print(data)
        file.close()
    def read_bankdata(self):
        file=open("bankdata.txt","r")
        data=file.read()
        file.close()
        return data

class Atm_Logic:
    def __init__(self,message):
        print(message)
        print("-------------Welcome------------")

    def CheckingAccount_Functions(self,pin):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")
        option = str(input("Please select one of the above:"))
        if option != "":
            Chk = CheckingAccount(pin)
            if option == "1":
                Chk.check_balance()
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Chk.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
                Chk.withdraw(amount)
            elif option == "4":
                tr = Transaction_History("")
                tr.Show_transaction_history()
            elif option == "5":
                print("Thank You!!")

    def SavingAccount_Functions(self,pin):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")

        option = str(input("Please select one of the above:"))
        if option != "":
            Svg = SavingAccount(pin)
            if option == "1":
                Svg.check_balance(pin)
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Svg.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
                Svg.withdraw(amount)
            elif option == "4":
                tr = Transaction_History("")
                tr.Show_transaction_history()
            elif option == "5":
                print("Thank You!!")

    def BusniessAccount_Functions(self,pin):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")

        option = str(input("Please select one of the above:"))
        if option != "":
            Bsg = BusinessAccount(pin)
            if option == "1":
                Bsg.check_balance(pin)
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Bsg.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
                Bsg.withdraw(amount)
            elif option == "4":
                tr = Transaction_History("")
                tr.Show_transaction_history()
            elif option == "5":
                print("Thank You!!")


    

        


    



    






    
        

        
