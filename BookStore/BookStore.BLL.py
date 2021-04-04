from BookStore import Library
from BookStore import Book,Author,BookType,AppUser,Publisher
a=Library()
while True:
    Selection = input("""
       1.Kullanici girisi
       2. uye ol
       """)
    username = input("please enter your username")
    password = input("please enter your password")
    if Selection=="1":
        sonuc=a.FindUserID(username)
        if sonuc==None:
            continue
        if username=="admin":
           adminSelection= input("""Select the action you want to do.
            1.Book          
            2.Book Type
            3.Author
            4.Appuser
            5.Publisher 
            6.Quit""")
           if adminSelection=="1":
                sec=input("""1.Book insert
                2.Book delete
                3.Book update
                4.See the books""")
                if sec=="1":
                    kitapAdi=input("enter the name of the book you want to add")
                    fiyat=input("enter a price")
                    b=Book(kitapAdi,fiyat)
                    a.AddBooks(b)
                elif sec=="2":
                    ad=input("enter the name of the book you want to delete")
                    a.DeleteBook(ad)
                elif sec=="3":
                    oldB=input("enter the old name of the book you want to update")
                    newB=input("enter a new name of the book for update")
                    newP=input("enter a new price")
                    a.UpdateBook(oldB,newB,newP)
                elif sec=="4":
                    a.ShowBooks()
           elif adminSelection=="2":
                choise=input("""please select you want to do
                1.add a booktype
                2.delete a booktype
                3.show booktypes""")
                if choise=="1":
                    Name=input("enter the name of booktype")
                    Description=input("enter a description")
                    c=BookType(Name,Description)
                    a.AddBookSpecies(c)
                elif choise=="2":
                    enter=input("enter a booktype you want to delete")
                    a.DeleteSpecies(enter)
                elif choise=="3":
                    a.ShowSpecies()
           elif adminSelection=="3":
                select=input("""please select you want to do
                1. insert an author
                2. delete an author
                3. update an author
                4.show the authors""")
                if select=="1":
                    add=input("enter the name of the author you want to add")
                    age=input("enter the age of the author")
                    b=Author(add,age,None)
                    a.AddAuthor(b)
                elif select=="2":
                    delete=input("enter the name of the author you want to delete")
                    a.deleteAuthor(delete)
                elif select=="3":
                    oldA=input("enter the old name of the Author you want to update")
                    newA=input("enter a new name of the Author for update")
                    Age=input("enter the age of the author")
                    a.UpdateAuthor(oldA,newA,Age)
                elif select=="4":
                    a.ShowAuthor()
           elif adminSelection=="4":
                option=input("""please select you want to do
                1.add a new user
                2. show the users""")
                if option=="1":
                    username=input("username:")
                    password=input("password:")
                    app=AppUser(username,password)
                    a.AddUser(app)
                elif option=="2":
                    a.ShowUser()
           elif adminSelection=="5":
                sec=input("""select you want to do
                1.add a publisher
                2.update a publisher
                3.delete a publisher
                4.show the publishers""")
                if sec=="1":
                    publisher=input("enter the name of the publisher you want to add")
                    b=Publisher(publisher)
                    a.AddPublisher(b)
                elif sec=="2":
                    oldP=input("enter the name of the publisher you want to update")
                    newP=input("enter a new name of the publisher for update")
                    a.UpdatePublisher(oldP,newP)
                elif sec=="3":
                    sec=input("enter the name of the publisher you want to delete")
                    a.DeletePublisher(sec)
                elif sec=="4":
                    a.ShowPublisher()
           elif adminSelection=="6":
               print("Quit..")
               break
        else:
            order=input("if you would like to order a book, select 1")
            if order=="1":
                SelectedBooks=[]
                while True:
                    a.ShowBooks()
                    select=input("Select the book you want to add to your cart")
                    SelectedObject=a.AddtoCart(select)
                    SelectedBooks.append(SelectedObject)
                    a.FindBookID(select)

                    theLastUserID=a.GettheLastAppUserID()
                    tekrarSec=input("Would you like to choose a book again?")
                    if tekrarSec=="yes":
                        continue
                    else:
                        for x in SelectedBooks:
                         a.AddOrderDetails(x.BookID,theLastUserID)

                    break



    elif Selection=="2":
        app=AppUser(username,password)
        a.AddUser(app)


