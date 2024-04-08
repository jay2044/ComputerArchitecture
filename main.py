from converters.mips_to_machine import *
from converters.machine_to_mips import *


def main():
    while True:
        print("\nOPTIONS:")
        print("1. MIPS to Machine Code")
        print("2. Machine to MIPS")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            mips_instruction = input("Enter MIPS instruction: ")
            print(mips_to_machine(mips_instruction))
        elif choice == '2':
            machine_code = input("Enter Machine Code: ")
            print(machine_to_mips(machine_code))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
