FILE_NAME = "borrowed_books.txt"


def save_borrow_record(book_title: str, borrower_name: str, borrowing_date: str) -> None:
    """Stores a borrowed book record in a text file."""
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{book_title} | {borrower_name} | {borrowing_date}\n")


def retrieve_borrow_records() -> None:
    """Reads and displays all stored borrowing records from the text file."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            records = file.readlines()

        if not records:
            print("\nNo borrowing records found.")
            return

        print("\n--- Borrowed Books Records ---")
        for index, record in enumerate(records, start=1):
            print(f"{index}. {record.strip()}")
    except FileNotFoundError:
        print("\nNo records file exists yet. Please add a record first.")


def main() -> None:
    while True:
        print("\n1. Record a borrowed book")
        print("2. Retrieve borrowed book records")
        print("3. Exit")
        option = input("Choose an option (1-3): ").strip()

        if option == "1":
            title = input("Enter book title: ").strip()
            borrower = input("Enter borrower name: ").strip()
            date = input("Enter borrowing date (e.g., 2026-11-20): ").strip()
            save_borrow_record(title, borrower, date)
            print("Record saved successfully.")
        elif option == "2":
            retrieve_borrow_records()
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
