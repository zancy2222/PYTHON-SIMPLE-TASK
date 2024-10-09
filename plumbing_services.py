import re


def get_services():
    services = [
        ('Plumbing Inspection', 900),
        ('Pipe Leak Repair', 400),
        ('Toilet Leak Repair', 850),
        ('Faucet Leak Repair', 350),
        ('Bathtub Leak Repair', 350),
        ('Shower Leak Repair', 350),
        ('Sink Leak Repair', 350),
        ('Bathroom Drain Cleaning', 1200),
        ('Kitchen Drain Cleaning', 1000),
        ('Water Heater Installation', 2500),
        ('Water Filtration System Installation', 5000),
        ('Water Meter Installation', 2500),
        ('Pressure Regulator Installation', 2500),
        ('Drainage System Installation', 5000),
        ('Sump Pump Installation', 2500),
        ('Sink Installation', 1500),
        ('Toilet Installation', 1800),
        ('Sink Clog Removal', 550),
        ('Shower Clog Removal', 650),
        ('Toilet Clog Removal', 850),
        ('Sewer Line Cleaning', 850),
        ('Septic Tank Pumping', 8500),
        ('Grease Trap Cleaning', 3500),
        ('Hydro Jetting', 5000),
        ('Water Pressure Adjustment', 1500)
    ]
    return services


def get_districts():
    districts = {
        '1': 'Davao City Proper',
        '2': 'Agdao',
        '3': 'Buhangin',
        '4': 'Calinan',
        '5': 'Paquibato',
        '6': 'Tugbok',
        '7': 'Toril',
        '8': 'Talomo',
        '9': 'Bago Aplaya',
        '10': 'Bago Gallera',
        '11': 'Sasa'
    }
    return districts


def generate_receipt(name, address, phone, email, district, selected_services, total_amount):
    receipt = f"""

========================================================================
Name: {name}
Address: {address}
Phone: {phone}
Email: {email}
District: {district}
========================================================================
Services Selected:
========================================================================
    """
    for service_name, service_price in selected_services:
        receipt += f"{service_name} - ₱{service_price}\n"
    receipt += f"\nTotal Amount: ₱{total_amount}\n========================================================================"
    return receipt


def validate_email(email):
    return re.match(r'^[\w\.-]+@gmail\.com$', email) is not None


def validate_phone(phone):
    return re.match(r'^09\d{9}$', phone) is not None


def validate_name(name):
    return len(name) > 0


def save_receipt_to_file(receipt, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(receipt)
        print(f"Receipt saved as '{filename}'")
    except IOError as e:
        print(f"Error occurred while saving receipt: {e}")
