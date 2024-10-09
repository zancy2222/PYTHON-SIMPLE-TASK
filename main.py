print("\033[38;5;37m===================================================================================\033[0m")
print("                      Welcome to \033[38;5;10mMERS FOODS AND DELICACIES! \033[0m ")
print('                                  Created by:')
print("                                \033[38;5;35mGROUP 1 (A143) ")
print("                            Arellano, Carl Angelo G.")
print("                            Cago, Francis Elijah L. ")
print("                               Piastro, James A.  ")
print("                            Tamesis, Austin Mhar S.   ")
print("\033[38;5;37m===================================================================================\033[0m")
print("                                 DESCRIPTION")
print("Home to the finest, tastiest, and healthiest native food in the south. The City of")
print("Digos' sparkling gem. Mers Foods and Delicacies offers diverse range of snacks and")
print("desserts that highlight the rich culinary heritage of the Philippines.")
print("")
print("This program acts as an inventory system in which pasalubong foods are displayed.")
print("It also functions as a cash register, receiving orders and payments, and printing")
print("receipts for the customers' overall orders.")
print("\033[38;5;37m===================================================================================\033[0m")

while True:
    input_yes = input("Type {YES} to start the program or {NO} to exit: ").upper()
    if input_yes == "YES":
        import inventory
        inventory.shopping()
        break
    elif input_yes == "NO":
        print("")
        print("\033[38;5;37m===================================================================================\033[0m")
        print("")
        print("                   Thank you for visiting \033[38;5;10mMERS FOODS AND DELICACIES! \033[0m ")
        print("                       We hope to serve you well next time!")
        print("")
        print("\033[38;5;37m===================================================================================\033[0m")
        exit()
    else:
        print("")
        print("\033[38;5;37mInvalid input! Please type YES or NO.\033[0m")
        print("")