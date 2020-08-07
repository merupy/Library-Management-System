#This module displays the entire information of the library
def item_display():
    print("\t\t\tWelcome To Library")
    print("\t\t\t------------------\n")
    print(" S.N     Book Name                Author               Stock    Price($)")
    
def display_items(notepad_text):
    for i in notepad_text:
        print(" ",i[0]," "*(3-len(i[0])),
              " ",i[1]," "*(21-len(i[1])),
              " ",i[2]," "*(17-len(i[2])),
              " ",i[3]," "*(5-len(str(i[3]))),
              " ",i[4]," "*(5-len(i[4])))
        


