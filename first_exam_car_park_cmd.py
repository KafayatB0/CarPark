#first_exam_car_park_cmd.py

from first_exam_car_park_functions import FirstExamCarPark

# Getting to know the customer
customer = input("Hello, Please what is your name?")
print(f"Welcome to First Exam Car Park {customer}, which of our services will you like to access today?")

def main():
    this_car_park = FirstExamCarPark()

    while True:
        print("\nMenu:")
        print("a. Enter the Car Park")
        print("b. Exit the Car Park")
        print("c. View available parking spaces")
        print("d. Query parking record by ticket number")
        print("e. Quit")

        choice = input("Select an option: ").lower()

        if choice == 'a':
            print("Enter your UK car number in the standard format (e.g., AB12 CDE). Avoid special characters and note your input is not case-sensitive")
            reg_number = input("Please enter your car registration number: ")
            result = this_car_park.Enter_the_Car_Park(reg_number)
            print(result)

        elif choice == 'b':
            print("Enter your UK car registration number in the standard format (e.g., AB12 CDE). Avoid special characters and note your input is not case-sensitive")
            reg_number = input("Please enter your car registration number: ")
            result = this_car_park.Exit_the_Car_Park(reg_number)
            print(result)

        elif choice == 'c':
            available_spaces = this_car_park.AvailableParkingSpace()
            print()
            print('Number of Available Parking Spaces:', len(available_spaces) )

        elif choice == 'd':
            value = input("Please enter ticket number: ")
            result = this_car_park.Query_Parking_Record_by_TicketNumber(value)
            print(result)

        elif choice == 'e':
            this_car_park.UpdateParkDetails()
            input(f"Thank you!, we hope to see you again soon {customer}.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
