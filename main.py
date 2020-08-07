import read  # importing module
import display  # importing module
import datetime  # importing module
import returnNote  # importing module
import write  # importing module

# This main module runs the program
# In this module all the functions of different modules are called out

textfile = "library.txt"  # putting text file into variable
readf = read.convert_2d(read.read_text_file(textfile))


def main_menu():  # this function runs the program
    print("\nLibrary Option")
    print("--------------")
    a = input("1.Display Library\n2.Borrow Book\n3.Return Book\n4.Exit\n")

    if a == "1":
        display.item_display()
        display.display_items(readf)
        main_menu()

    elif a == "2":
        display.item_display()
        display.display_items(readf)
        your_name = input("\nEnter your full name: ")  # asking user's name
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        counter = 1

        SN = int(input("Enter the S.N to borrow book:"))  # user input
        if SN < 6:
            while counter == 1:
                anotherbook = input(
                    "Do you want to borrow another book?(y/n)")  # user input
                if anotherbook == "y":
                    next_book = int(
                        input("Enter the S.N to borrow book:"))  # user input
                    if next_book < 6:
                        if next_book == SN:
                            print("You cannot borrow same books multiple times!")
                        else:
                            returnNote.book2(
                                your_name, SN, next_book, day, month, year)
                            overwrite2 = write.decrease_stock2(
                                readf, (SN-1), (next_book-1))
                            write.user_database(overwrite2)
                            write.database2(your_name, readf[SN-1][1], readf[next_book-1][1], SN,
                                            next_book, readf[SN-1][4], readf[next_book-1][4], day, month, year)
                            counter = 0
                            main_menu()
                    else:
                        print("Please enter a valid SN")
                        main_menu()

                elif anotherbook == "n":
                    returnNote.book1(your_name, SN, day, month, year)
                    overwrite = write.decrease_stock(readf, (SN-1))
                    write.user_database(overwrite)
                    write.database1(
                        your_name, readf[SN-1][1], SN, readf[SN-1][4], day, month, year)
                    counter = 0
                    main_menu()
                else:
                    print("Please type y/n")
                    print(SN)
        else:
            print("Please enter a valid SN")
            main_menu()

    elif a == "3":
        try:
            user_receipt = input("Enter your name:")  # user input
            b = read.user_database(user_receipt)
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            year = datetime.datetime.now().year
            book1 = str(b[0])
            book2 = str(b[0])
            if book1 == "1":
                day1 = int(b[8])
                month1 = int(b[9])
                year1 = int(b[10])
                if day1 > day:
                    display.item_display()
                    display.display_items(readf)
                    print("\n")
                    # user input
                    SN = int(input("Enter the S.N to return book:"))
                    if SN < 6:
                        overwrite = write.increase_stock(readf, (SN-1))
                        write.user_database(overwrite)
                        returnNote.return1_receipt(
                            user_receipt, SN, day, month, year)
                        main_menu()
                    else:
                        print("Enter a valid S.N")
                        main_menu()

                elif day1 < day:
                    display.item_display()
                    display.display_items(readf)
                    print("\n")
                    # user input
                    SN = int(input("Enter the S.N to return book:"))
                    if SN < 6:
                        print("\n")
                        print("\t(TOO LATE,PLEASE PAY $1 AS FINE)")
                        overwrite = write.increase_stock(readf, (SN-1))
                        write.user_database(overwrite)
                        returnNote.return1_receipt(
                            user_receipt, SN, day, month, year)
                        print('\tFine:$1')
                        main_menu()
                    else:
                        print("Enter a valid S.N")

            elif book2 == "2":
                day2 = int(b[12])
                month2 = int(b[13])
                year2 = int(b[14])
                if day2 > day:
                    display.item_display()
                    display.display_items(readf)
                    print("\n")
                    # user input
                    SN = int(input("Enter the S.N of first borrowed book:"))
                    next_book = int(
                        input("Enter the S.N of second borrowed book:"))
                    overwrite = write.increase_stock2(
                        readf, (SN-1), (next_book-1))
                    write.user_database(overwrite)
                    returnNote.return2_receipt(
                        user_receipt, SN, next_book, day, month, year)
                    main_menu()

                elif day2 < day:
                    display.item_display()
                    display.display_items(readf)
                    print("\n")
                    # user input
                    SN = int(input("Enter the S.N to first borrowed book:"))
                    next_book = int(
                        input("Enter the S.N of second borrowed book:"))
                    print("\n")
                    print("\t(TOO LATE,PLEASE PAY $1 AS FINE)")
                    overwrite = write.increase_stock2(
                        readf, (SN-1), (next_book-1))
                    write.user_database(overwrite)
                    returnNote.return2_receipt(
                        user_receipt, SN, next_book, day, month, year)
                    print('\tFine:$1')
                    main_menu()

        except:
            print("There is no such borrower")
            main_menu()

    elif a == "4":
        print("Thank You! Visit us again")

    else:
        print("Please enter a valid option")
        main_menu()


main_menu()  # calling the function
