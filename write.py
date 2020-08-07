import returnNote #importing module
import datetime #importing module

def user_database(dlist): #this function decreases the quantity of the books in the library database based on book borrowed by the user
    file=open("library.txt","w")
    for i in range(len(dlist)):
        count=0
        for j in range(len(dlist[i])):
            file.write(str(dlist[i][j]))
            if count<4:
                file.write(",")
            count+=1
        file.write("\n")
    file.close()


def decrease_stock(dlist,SN): #this function changes the quantity of books in the library when user borrows only 1 book
    dlist[SN][3]=int(dlist[SN][3])-1
    return dlist

def decrease_stock2(dlist,SN,SN2): #this function changes the quantity of books in the library when user borrows 2 books
    dlist[SN][3]=int(dlist[SN][3])-1
    dlist[SN2][3]=int(dlist[SN2][3])-1
    return dlist

def increase_stock(dlist,SN): #this function changes the quantity of books in the library when user returns only 1 book
    dlist[SN][3]=int(dlist[SN][3])+1
    return dlist

def increase_stock2(dlist,SN,SN2): #this function changes the quantity of books in the library when user returns 2 books
    dlist[SN][3]=int(dlist[SN][3])+1
    dlist[SN2][3]=int(dlist[SN2][3])+1
    return dlist

def database1(username,book,booknum,price,day,month,year): #this function creates a new database of the user who borrowed only 1 book
    file=open(str(username)+".txt","w")
    file.write(str("1"))
    file.write(",")
    file.write(str(username))
    file.write(",")
    file.write(str(book))
    file.write(",")
    file.write(str(booknum))
    file.write(",")
    file.write(str(price))
    file.write(",")
    file.write(str(datetime.datetime.now().day)+","+str(datetime.datetime.now().month)+","+str(datetime.datetime.now().year))
    file.write(",")
    file.write(str(returnNote.return_day(datetime.datetime.now().day))+","+str(returnNote.return_month(datetime.datetime.now().month))+","+str(returnNote.return_year(datetime.datetime.now().year)))
    file.close()

def database2(username,book,secbook,booknum,booknum2,price,price2,day,month,year): #this function creates a new database of the user who borrowed 2 books
    file=open(str(username)+".txt","w")
    file.write(str("2"))
    file.write(",")
    file.write(str(username))
    file.write(",")
    file.write(str(book))
    file.write(",")
    file.write(str(booknum))
    file.write(",")
    file.write(str(price))
    file.write(",")
    file.write(str(secbook))
    file.write(",")
    file.write(str(booknum2))
    file.write(",")
    file.write(str(price2))
    file.write(",")
    file.write((str(float(price)+float(price2))))
    file.write(",")
    file.write(str(datetime.datetime.now().day)+","+str(datetime.datetime.now().month)+","+str(datetime.datetime.now().year))
    file.write(",")
    file.write(str(returnNote.return_day(datetime.datetime.now().day))+","+str(returnNote.return_month(datetime.datetime.now().month))+","+str(returnNote.return_year(datetime.datetime.now().year)))
    file.close()


    
    
               

               
