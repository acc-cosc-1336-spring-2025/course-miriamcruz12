from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

def main():
    while True: 
        print("\nMenu:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dna1 = input("Enter first DNA sequence: ")
            dna2 = input("Enter second DNA sequence: ")
            try:
                result = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {result}")
            except ValueError as e:
                print(e) 

        elif choice == "2":
            dna = input("Enter DNA sequence: ")
            print(f"Complement: {get_dna_complement(dna)}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()