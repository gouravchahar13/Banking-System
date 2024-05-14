import os
class Bank():
    name=None
    age=None
    city=None
    amount=None

    # Intialisation
    def __init__(self,name,age,city,sal):
        self.name=name
        self.age=int(age)
        self.city=city
        self.amount=int(sal)
    def save(self):
        #save details
        f=open(f"./{self.name}.txt","w")
        f.write(f"Name: {self.name}\nAge:{self.age} \nCity:{self.city} \nAmount:{self.amount}")
        f.close()
    #display
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("City: ",self.city)
        print("Amount",self.amount)

    # Update functions
    def update_amount(self,sal):
        self.amount=sal
    def update_age(self,age):
        self.age=age
    def update_name(self,name):
        self.name=name
    def update_city(self,city):
        self.city=city

    # annual increments:
    #schedule library learn
    def annual_increment(self):
        pass
    
    # deposit
    def deposit(self,amt):
        self.amount+=amt
        print("The current ammount is:",self.amount)
    
    #transact
    def transact(self,amt):
        self.amount-=amt
        print("The current amount is:",self.amount)
    
    #Loan
    def Loan(self,Sum,IR,Time):
        Sum=int(Sum)
        IR=int(IR)
        Time=int(Time)
        Interest=(Sum*IR*Time)/100
        #schedule use deduct this from the amount
        self.amount-=Interest
        print("the amt for loan interest deducted from your acc is:",Interest)
        print("The current amount is:",self.amount)

    def salary(self,sal,institution):
        #schedule use increment  the amount to acc
        self.amount+=sal
        print(f"An amount of {sal} is creditied to your acc by {institution}")

    def Fixed_Deposit(self,amount,Time=1,IR=7.5):
        amount=float(amount)
        Time=float(Time)
        if(amount>self.amount):
            print("the amount for F.D should be less than acc balance")
            print("please choose make the coorect choice next time")
            return 
        self.amount+=(amount*Time*IR)/100
        print(f"The current amt after F.D is {self.amount}")