import save

def exit():
    state=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if state!="Y" or state!="y" or state!="N" or state!="n":
        inputValid=False
    else:
        if state=="Y" or state=="y":
                save()
                exit=True
                # Pada program utama terdapat while loop yang dijalankan jika boolean exit=False, 
                # jika exit=True maka program akan berhenti dijalankan 
        else:
                exit=False
        return(exit)
    while not inputValid:    
        print("Ketik (y/n)")
        state=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if state!="Y" or state!="y" or state!="N" or state!="n":
            inputValid=False
        else:
            if state=="Y" or state=="y":
                save()
                exit=True
            else:
                exit=False
            return(exit)

