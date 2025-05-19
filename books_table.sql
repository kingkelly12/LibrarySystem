CREATE TABLE books (
    isbn INTEGER PRIMARY KEY, 
    title TEXT,
    genre TEXT,
    publication_date DATE,  
    pages INTEGER,
    total_copies INTEGER,
    copies_available INTEGER
);