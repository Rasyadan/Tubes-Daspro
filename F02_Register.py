from lensplit import arrayLength
from lensplit import length

def isAdmin (data_pengguna):
    # Mengecek apakah role pengguna merupakan admin atau user, jika pengguna 
    # adalah admin maka akan mengembalikan True, dan sebaliknya
    # Kamus: 
        # data_pengguna[4] : string
    # Algoritma
    if data_pengguna[4]=="admin":
        return(True)
    else:
        return(False)

def isUsernameValid(username):
# fungsi untuk validasi tiap character pada username 
# KAMUS:
    # isValid : boolean
    # function length {menghitung panjang string}
# ALGORITMA
    isValid=True
    for i in range (length(username)):
        if 97<= ord(username[i]) <= 122 or 65<=ord(username[i])<=90 or 0<=ord(username[i])<=9 or username[i]=="_" or username[i]=="-" or 48<=ord(username[i])<=57:
            isValid
        else:
            isValid=False
    return(isValid)

def register(user,data_pengguna):
# fungsi register menerima input username, nama, dan password 
# lalu menambahkannya sebagai data pengguna baru pada memori data user
# KAMUS:
    # nama,username,password:string
    # data_pengguna : array
    # ALGORITMA
    if isAdmin(data_pengguna): # validasi role
        nama= input("Masukkan nama: ") 
        username = input("Masukkan username: ")
        # validasi username
        if isUsernameValid(username):
            print(end="")
        else:
            print("Maaf, username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")
        while isUsernameValid(username)==False: # input username sampai benar
            username=input("Masukkan username: ")
            if isUsernameValid(username):
                isUsernameValid(username)==True
        
        password= input("Masukkan password: ")
    
        found=True # mencari apakah username sudah terpakai atau belum
        while found==True: # input username sampai username tersedia (tidak ada di file csv)
            found=False
            for i in range (7,arrayLength(user),6): # mengakses username mulai dari user id pertama
                        if user[i]==username:
                            found=True
                        else:
                            i+=1
            if found==True : # jika username sudah terpakai
                print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
                username=input("Masukkan username: ")
                password=input("Masukkan password: ")
            else: # jika username tersedia
                tambahan = [round(arrayLength(user)/6),username,nama,password,"user",0] # data_pengguna baru
                print(f"Username berhasil ditambahkan.")
                print("=="*24)
                print()
                user = user + tambahan
        return (user)
    else: # jika bukan diakses admin
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
        print("=="*24)
        print()
