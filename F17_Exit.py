from F16_Save import save

def exitBNMO(dir,game,riwayat,user,kepemilikan):
    # Fungsi akan memberi pilihan pada pengguna untuk menyimpan 
    # data (dengan fungsi save) atau tidak, lalu fungsi akan menghentikan loop program utama.
    # KAMUS
    # state1:integer
    # state2:character
    # inputValid,exit:boolean
    # function save {menyimpan data pada memori berupa array ke file csv}
    # ALGORITMA
    print("Apakah Anda ingin keluar dari game?")
    print("1. Ya")
    print("2. Tidak")
    state1=int(input("Ketikkan di sini: "))
    if state1==1 or state1==2:
        if state1==2:
            exit=False
        else:
            inputValid=False
            state2=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # validasi input
            if state2=="Y" or state2=="y" or state2=="N" or state2=="n":
                inputValid
                if state2=="Y" or state2=="y":
                    save(dir,game,riwayat, user,kepemilikan)
                    print("Perubahan data berhasil tersimpan.")
                    exit=True
                else:
                    exit=True
            else:
                inputValid=False
                while not inputValid:    
                    print("Ketik (y/n)")
                    state2=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)") # validasi input
                    if state2=="Y" or state2=="y" or state2=="N" or state2=="n":
                        inputValid=True
                        if state2=="Y" or state2=="y":
                            save(dir,game,riwayat,user,kepemilikan)
                            print("Perubahan data berhasil tersimpan.")
                            exit=True
                        else:
                            exit=True
                    else:
                        inputValid=False
    return(exit)

