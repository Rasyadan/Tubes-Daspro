import save

def exit():
    inputValid=False
    state=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if state=="Y" or state=="y" or state=="N" or state=="n":
        inputValid
        if state=="Y" or state=="y":
            save()
            exit=True
        else:
            exit=False
    else:
        inputValid=False
        while not inputValid:    
            print("Ketik (y/n)")
            state=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
            if state=="Y" or state=="y" or state=="N" or state=="n":
                inputValid=True
                if state=="Y" or state=="y":
                    save()
                    exit=True
                else:
                    exit=False
            else:
                inputValid=False
    return(exit)

