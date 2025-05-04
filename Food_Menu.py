print("WELCOME TO MY FOOD MENU!")

print("Please select what type of food from the menu below")


print("Dishes:\n(1)American\n(2)Indian\n(3)Chinese\n(4)Italian\n(5)Mexican")


try:
    choice = int(input("Choose your dish:").strip())
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()



American = {
    "Cheeseburger":10.99,
    "French Fries":5.99,
    "Soda":1.99,
    "Hot Dog": 15.99,
    "Ceaser Salad":10.99
}
Indian = {
    "Rice":1.99,
    "Naan":5.99,
    "Mango Lassi":1.99,
    "Butter Chicken": 15.99,
    "Daal":10.99
}
Italian = {
    "Fettucini Alfredo":19.99,
    "Cheese pizza":20.99,
    "Gnnochi":15.99,
    "Negroni": 105.99,
    "Shrimp Scampi":21.99
}
Chinese = {
    "Lo Mein":10.99,
    "Orange Chicken":15.99,
    "Kung Pao Chicken":12.99,
    "Dumplings": 5.99,
    "Fried Rice":10.99
}
Mexican = {
    "Chips and Salsa":4.99, 
    "Tacos":10.99,
    "Enchiladas":10.99,
    "Burrito": 15.99,
    "Quesadilla":10.99
}


menu = None
if choice == 1:
    menu = American
elif choice == 2:
      menu = Indian
elif choice == 3:
  menu = Italian
elif choice == 4:
   menu = Chinese
elif choice == 5:
 menu = Mexican
else:
    print("Invalid selection.")
    exit()   
    
    
    

print(f"HERE IS THE MENU FOR:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")  
    
    
food_decision = input("What would you like from this Selection?").strip()


ORDER = [item.strip().title() for item in food_decision.split("and")]


total = 0
found = []
not_found = []

for item in ORDER:
    if item in menu:
        total += menu[item]
        found.append(item)
    else:
        not_found.append(item)
        
        
if found:
    print(f"\nYou ordered: {', '.join(found)}")
    print(f"Total price: ${total:.2f}")
if not_found:
    print(f"Sorry, we don't have: {', '.join(not_found)}")



    

    