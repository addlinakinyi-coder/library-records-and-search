def linear_search_reg(reg_numbers: list[str], target_reg: str) -> int:
    """Searches for target_reg in reg_numbers using linear search.
    Returns the index if found, or -1 if not found.
    """
    for index, reg in enumerate(reg_numbers):
        if reg.strip().lower() == target_reg.strip().lower():
            return index
    return -1


def main() -> None:
    student_reg_numbers = [
        "REG/101/2025",
        "REG/102/2025",
        "REG/103/2025",
        "REG/104/2025",
        "REG/105/2025",
    ]

    search_reg = input("Enter student registration number to search: ")
    position = linear_search_reg(student_reg_numbers, search_reg)

    if position != -1:
        print(f"Registration number '{search_reg}' found at index {position}.")
    else:
        print(f"Registration number '{search_reg}' was not found in the records.")


if __name__ == "__main__":
    main()
