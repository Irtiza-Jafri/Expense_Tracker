# Create a Python program that allows users to
# add, view, filter, analyze, and export their personal expenses using basic data structures and functions.

# This project should help you:

# Practice working with lists, dictionaries, and optionally tuples

# Apply user input, loops, conditionals, and functions

# Learn file handling

# Build a real-world, portfolio-worthy CLI application



"""
Welcome to Personal Expense Tracker!

1. Add New Expense
2. View All Expenses
3. Filter by Category
5. View Stats (Total, Avg, Max, Min)
6. Export Report to File
7. Exit
"""




Expenses=[]
#1. Add New Expense
def Add_Expnese():
    Date=input("Enter Date in (YYYY,MM,DD) Format : ")
    Money_Spent=int(input("Enter the amount you spent : "))
    Category=input("Enter Category where you spent your money : ")
    Note = input("Enter Note : ")
    
    
    Expense = {
        "date":Date,
        "money_spent" : Money_Spent,
        "category" :  Category ,
        "note" : Note
                   
    }
    
    Expenses.append(Expense)
    y="Expense and Data Added Successfully !"
    print(y)
    print("-"*len(y))
      
def View_expense():
    with open ("User_Data.txt") as f:
       for line in f:
           print(line)
            
# 6. Export Report to File
def Store_Data():
    with open("User_Data.txt","a") as f:
        for e in Expenses:
            temp=(f"\n{e['date']} | {e['money_spent']} Rs | {e['category']} | {e['note']}")
            f.write(temp)
        print("The Data Is Stored Successfully !")

# 3. Filter by Category
def Filter():
    Categ=str(input("Enter a suitable Category ,to search all Its Purchases : ").lower())
    Count = 0
    Total=0
    Found=False
        
    with open("User_Data.txt", "r") as file:
            
        print(f"\n Expenses In Category {Categ.title()}")
        print("-"* len(f"\n Expenses In Category {Categ.title()}"))
            
        for line in file:
            parts = line.strip().split(" | ")

                
                
            if (len(parts)>=4):
                    
                line_categ=parts[1].strip().lower()
                    
                if Categ== line_categ:
                    print(line.strip())
                        
                    try :
                          
                        amount_str = parts[2].replace("Rs.", "").strip()
                        amount = float(amount_str)
                        Total += amount
                        Count += 1
                        Found= True
                    except ValueError:
                        continue
                        
        if Found:
                print("-" * len(f"Expenses In Category {Categ.title()}"))
                print(f"The total amount spent On {Categ.title()} = {int(Total)}")
                print(f"Average amount spent = {round(Total/Count , 2)}")
                print("-"* len(f"\n Expenses In Category {Categ.title()}"))
        else :
                print("No amount spent on this Category ")
                
# 2. View All Expenses   
def View_All_Expenses():
    
    print("Your Recent Expense")
    print("-"*20)
    with open ("User_Data.txt","r") as f:
        
        for line in f:
            print(line)

# 5. View Stats (Total, Avg, Max, Min) 
def Stats():
    smallest=100000
    largest=-999
    Total_spent : int =0
    Avg : float =0
    Max : int =0
    Min : int =0
     
    count=0
    
    with open("User_Data.txt", "r") as file:
        
        for line in file:
            parts= line.strip().split(" | ")
             
            if len(parts)>=4:
                Money=parts[2].replace("Rs.", "")
                Total_spent += int(Money)
                count += 1
                
                if (int(Money)>largest):
                   largest=int(Money)
                   Max = int(Money)
                   
                if (int(Money)< smallest):
                    smallest=int(Money)
                    Min=int(Money)
                    
                    
        Avg=(Total_spent/count)
        
        print("-"* 40)
        print(f"The Total Money spent is : {Total_spent}")
        print("-"* 40)
        print(f"On an Average you spent : {round(Avg,2)}")
        print("-"* 40)
        print(f"The Max Amount spent is : {Max}")
        print("-"* 40)
        print(f"The Min Amount spent is : {Min}")
        print("-"* 40)
        
        

        

    
            
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. View Stats")
        print("5. Export to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Add_Expnese()
        elif choice == "2":
            View_All_Expenses()
        elif choice == "3":
            Filter()
        elif choice == "4":
            Stats()
        elif choice == "5":
            Store_Data()
        elif choice == "6":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid input. Try again.")

    
    
main()