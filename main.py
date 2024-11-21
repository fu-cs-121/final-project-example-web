# cli_interface.py
from core import Journal

def display_menu():
    print("\n=== Journal Menu ===")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search by Title")
    print("4. Search by Date")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    journal = Journal()
    journal.load_from_file('journal.json')  # Load entries from file at startup

    while True:
        choice = display_menu()

        if choice == "1":
            title = input("\nEnter entry title: ")
            content = input("Enter entry content: ")
            journal.add_entry(title, content)
            journal.save_to_file('journal.json')  # Save entries after adding a new one
            print("Entry added successfully!")

        elif choice == "2":
            entries = journal.get_all_entries()
            if not entries:
                print("\nNo entries found.")
            else:
                print("\n=== All Entries ===")
                for entry in entries:
                    print(f"\n{entry}")
                    print("-" * 40)

        elif choice == "3":
            title = input("\nEnter title to search: ")
            entry = journal.get_entry_by_title(title)
            if entry:
                print(f"\n{entry}")
            else:
                print("\nEntry not found.")

        elif choice == "4":
            date = input("\nEnter date (YYYY-MM-DD): ")
            entries = journal.get_entries_by_date(date)
            if entries:
                print(f"\nEntries for {date}:")
                for entry in entries:
                    print(f"\n{entry}")
                    print("-" * 40)
            else:
                print("\nNo entries found for this date.")

        elif choice == "5":
            journal.save_to_file('journal.json')  # Save entries before exiting
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()