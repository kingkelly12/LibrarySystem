class Person:
    def __init__(self, name, age, gender, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = id

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

person_one = Person('Moses', 19, 'Male', 12345)
person_two = Person('Kelly', 25, 'Male', 12346)
person_three = Person('John', 25, 'Male', 12347)

person_one.greet()

print(person_one.name, person_one.age, person_one.gender, person_one.id)
print(person_two.name, person_two.age, person_two.gender, person_two.id)
print(person_three.name, person_three.age, person_three.gender, person_three.id)

class Student(Person):
    def __init__(self, name, age, course, student_id):
        super().__init__(name, age, "Student", student_id)
        self.student_id = student_id
        self.course = course

    def greet(self):
        print(f'Hello, my name is {self.name}. I am a student pursuing {self.course}. My student ID is {self.student_id}, and my age is {self.age}.')

student_one = Student('Moses', 19, 'Software Engineering', 12345)
student_one.greet()

class Books:
    def __init__(self, title, author, year, isbn, genre, status="Available"):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.status = status
        self.borrowed_by = None

    def display_info(self):
        print(f'BookTitle: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Genre: {self.genre}, Status: {self.status}')

    def update_status(self, new_status):
        valid_statuses = ['Borrowed', 'Misplaced', 'Returned', 'Read', 'Available']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Status of '{self.title}' updated to: {self.status}")
        else:
            print(f"Invalid status. Choose from: {', '.join(valid_statuses)}")

book_one = Books('Clean Code', 'Robert C. Martin', 2008, '9780132350884', 'Software Engineering')
book_two = Books('The Pragmatic Programmer', 'Andrew Hunt and David Thomas', 1999, '9780201616224', 'Software Engineering')

book_one.display_info()
book_one.update_status("Borrowed")
book_one.display_info()

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age, "Librarian", employee_id)
        self.employee_id = employee_id
        self.books = []

    def greet(self):
        print(f'Hello, my name is {self.name} and I am a librarian with employee ID {self.employee_id}.')

    def record_new_book(self, book):
        self.books.append(book)
        print(f"Recorded new book: {book.title}")

    def lend_book(self, title, borrower_name):
        for book in self.books:
            if book.title == title and book.status == "Available":
                book.status = "Borrowed"
                book.borrowed_by = borrower_name
                print(f"{title} has been lent to {borrower_name}.")
                return
        print(f"{title} is not available for lending.")

    def receive_returned_book(self, title):
        for book in self.books:
            if book.title == title and book.status == "Borrowed":
                print(f"{title} returned by {book.borrowed_by}.")
                book.status = "Available"
                book.borrowed_by = None
                return
        print(f"No borrowed record found for {title}.")

    def track_borrowed_books(self):
        print("Currently borrowed books:")
        borrowed = False
        for book in self.books:
            if book.status == "Borrowed":
                print(f"{book.title} (borrowed by {book.borrowed_by})")
                borrowed = True
        if not borrowed:
            print("No books are currently borrowed.")

librarian_one = Librarian('Mary', 50, 12398)
librarian_one.greet()

book1 = Books("Code Complete", "Steve McConnell", 1993, "9780735619678", "Software Engineering")
book2 = Books("Design Patterns", "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", 1994, "9780201633610", "Software Engineering")

librarian_one.record_new_book(book1)
librarian_one.record_new_book(book2)
librarian_one.lend_book("Code Complete", "Mary")
librarian_one.track_borrowed_books()
librarian_one.receive_returned_book("Code Complete")
librarian_one.track_borrowed_books()