import datetime

inventory = {
    1: "Bibingka", 2: "Puto Sa Dahon", 3: "Plain Suman", 4: "Nilambiran",
    5: "Moron", 6: "Cassava Suman", 7: "Tupig", 8: "Espasol", 9: "Puto Bignas",
    10: "Calamay", 11: "Puto Maya", 12: "Sapin-Sapin", 13: "Biko", 14: "Ube Halaya",
    15: "Ube Rice Cake", 16: "Maja Blanca", 17: "Kutsinta", 18: "Cassava Cake"
}

prices = {
    1: 110.00, 2: 110.00, 3: 80.00, 4: 55.00, 5: 55.00, 6: 70.00, 7: 75.00, 8: 70.00,
    9: 75.00, 10: 80.00, 11: 65.00, 12: 75.00, 13: 75.00, 14: 105.00, 15: 105.00,
    16: 85.00, 17: 100.00, 18: 115.00
}

order = []
special_deals = ["Buy one get one free on Bibingka", "10% discount on Puto Sa Dahon",
                 "Free delivery on orders over PHP 1000"]

def read_stock_from_file(filename):
    stock = {code: {'product': product, 'quantity': 0} for code, product in inventory.items()}
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            code, product, quantity = line.strip().split(',')
            stock[int(code)]['quantity'] = int(quantity)
    return stock


def write_stock_to_file(filename, stock):
    with open(filename, 'w') as f:
        for code, product_info in stock.items():
            f.write(f"{code},{product_info['product']},{product_info['quantity']}\n")


stock_filename = 'stock.txt'
stock = read_stock_from_file(stock_filename)

if 1 in stock:
    stock[1]['quantity'] = 25
if 5 in stock:
    stock[5]['quantity'] = 10

write_stock_to_file(stock_filename, stock)


def print_receipt(items, customer_name, cash_paid):
    filename = f"receipt_{customer_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'w') as f:
        f.write("================================ RECEIPT ================================\n")
        f.write("                           MERS NATIVE DELICACIES                        \n")
        f.write("=========================================================================\n")
        f.write("                        THIS IS THE OFFICIAL RECEIPT                    \n")
        f.write("=========================================================================\n")
        f.write("Facebook: MersfoodsAndDelicaciesinc\n")
        f.write("Instagram: Mersdelicacies.1975\n")
        f.write("Email: merskitchenette1975@gmail.com\n\n")

        f.write(f"SOLD TO: {customer_name}\n")
        f.write("---------------------------------------------------------------------------\n")
        f.write("ITEMS                  QUANTITY      PRICE              SUB-TOTAL   \n")

        total_cost = 0
        for item, quantity, item_total, _ in items:
            f.write(f"{item:<20}{quantity:>5}{item_total:>18,.2f}\n")
            total_cost += item_total

        f.write("........................................................................\n")
        f.write(f"                                                       TOTAL       {total_cost:,.2f}\n")
        f.write("============================================================================\n")
        f.write(f"AMOUNT PAID: PHP {cash_paid:,.2f}\n")
        f.write(f"CHANGE: PHP {(cash_paid - total_cost):,.2f}\n")
        f.write("           THANK YOU FOR SHOPPING AT MERS NATIVE DELICACIES                \n")
        f.write("============================================================================\n")
        f.write(
            f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}        TIME: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
        f.write("Address: Digos City Philippines\n\n")
    print(f'Receipt saved as {filename}')
    print('Your receipt has been processed.')

def display_grocery_list(stock):
    print("\033[38;5;10m\nMERS NATIVE DELICACIES:\033[0m")
    print("\033[38;5;37m=================================================================\033[0m")
    print(f"{'Code':<10}{'Item':<30}{'Price':>10}{'Available':>15}")
    print("\033[38;5;37m=================================================================\033[0m")
    for code in inventory:
        if code in stock:
            print(f"{code:<10}{inventory[code]:<30}PHP {prices[code]:,.2f}{stock[code]['quantity']:>10}")
        else:
            print(f"{code:<10}{inventory[code]:<30}PHP {prices[code]:,.2f}{'Out of Stock':>10}")
    print("-" * 65)
    print("SPECIAL DEALS:")
    for deal in special_deals:
        print(deal)
    print()


def buy_item(stock):
    while True:
        code_input = input("Enter the item code you want to buy (1-18): ")
        if code_input.isdigit():
            code = int(code_input)
            if code in inventory:
                while True:
                    quantity_input = input(f"Enter the quantity of {inventory[code]} you want to buy: ")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Please enter a positive quantity.")
                        elif quantity > stock[code]['quantity']:
                            print(f"Sorry, only {stock[code]['quantity']} {inventory[code]}(s) available.")
                        else:
                            item_total = prices[code] * quantity
                            print(f"Total amount due for this item: PHP {item_total:,.2f}")

                            order.append((inventory[code], quantity, item_total, 0))
                            stock[code]['quantity'] -= quantity
                            write_stock_to_file(stock_filename, stock)  # Update the stock file
                            print(f"You have bought {quantity} {inventory[code]}(s).")
                            return
                    else:
                        print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid item code. Please enter a code from 1 to 18.")
        else:
            print("Invalid input. Please enter a valid number.")


def deduct_item():
    if order:
        print("\nYour Order:")
        print("-" * 45)
        print(f"{'Item':<25}{'Qty':>10}{'Total':>10}")
        print("-" * 45)
        for i, (item, quantity, item_total, _) in enumerate(order):
            if quantity > 0:
                print(f"{i + 1}. {item:<25}{quantity:>10}{item_total:>10,.2f}")
        print("-" * 45)
        while True:
            try:
                item_number = int(input("Enter the item number you want to deduct (0 to cancel): "))
                if item_number == 0:
                    break
                elif 1 <= item_number <= len(order):
                    item, quantity, item_total, _ = order[item_number - 1]
                    while True:
                        try:
                            deduct_qty = int(
                                input(f"Enter the quantity of {item} you want to deduct (max {quantity}): "))
                            if deduct_qty <= 0:
                                print("Invalid quantity. Please enter a positive number.")
                            elif deduct_qty == 0:
                                print("Invalid quantity. Please enter a positive number.")
                            elif deduct_qty > quantity:
                                print(f"You only have {quantity} {item}(s) in your order.")
                            else:
                                order[item_number - 1] = (
                                    item, quantity - deduct_qty, item_total - (item_total / quantity) * deduct_qty, _)
                                key = [key for key, value in inventory.items() if value == item][0]
                                stock[key]['quantity'] += deduct_qty
                                print(f"You have deducted {deduct_qty} {item}(s) from your order.")
                                break
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break
                else:
                    print("Invalid item number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print("You have no items in your order.")


def add_item():
    while True:
        display_grocery_list(stock)
        code_input = input("Enter the item code you want to add (1-18): ")
        if code_input.isdigit():
            code = int(code_input)
            if code in inventory:
                while True:
                    quantity_input = input(f"Enter the quantity of {inventory[code]} you want to add: ")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Please enter a positive quantity.")
                        else:
                            key = [key for key, value in inventory.items() if value == inventory[code]][0]
                            if quantity > stock[key]['quantity']:
                                print(f"Sorry, only {stock[key]['quantity']} {inventory[code]}(s) available.")
                            else:
                                item_total = prices[code] * quantity
                                print(f"Total amount due for this item: PHP {item_total:,.2f}")
                                order.append((inventory[code], quantity, item_total, 0))
                                stock[key]['quantity'] -= quantity
                                write_stock_to_file(stock_filename, stock)  # Update the stock file
                                print(f"You have added {quantity} {inventory[code]}(s) to your order.")
                                return
                    else:
                        print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid item code. Please enter a code from 1 to 18.")
        else:
            print("Invalid input. Please enter a valid number.")


def display_order():
    if order:
        total_cost = sum(item_total for _, quantity, item_total, _ in order if quantity > 0)
        print("\nYour Order:")
        print("-" * 45)
        print(f"{'Item':<25}{'Qty':>10}{'Total':>10}")
        print("-" * 45)
        for item, quantity, item_total, _ in order:
            if quantity > 0:
                print(f"{item:<25}{quantity:>10}{item_total:>10,.2f}")
        print("-" * 45)
        print(f"{'Total Amount':<25}{' ':>10}PHP {total_cost:>7,.2f}")
        print()

        while True:
            try:
                cash_paid = float(input("Enter cash amount: PHP "))
                if cash_paid < total_cost:
                    print("Insufficient amount.")
                else:
                    change = cash_paid - total_cost
                    print(f"Change: PHP {change:,.2f}")
                    customer_name = input("Enter your name for the receipt: ")
                    print_receipt(order, customer_name, cash_paid)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
    else:
        print("You have no items in your order.")

def shopping():
    while True:
        display_grocery_list(stock)
        buy_item(stock)
        while True:
            print("\n1. Add item to order")
            print("2. Deduct item from order")
            print("3. Proceed to checkout")
            choice = input("Enter your choice (Type 1, 2, 3): ")
            if choice == '1':
                add_item()
            elif choice == '2':
                deduct_item()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        display_order()
        print("")
        print("\033[38;5;37m===================================================================================\033[0m")
        print("")
        print("                   Thank you for visiting \033[38;5;10mMERS FOODS AND DELICACIES! \033[0m ")
        print("                       We hope to serve you well next time!")
        print("")
        print("\033[38;5;37m===================================================================================\033[0m")
        exit()


if __name__ == "__main__":
    shopping()