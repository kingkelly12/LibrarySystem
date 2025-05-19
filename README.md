# Library Management System

This project is a simple **Library Management System** implemented in Python. It provides classes and methods to manage books, librarians, and students in a library setting.

## Features

- **Person Class**: A base class for common attributes like name, age, gender, and ID.
- **Book Class**: Represents a book with attributes like title, author, genre, publication year, and ISBN. Includes methods for book-related actions such as borrowing, returning, and reading.
- **Librarian Class**: Inherits from `Person` and includes methods for assisting users, lending books, organizing books, and tracking library inventory.
- **Student Class**: Inherits from `Person` and includes methods for enrolling in courses, borrowing books, and returning books.

## Classes and Methods

### `Person`
- `__init__(name, age, gender, ID)`
- `greet()`
- `get_info()`

### `Book`
- `__init__(title, author, genre, publication_year, ISBN)`
- `get_info()`
- `get_details()`
- `borrowed()`
- `return_book()`
- `misplace()`
- `read()`

### `Librarian` (inherits from `Person`)
- `__init__(name, employee_id)`
- `assist(person)`
- `lend_books(book)`
- `receive_returned_book(book)`
- `organize(book)`
- `record_new_book(book)`
- `track_books()`

### `Student` (inherits from `Person`)
- `__init__(name, student_id, course)`
- `enroll(course)`
- `get_student_info()`
- `borrow_book(book)`
- `return_book(book)`

## Usage

1. **Create a Book**:
   ```python
   book = Book("1984", "George Orwell", "Dystopian", 1949, "1234567890")
   print(book.get_info())
   ```

2. **Create a Librarian**:
   ```python
   librarian = Librarian("Alice", "L001")
   print(librarian.assist(Person("Bob", 25, "Male", "P001")))
   ```

3. **Create a Student**:
   ```python
   student = Student("Charlie", "S001", "Computer Science")
   print(student.borrow_book(book))
   ```

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the Python script:
   ```bash
   python library.py
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Kelly Koome
