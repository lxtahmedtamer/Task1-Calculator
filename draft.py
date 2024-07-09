class Coffee_VM:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.x = 0  # indicator for coffee type
        self.money_rest=0 #indicator for money difference for the client
        print("WELCOME TO THE COFFEE VENDING MACHINE:")
       
    def display_menu(self):
        # MENU DISPLAY
        print("The Menu is as the following:")
        self.coffees = {
            1: {'name': 'Nescafe', 'price': 20},
            2: {'name': 'Latte', 'price': 30},
            3: {'name': 'Cappuccino', 'price': 35},
            4: {'name': 'Mocha', 'price': 40}
        }
    
        for key, value in self.coffees.items():
            print(f"{key}: {value['name']} - {value['price']}")
            
            
    def select_coffee(self):
        self.x=int(input("Choose a number from 1 to 4:"))
        while self.x<1 or self.x>4:
            self.x=int(input("Sorry,Please Enter a Valid number from 1 to 4:"))
        
        else:
            return self.x

    def payment(self):
       
        
        amount = float(input("Please insert money : "))
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount. "))
        if(self.x==1):
            self.price=20
            while(amount<20):
                 amount = float(input("Please insert money applicable to buy Nescafe : "))
        elif(self.x==2):
            self.price=30
            while(amount<30):
                 amount = float(input("Please insert money applicable to buy Latte : "))
        elif(self.x==3):
            self.price=35  
            while(amount<35):
                 amount = float(input("Please insert money applicable to buy Cappucino: "))      
        elif(self.x==4):
            self.price=40
            while(amount<40):
                 amount = float(input("Please insert money applicable to buy Mocha: "))
        #PROCESS FINISHED                
        self.money_rest =amount-self.price
        print("Thank you for using the Coffee Vending Machine!")   
        print("Your rest of money =",self.money_rest)
        
    
    def last_phase(self):
        self.display_menu()
        self.x = self.select_coffee()
        self.payment()

#Creating an instance for the class    
vending_machine = Coffee_VM()
vending_machine.last_phase()
