class Category:
    def __init__(self,name,ledger=[],Total = 0,Total_withdraw = 0) :
        self.name = name
        self.ledger = []
        self.Total = Total
        self.Total_withdraw = Total_withdraw

    def __str__(self) :
        title_name = self.name.center(30,"*") 
        
        liste =""
        i = 0
        while i < len(self.ledger):
            liste += f"{self.ledger[i]['description'][0:23]: <23}{(self.ledger[i]['amount']):>7.2f}"
            i += 1
            if i < len(self.ledger) :
                liste += "\n"
            

        return f"{title_name}\n{liste}\nTotal: {self.Total}"
    
    def deposit (self,deposit_amount,deposit_description = "") :

        self.Total += deposit_amount
        
        new_deposit = {f"amount" : deposit_amount, "description" : deposit_description}
        self.ledger.append(new_deposit)
        
        
    def withdraw (self,withdraw_amount,withdraw_description = "") :

        if self.check_funds(withdraw_amount) == False :
            
            return False
        
        elif self.check_funds(withdraw_amount) == True :

            self.Total -= withdraw_amount
            self.Total_withdraw += withdraw_amount

            withdraw_amount = withdraw_amount*-1

            new_withdraw = {"amount" : withdraw_amount, "description" : withdraw_description}
            self.ledger.append(new_withdraw)
            
            
            return True
        
        else :

            return False

    def get_balance (self):
        
        return self.Total

    def transfer (self,transfer_amount,Category) :
        
        if self.check_funds(transfer_amount) == True :

            self.withdraw(transfer_amount,f"Transfer to {Category.name}")

            Category.deposit(transfer_amount,f"Transfer from {self.name}")            
            return True
        else :

            return False

    def check_funds (self,check_amount) :
  
        if check_amount > self.Total :

            return False
        
        elif check_amount <= self.Total :

            return True
        
        else :

            return False

def create_spend_chart(categories):
    
    total_spend = 0
    x = 0
    percentage = []
    name_list = []
    while x < len(categories) :

        total_spend += categories[x].Total_withdraw
        
        x+=1
    y = 0

    while y < len(categories) :
        name_list += [categories[y].name]
        percentage += [(categories[y].Total_withdraw/total_spend)*100] 
        y+=1
      
    chart = "Percentage spent by category\n"
    

    for i in range (100,-1,-10):
        chart += str(i).rjust(3) + "| "
        for percent in percentage :
            if percent >= i :
                chart += "o  " 
            else : 
                chart += "   "
        
        chart += "\n"
    
    chart += "    ----------\n"
    
    max_len_name = max(len(c.name) for c in categories) 
    
    for l in range(max_len_name):

        chart += "     "

        for letter in name_list :
        
        
            if l < len(letter) :
                chart += letter[l] + "  "

            else :

                chart += "   "
        
        if l < max_len_name -1 :
            chart += "\n"
        
    return chart

    

    


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food.ledger)
print(food)

