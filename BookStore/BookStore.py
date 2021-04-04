import sqlite3
class Book:
    def __init__(self,_bookName,_UnitPrice,_BookID=None):
        self.BookName=_bookName
        self.UnitPrice=_UnitPrice
        self.BookID=_BookID
    def __str__(self):
        return "Name : {}, price={}".format(self.BookName,self.UnitPrice)
class BookType:
    def __init__(self,_SpeciesName,_description,_BookSpeciesID=None):
        self.Description=_description
        self.SpeciesName=_SpeciesName
        self.BookSpecies=_BookSpeciesID
    def __str__(self):
        return self.SpeciesName
class Author:
    def __init__(self,_AuthorName,_AuthorAge,_AuthorID=None):
        self.AuthorName=_AuthorName
        self.AuthorAge=_AuthorAge
        self.AuthorID=_AuthorID
    def __str__(self):
        return self.AuthorName
class Publisher:
    def __init__(self,_PublisherName,_PublisherID=None):
        self.PublisherName=_PublisherName
        self.PublisherID=_PublisherID
    def __str__(self):
        return  "the name of publisher={}".format(self.PublisherName)

class AppUser:
    def __init__(self,_userName,_Password,Role="Member",_AppuserID=None):
        self.Username=_userName
        self.Password=_Password
        self.AppUserID=_AppuserID
    def __str__(self):
        return "User with username: {} and password: {} ".format(self.Username,self.Password)
class OrderDetail:
    def __init__(self,_BookID,_AppUserID):
        self.BookID=_BookID
        self.AppUserID=_AppUserID
class Library:
    def KutuphaneLib(self):
        self.__Connection=sqlite3.connect("KitapEvi.DB")
        self.__Cursor=self.__Connection.cursor()
        Publishers="create table if not exists Publishers(PublisherID integer primary key autoincrement,PublisherName text)"
        Authors = "create table if not exists Authors(AuthorID integer primary key autoincrement,AuthorName text,AuthorAge number,PublisherID int,foreign key(PublisherID) references Publishers(PublisherID))"
        BookSpecies = "create table if not exists BookSpecies(BookSpeciesID integer primary key autoincrement,SpeciesName text,Description text)"
        Books="create table if not exists Books(BookID integer primary key autoincrement,BookName text,UnitPrice number,AuthorID int,BookSpeciesID int,foreign key(AuthorID) references Authors(AuthorID),foreign key(BookSpeciesID) references BookSpecies(BookSpeciesID))"
        AppUsers="create table if not exists AppUsers(AppUserID integer primary key autoincrement,UserName text,Password number,Role text)"
        OrderDetails = "create table if not exists OrderDetails(BookID integer, AppUserID integer,foreign key(BookID) references Books(BookID),foreign key(AppUserID) references AppUsers(AppUserID))"
        commands=[Books,Authors,BookSpecies,AppUsers,OrderDetails,Publishers]
        for x in commands:
            self.__Cursor.execute(x)
        self.__Connection.commit()
    def EndConnection(self):
        self.__Connection.close()
    def __init__(self):
        self.KutuphaneLib()
    def AddBooks(self,b:Book):
        addBooks="insert into Books(BookName,UnitPrice) values (?,?)"
        self.__Cursor.execute(addBooks,(b.BookName,b.UnitPrice))
        self.__Connection.commit()
        print("eklendi...")
    def FindBookID(self,_bookName):
        FindBookID="select BookID,BookName,UnitPrice from Books where BookName=?"
        self.__Cursor.execute(FindBookID,(_bookName,))
        findList=self.__Cursor.fetchall()
        p=Book(findList[0][1],findList[0][2],findList[0][0])
        return p
    def UpdateBook(self,_oldName,_newName,_NewPrice):
        tobeupdated=self.FindBookID(_oldName)
        updateBook="update Books set BookName=? ,UnitPrice=? where BookID=?"
        self.__Cursor.execute(updateBook,(_newName,_NewPrice,tobeupdated))
        self.__Connection.commit()
        print("updated..")
    def DeleteBook(self,_BookName):
        deleteBook="delete from Books(BookID,BookName,UnitPrice) where BookName=?"
        self.__Cursor.execute(deleteBook,(_BookName,))
        self.__Connection.commit()
        print("deleted...")
    def ShowBooks(self):
        showBooks="select BookName,UnitPrice from Books"
        self.__Cursor.execute(showBooks)
        show=self.__Cursor.fetchall()
        if len(show)==0:
            print("cant find")
        else:
            for x in show:
                listele=Book(x[0],x[1])
                print(listele)
    def AddOrderDetails(self,_BookID,_AppUserID):
        addOrderDetails = "insert into OrderDetails(BookID,AppUserID) values (?,?)"
        self.__Cursor.execute(addOrderDetails,(_BookID,_AppUserID))
        self.__Connection.commit()
        print("succesfully completed..")
    def AddAuthor(self,author:Author):
        addAuthor="insert into Authors(AuthorName) values (?)"
        self.__Cursor.execute(addAuthor,(author.AuthorName,))
        self.__Connection.commit()
        print("added")
    def FindAuthorID(self,_AuthorName):
        findAuthorID="select AuthorID,AuthorName,AuthorAge from Authors where AuthorName=?"
        self.__Cursor.execute(findAuthorID,(_AuthorName,))
        findAuthorlist=self.__Cursor.fetchall()
        if len(findAuthorlist)==0:
            print("can not find")
        else:
            listele=findAuthorlist[0][0]
            print(listele)
    def UpdateAuthor(self,_oldName,_newName,_age):
        tobeupdated=self.FindAuthorID(_oldName)
        updateAuthor="update Authors set AuthorName=? ,AuthorAge=? where AuthorID=?"
        self.__Cursor.execute(updateAuthor,(_newName,_age,tobeupdated))
        self.__Connection.commit()
        print("updated")
    def ShowAuthor(self):
        ShowUpdate="select AuthorID,AuthorName,AuthorAge from Authors"
        self.__Cursor.execute(ShowUpdate)
        show=self.__Cursor.fetchall()
        if len(show)==0:
            print("cant find.")
        else:
            for x in show:
                listele=Author(x[1],x[2])
                print(listele)
    def deleteAuthor(self,_AuthorName):
        deleteAuthor="delete from Authors where AuthorName=?"
        self.__Cursor.execute(deleteAuthor,(_AuthorName,))
        self.__Connection.commit()
        print("deleted...")
    def AddPublisher(self,add:Publisher):
        AddPublisher="insert into Publishers(PublisherName) values (?)"
        self.__Cursor.execute(AddPublisher,(add.PublisherName,))
        self.__Connection.commit()
        print("added...")
    def AddtoCart(self,_bookName):
       __AddBook="select BookName,UnitPrice,BookID from Books where BookName=?"
       self.__Cursor.execute(__AddBook,(_bookName,))
       theGetProduct=self.__Cursor.fetchall()
       p=Book(theGetProduct[0][0],theGetProduct[0][1],theGetProduct[0][2])
       return p
    def FindPublisherID(self,_publisherName):
        FindID="select PublisherID from Publishers where PublisherName=? "
        self.__Cursor.execute(FindID,(_publisherName,))
        find=self.__Cursor.fetchall()
        if len(find)==0:
            print("can not find")
        else:
            list=find[0][0]
            print(list)
    def UpdatePublisher(self,_oldName,_newName):
        tobeupdated=self.FindPublisherID(_oldName)
        updatedPublisher="update Publishers set PublisherName=? where PublisherID=?"
        self.__Cursor.execute(updatedPublisher,(_newName,tobeupdated))
        self.__Connection.commit()
        print("updated")
    def ShowPublisher(self):
        showPublisher="select PublisherName,PublisherID from Publishers"
        self.__Cursor.execute(showPublisher)
        show=self.__Cursor.fetchall()
        if len(show)==0:
           print("can not find")
        else:
            for x in show:
                listele=Publisher(x[0],x[1])
                print(listele)
    def DeletePublisher(self,_publisherName):
        deletePublisher="delete from Publishers where PublisherName=?"
        self.__Cursor.execute(deletePublisher,(_publisherName,))
        self.__Connection.commit()
        print("deleted")
    def AddBookSpecies(self,add:BookType):
        addBookSpecies="insert into BookSpecies(SpeciesName,Description) values (?,?)"
        self.__Cursor.execute(addBookSpecies,(add.SpeciesName,add.Description))
        self.__Connection.commit()
        print("added....")
    def findBookSpeciesID(self,_SpeciesName):
        findID="select BookSpeciesID,SpeciesName from BookSpecies where SpeciesName=?"
        self.__Cursor.execute(findID,(_SpeciesName,))
        find=self.__Cursor.fetchall()
        if len(find)==0:
            print("can not find")
        else:
             list=find[1]
             print(list)
    def UpdateSpecies(self,_oldspecies,_newSpecies):
        tobeupdated=self.findBookSpeciesID(_oldspecies)
        update="update BookSpecies set SpeciesName=? where BookSpeciesID=?"
        self.__Cursor.execute(update,(_newSpecies,tobeupdated))
        self.__Connection.commit()
        print("updated")
    def ShowSpecies(self):
        showSpecies="select SpeciesName,Description from BookSpecies"
        self.__Cursor.execute(showSpecies)
        show=self.__Cursor.fetchall()
        if len(show)==0:
            print("cant find")
        else:
            listele=show[0],show[1]
            print(listele)
    def DeleteSpecies(self,_speciesName):
        deleteSpecies="delete from BookSpecies where SpeciesName=?"
        self.__Cursor.execute(deleteSpecies,(_speciesName,))
        self.__Connection.commit()
        print("deleted...")
    def ShowUser(self):
        showUser="select UserName,Password from AppUsers "
        self.__Cursor.execute(showUser)
        show=self.__Cursor.fetchall()
        if len(show)==0:
            print("the appuser cant find")
        else:
            listele=show[0],show[1]
            print(listele)
    def FindUserID(self,_userName):
        findID="select Role from AppUsers where UserName=?"
        self.__Cursor.execute(findID,(_userName,))
        find=self.__Cursor.fetchall()
        if len(find)==0:
            print("cant find")
        else:
            rol=find[0][0]
            if rol=="Admin":
                return "Admin"
            else:
                return "Member"
    def AddUser(self,add:AppUser):
        addUser="insert into AppUsers(UserName,Password) values (?,?)"
        self.__Cursor.execute(addUser,(add.Username,add.Password))
        self.__Connection.commit()
        print("added...")
    def GettheLastAppUserID(self):
        gettheLast="select AppUserID from AppUsers order by AppUserID DESC limit 1"
        self.__Cursor.execute(gettheLast)
        getirilenEleman = self.__Cursor.fetchall()
        return getirilenEleman[0][0]

k=Library()

