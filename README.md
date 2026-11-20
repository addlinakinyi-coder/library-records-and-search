# library-records-and-search

Library borrowed books record system and linear search algorithm.

---

## Question 1: Library Borrowed Books System

### a) Pseudocode

BEGIN BorrowedBooksRecord
    DECLARE bookTitle, borrowerName, borrowingDate AS STRING
    DECLARE choice AS CHARACTER
    DECLARE fileHandle AS FILE

    OPEN "borrowed_books.txt" FOR APPEND AS fileHandle

    REPEAT
        DISPLAY "Enter Book Title: "
        INPUT bookTitle

        DISPLAY "Enter Borrower Name: "
        INPUT borrowerName

        DISPLAY "Enter Borrowing Date (YYYY-MM-DD): "
        INPUT borrowingDate

        WRITE bookTitle, " | ", borrowerName, " | ", borrowingDate TO fileHandle

        DISPLAY "Record saved successfully."
        DISPLAY "Do you want to enter another record? (Y/N): "
        INPUT choice
    UNTIL choice = "N" OR choice = "n"

    CLOSE fileHandle

    DISPLAY "Do you want to view saved records? (Y/N): "
    INPUT choice

    IF choice = "Y" OR choice = "y" THEN
        OPEN "borrowed_books.txt" FOR READ AS fileHandle
        WHILE NOT EOF(fileHandle) DO
            READ line FROM fileHandle
            DISPLAY line
        ENDWHILE
        CLOSE fileHandle
    ENDIF
END BorrowedBooksRecord

### b) Flowchart

Start -> Open borrowed_books.txt in Append Mode -> Input bookTitle, borrowerName, borrowingDate -> Save Record to Text File -> Input choice: Add another record? (Y/N)
- If Yes: loop back to Input bookTitle, borrowerName, borrowingDate
- If No: Close File -> Input choice: View records? (Y/N)
  - If Yes: Open File in Read Mode & Display Records -> End
  - If No: End

### c) Python Implementation
See borrowed_books.py in this repository.

---

## Question 2: Student Registration Number Search

### a) Linear Search Pseudocode

BEGIN LinearSearchRegistration
    DECLARE regNumbers AS ARRAY OF STRING
    DECLARE targetReg AS STRING
    DECLARE foundIndex AS INTEGER
    DECLARE i AS INTEGER

    regNumbers <- ["REG/001/2026", "REG/002/2026", "REG/003/2026", "REG/004/2026"]
    foundIndex <- -1

    DISPLAY "Enter registration number to search: "
    INPUT targetReg

    FOR i <- 0 TO LENGTH(regNumbers) - 1 DO
        IF regNumbers[i] = targetReg THEN
            foundIndex <- i
            BREAK
        ENDIF
    ENDFOR

    IF foundIndex != -1 THEN
        DISPLAY "Record found at index ", foundIndex
    ELSE
        DISPLAY "Registration number not found."
    ENDIF
END LinearSearchRegistration

### Python Implementation
See linear_search.py in this repository.

