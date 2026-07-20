foods = []
choice = 0
while choice != 4:
  
  print("1.Donate Food")
  print("2.View Food")
  print("3.Search Food")
  print("4.Exit")
  choice =int(input("Ënter your choice : "))
  if choice == 1:
    print("Donate Food")
    Food_Name = input("Enter your Food name: ")
    Quantity = input("Enter your food quantity: ")
    Category = input("Enter your food category: ")
    Location = input("Enter your Location: ")
    
    food={
        "Food_Name" : Food_Name,
        "Quantity" : Quantity,
        "Category": Category,
        "Location" : Location
    }

   
    foods.append(food)
    print(foods) 

    print("All foods added successfully")

  
#View foods
  elif choice ==2:
    print("View food")
    
    if foods == []:
        print("No,food yet added")
    else:
        print(f"Here is all donated food items")
        for food in foods:
            print(food)
        
        
        
        
        

  elif choice == 3:
    found = False
    print("Search food")
    category_search = input("Enter your category_search: ")
    
     
    for food in foods:
    
        if food["Category"] == category_search:
            print(food)
            found = True
        
    if found == False:
        print("Not found here")   
    

  elif choice == 4:
    print("Exit")

  else:
    print("Thank you for using Community Food Sharing System.")
    


