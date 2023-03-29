from inventory.warehouse import warehouse_management

inventory = {}

print("   ")
print("***Welcome to Tucán.com***")
print("   ")
print("What would you like to do?")
print("   ")
print("Press 1 or 2")
print("   ")
print("1. Entry a Product")
print("2. Sale")
print("3. Exit")
option = int(input())

while True:
    if option == 1:
        warehouse_management(inventory)
    elif option == 2:
        print(" ")
        print("Not implemented yet")
        break
    elif option == 3:
        print("   ")
        print("Goodbye!")
        break 
    else:
        print("Select a valid option")
    
    print("***Welcome to Tucán.com***")
    print("   ")
    print("What would you like to do?")
    print("   ")
    print("Press 1 or 2")
    print("1. Entry a Product")
    print("2. Sale")
    print("3. Exit")
    option = int(input())
