import read #impoting module
import datetime #importing module
day=datetime.datetime.now().day 
month=datetime.datetime.now().month
year=datetime.datetime.now().year
def book1(your_name,SN,day,month,year): #this function displays the receipt of user who takes only 1 book
    r=read.convert_2d(read.read_text_file("library.txt"))
    print('\n\t\t\tRECEIPT')
    print('\t\t\t-------')
    print('\tName: ',your_name,)
    print('\tBorrowed Book:',r[SN-1][1])
    print('\tPrice:$',r[SN-1][4])
    print('\tBook issued on:',day,"-",month,"-",year)                     
    print('\tBook to be returned on:',return_day(day),"-",return_month(month),"-",return_year(year))
    print('\tBook SN: ',SN,"(This is needed while returning book)")

def book2(your_name,SN,next_book,day,month,year): #this function displays the receipt of user who takes 2 books
    r=read.convert_2d(read.read_text_file("library.txt"))
    print('\n\t\tRECEIPT')
    print('\t\t-------')
    print('\tName: ',your_name)
    print('\tBorrowed Book:',r[SN-1][1])
    print('\tPrice:$',r[SN-1][4])
    print('\tBorrowed Book:',r[next_book-1][1])
    print('\tPrice:$',r[next_book-1][4])
    print('\tTotal Price:$',float(r[SN-1][4])+float(r[next_book-1][4]))   
    print('\tBook issued on:',day,"-",month,"-",year)
    print('\tBook to be returned on:',return_day(day),"-",return_month(month),"-",return_year(year))
    print('\tFirst Book SN:',SN,"(This is needed while returning book)")
    print('\tSecond Book SN:',next_book,"(This is needed while returning book)")


def return_day(day): #this function adds 10 days date from the book borrowed date which is used while displaying book return date
    returnday=day+10
    return returnday

def return_month(month): #if the user borrowes the book at the end of the month, this function changes the month while displaying book return date
    returnmonth=month
    returnd=return_day(day)
    if returnd>30:
        returnmonth+=1
        returnd=1
    return returnmonth
def return_year(year): #if the user borrowes the book at the end of the year, this function changes the year while displaying book return date
    returny=year
    returnmonth=return_month(month)
    if returnmonth>12:
        returny+=1
        returnmonth=1
    return returny
    
def return1_receipt(user_receipt,SN,day,month,year):
    r=read.convert_2d(read.read_text_file("library.txt"))
    print('\n\t\tRECEIPT')
    print('\t\t-------')
    print('\tName: ',user_receipt)
    print('\tBorrowed Book:',r[SN-1][1])
    print('\tPrice:$',r[SN-1][4])
    print('\tBook returned on:',day,"-",month,"-",year)
    
def return2_receipt(user_receipt,SN,next_book,day,month,year):
    r=read.convert_2d(read.read_text_file("library.txt"))
    print('\n\t\tRECEIPT')
    print('\t\t-------')
    print('\tName: ',user_receipt)
    print('\tBorrowed Book:',r[SN-1][1])
    print('\tPrice:$',r[SN-1][4])
    print('\tBorrowed Book:',r[next_book-1][1])
    print('\tPrice:$',r[next_book-1][4])
    print('\tTotal Price:$',float(r[SN-1][4])+float(r[next_book-1][4]))
    print('\tBook returned on:',day,"-",month,"-",year)

