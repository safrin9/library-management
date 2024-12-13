import datetime
import save_all_books
import json
borrowers=[]
def borrower(all_books):
   
        
    name=input("enter borrower name: ")
    phone=input("enter borrower phone: ")
    s_book=input("enter book title: ")
    
    lended_time=datetime.datetime.now()
    return_date = lended_time + datetime.timedelta(days=10)
    lended_time_str = lended_time.strftime("%d-%m-%y %H:%M:%S")
    return_date_str = return_date.strftime("%d-%m-%y %H:%M:%S")
   
    borrower={
        "name":name,
        "phone":phone,
        "book":s_book,
        "lended_time":lended_time_str,
        "return_due_date":return_date_str 
    }
    
    for book in all_books:
        if book["title"]==s_book:
            if book['quantity']<=0:
                print("not enough books to lend")
                return all_books
            book["quantity"]-=1
            borrowers.append(borrower)
            with open("borrow.json","w") as fp:
                json.dump(borrowers,fp,indent=4)
            save_all_books.save_all_books(all_books)
            print("book lended successfully\n")
            return all_books
    print("Book doesnt exist in the list")
