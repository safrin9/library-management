import save_all_books
def remove_book(all_books):
    search_book=input("Enter book title to remove: ")
    for book in all_books:
        if book['title']==search_book:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("book removed successfully")
            return all_books
    print("book not found")