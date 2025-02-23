import decisions 
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit") 

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            while True: 
                num = input("Enter a number (1-9): ").strip()
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= 9: 
                        print("Function of {num} is {get_factorial(num)}")
                        break
                print("Invalid input! Please enter a number between 1 and 9.")

        elif choice == "2": 
            while True: 
                num = input("Enter a number (1-99): ").strip()
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= 99:
                        print("Sum of odd numbers up to {num} if {sum_odd_numbers(num)}")
                        break
                print("Invalid input! Please enter a number between 1 and 99.")

        elif choice == "3":
            while True:
                exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
                if exit_choice in ["yes", "y"]:
                    print("Exiting program. Goodbye!")
                    return
        elif exit_choice in ["no", "n"]:
            break
        print("Invalid input! Please enter 'yes' or 'no'.")
    else: 
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e: 
        print("An unexpected error occured: {e}") 