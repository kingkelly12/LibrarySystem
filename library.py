class Person :
    def __init__(self, name, age, gender, ID):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID = ID

    def greet(self):
        return f"Hello, my name is {self.name} and I am a {self.gender}, I'm {self.age} years old."
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Book :
    def __init__(self, title, author, genre, publication_year, ISBN):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.ISBN = ISBN

    def get_info(self):
        return f"'{self.title}' by {self.author}"
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Year: {self.publication_year}, ISBN: {self.ISBN}"
    def borrowed(self):
        return f"'{self.title}' is currently borrowed."
    def return_book(self):
        return f"'{self.title}' has been returned." 
    def misplace(self):
        return f"'{self.title}' is misplaced."
    def read(self):
        return f"Reading '{self.title}' by {self.author}."
    
    
class Librarian(Person): 
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.age = None
        self.gender = None

    def assist(self, person):
        return f"{self.name} is assisting {person.name}."
    def lend_books(self, book):
        return f"{self.name} is lending '{book.title}'."
    def receive_returned_book(self, book):
        return f"{self.name} has returned '{book.title}'."
    def organize(self, book):
        return f"{self.name} is organizing '{book.title}'."
    def record_new_book(self, book):
        return f"{self.name} has recorded a new book: '{book.title}'."
    def track_books(self):
        return f"{self.name} is tracking the books in the library."
    
    
class Student(Person):
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.age = None
        self.gender = None
        
    def enroll(self, course):
        self.course = course
        return f"{self.name} has enrolled in {self.course}."
    def get_student_info(self):
        return f"Student Name: {self.name}, ID: {self.student_id}"
    def borrow_book(self, book):
        return f"{self.name} has borrowed '{book.title}'."
    def return_book(self, book):
        return f"{self.name} has returned '{book.title}'."