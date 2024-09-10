
def welcome_message():
    print("Welcome to the Car Management System")
    print("-----------------------------------")
    print("CARS DETAILS")
    print("*************")


def register_car(owner_name, car_details):
    """Register a car by adding details to the set."""
    print("Register your car")
    print("-----------------")
    print("Fill the details..")
    date = input("Date (dd-mm-yyyy): ")
    car_num = input("Enter your car number: ")
    model_num = input("Model Number: ")

    car_data = (owner_name, date, car_num, model_num)
    if car_data in car_details:
        print("Car is already registered.")
    else:
        car_details.add(car_data)
        print("Car registered successfully.")


def check_details(car_details):
    """Check car registration details."""
    print("Check your details")
    print("------------------")
    car_num = input("Enter your car number: ")

    car_found = False
    for car in car_details:
        if car[2] == car_num:
            print("Details.")
            print("--------")
            print(f"Owner: {car[0]}")
            print(f"Registered date: {car[1]}")
            print(f"Car number: {car[2]}")
            print(f"Model Number: {car[3]}")
            car_found = True
            break

    if not car_found:
        print("Invalid car number!")


def register_service(service_type, service_details):
    """Register a service for a car."""
    print(f"{service_type}")
    print("--------")
    date = input("Date (dd-mm-yyyy): ")
    car_num = input("Enter your car number: ")
    model_num = input("Model Number: ")

    service_data = (service_type, date, car_num, model_num)
    if service_data in service_details:
        print(f"{service_type} already registered.")
    else:
        service_details.add(service_data)
        print(f"{service_type} registered successfully.")


def show_services():
    """Display the available services."""
    print("Available Services")
    print("------------------")
    print("1. Car Wash")
    print("2. Car Paint")
    print("3. Servicing")
    print("4. Tire Replacement")
    print("5. Oil Change")
    print("6. Exit")


def handle_services(service_details):
    """Manage car services based on user selection."""
    while True:
        show_services()
        choice = input("Enter your choice: ")

        service_options = {
            "1": "Car Wash",
            "2": "Car Paint",
            "3": "Servicing",
            "4": "Tire Replacement",
            "5": "Oil Change"
        }

        if choice in service_options:
            register_service(service_options[choice], service_details)
        elif choice == "6":
            print("Exiting service menu...")
            break
        else:
            print("Invalid choice!")

        cont = input("Continue with services? (yes/no): ").lower()
        if cont != 'yes':
            break


def main():
    welcome_message()
    owner_name = input("Enter your name: ")
    print(f"Hello, {owner_name}!")

    # Data storage
    car_details = set()  # Stores tuples of car information
    service_details = set()  # Stores tuples of service information

    while True:
        print("\nMain Menu")
        print("Choose one option:")
        print("1. Register your car")
        print("2. Check the car details")
        print("3. Services")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_car(owner_name, car_details)
        elif choice == "2":
            check_details(car_details)
        elif choice == "3":
            handle_services(service_details)
        elif choice == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice!")

        cont = input("Do you want to return to the main menu? (yes/no): ").lower()
        if cont != 'yes':
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
