from save_all_books import save_all_books
import random
from datetime import datetime
def add_books(all_books):
    title=input("enter book title: ")
    author=input("enter author name: ")
    isbn=random.randint(10000,99999)
    bookAddedAt=datetime.now().strftime("%d-%m-%y %H:%M:%S")
    while True:
        try:
            quantity=int(input("Enter quantity: "))
           
            break
        except ValueError:
            print("invalid input. please enter integer.")
    
    while True:
        try:
            year=int(input("enter publishing year: "))
           
            break
        except ValueError:
            print("invalid input. please enter integer.")
    while True:
        try:
            price=int(input("Enter price: "))
            break
        except ValueError:
            print("invalid input. please enter integer.")
    book={
        "title":title,
        "author":author,
        "ISBN":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
        "bookAddedAt":bookAddedAt,
        "bookLastUpdated":""
        }
    
    all_books.append(book)
    save_all_books(all_books)
    print("Books added successfully\n")
    return all_books
