import json
import save_all_books
def return_book(all_books):
    name=input("borrower name: ")
    title=input("book to return: ")
    with open("borrow.json","r") as fp:
        data=json.load(fp)
    record_found=False
   
    for borrower in data[:]:

        if borrower['name'] == name and borrower['book'] == title:
            record_found = True
          
            for book in all_books:
                if book["title"] == borrower["book"]:
                
                    book["quantity"] += 1  
                    break
           
            data.remove(borrower)
            save_all_books.save_all_books(all_books)
            with open("borrow.json","w") as fp:
                json.dump(data,fp,indent=4)
            print("book returned successfully\n")
            return
        
   
    
    if not record_found:
        print(f"No record found for '{title}' borrowed by {name}.")
        return
   
  
    
   
    


    