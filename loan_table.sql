CREATE TABLE loans (
    id INTEGER PRIMARY KEY, 
    member_id INTEGER,
    book_isbn INTEGER,
    loan_date DATE,
    return_date DATE,
    status TEXT
);  