from datetime import datetime
import save_all_books
def update_all_books(all_books):
    search_book=input("Enter book title you want to update: ")
    for book in all_books:
      if book["title"]==search_book:
            title=input("enter book title: ")
            author=input("enter author name: ")
         
            year=int(input("enter publishing year: "))
            price=int(input("Enter price: "))
            quantity=int(input("Enter quantity: "))
            book_last_up_at=datetime.now().strftime("%d-%m-%y %H:%M:%S")

            book["title"]=title
            book['author']=author
            book['year']=year
            book['price']=price
            book["quantity"]=quantity
            book["bookLastUpdated"]=book_last_up_at
            
            save_all_books.save_all_books(all_books)
            print("book updated successfully..")
            return all_books
    print("book not found")