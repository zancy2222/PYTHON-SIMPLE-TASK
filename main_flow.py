from plumbing_services import get_services, generate_receipt, get_districts, validate_email, validate_phone, validate_name, \
    save_receipt_to_file


def print_receipt(receipt):
    print("\nReceipt:")
    print(receipt)


def main():
    print(
        "\033[38;5;15m-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("")
    print("                                    Welcome to \033[38;5;35m DR. PLUMBER! ")
    print("")
    print("                                        \033[38;5;22mGROUP 9 - A141")
    print("                                       \033[38;5;2mFiel, Anwell Earl")
    print("                                      \033[38;5;2mUnabia, Allaena Jae")
    print("")
    print(
        "\033[38;5;15m-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("")
    print("                                         \033[38;5;159mDESCRIPTION")
    print("             \033[38;5;120mWe offer installation, repair, and maintenance services. The plumbing")
    print("          \033[38;5;120mindustry is crucial for maintaining and improving community infrastructure.")
    print("        \033[38;5;120mQualified experts are needed to install, repair, and maintain water systems in ")
    print("          \033[38;5;120mall types of structures. With the complexity of modern plumbing systems and a")
    print("                \033[38;5;120mfocus on sustainability, practical solutions are essential.\n")
    print("")
    print("                 \033[38;5;2m* * * The Dr. Plumbers are only operated in Davao City * * *")
    print(
        "\033[38;5;15m---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___")
    print(
        "\033[38;5;15m___---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___")

    # Get user details
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ")

    address = input("Enter your address: ")
    phone = input("Enter your phone number (11 digits starting with 09): ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter a valid phone number.")
        phone = input("Enter your phone number (11 digits starting with 09): ")

    email = input("Enter your email address (must end with @gmail.com): ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
        email = input("Enter your email address (must end with @gmail.com): ")

    # Get and display districts
    districts = get_districts()
    print("Available Districts:")
    for district_id, district in districts.items():
        print(f"{district_id}. {district}")

    district_id = input("Select your district by entering the corresponding number: ")
    while district_id not in districts:
        print("Invalid district selection. Please enter a valid number.")
        district_id = input("Select your district by entering the corresponding number: ")

    selected_district = districts[district_id]
    print(f"You have selected: {selected_district}")

    # Get and display available services
    services = get_services()
    print("Available Services:")
    for idx, (service_name, price) in enumerate(services, start=1):
        print(f"{idx}. {service_name} - ₱{price}")

    # Service selection and processing
    selected_services = []
    while True:
        service_idx = input(
            "Enter the service number you want to add. \nEnter \"done\" when you are finished selecting the services that you want: ")
        if service_idx.lower() == 'done':
            break
        elif service_idx.isdigit() and 0 < int(service_idx) <= len(services):
            selected_services.append(services[int(service_idx) - 1])
            print(f"Added {services[int(service_idx) - 1][0]} to your selection.")
        else:
            print("Invalid service number. Please enter a valid number.")

    if not selected_services:
        print("No services selected. Exiting...")
        return

    while True:
        more_services = input("Do you want to add more services? (yes/no): ").strip().lower()
        if more_services == 'yes':
            print("Available Services:")
            for idx, (service_name, price) in enumerate(services, start=1):
                print(f"{idx}. {service_name} - ₱{price}")
            service_idx = input(
                "Enter the service number you want to add. \nEnter \"done\" when you are finished selecting the services that you want: ")
            if service_idx.isdigit() and 0 < int(service_idx) <= len(services):
                selected_services.append(services[int(service_idx) - 1])
                print(f"Added {services[int(service_idx) - 1][0]} to your selection.")
            else:
                print("Invalid service number. Please enter a valid number.")
        elif more_services == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Generate and display receipt
    total_amount = sum(price for _, price in selected_services)
    receipt = generate_receipt(name, address, phone, email, selected_district, selected_services, total_amount)

    # Display receipt
    print_receipt(receipt)

    # Save receipt to file
    filename = f"{name}_receipt.txt"
    save_receipt_to_file(receipt, filename)
    print(f"\nReceipt saved as '{filename}'.")


if __name__ == "__main__":
    main()
