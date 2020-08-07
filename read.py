def read_text_file(textfile): #this function reads the library database
    file=open(textfile,"r")
    content=file.readlines()
    return content

def convert_2d(un_prep): #this function converts the library database into 2d list
    list2=[]
    for i in un_prep:
        list2.append(i.replace("\n","").split(","))
    return list2

def user_database(user_receipt): #this function reads the user database
    file=open("{}.txt".format(user_receipt),"r")
    file1=file.read().split(",")
    file.close()
    return file1
           

