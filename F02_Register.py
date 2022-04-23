from lensplit import arrayLength
from lensplit import length

def isAdmin (data_pengguna):
# untuk validasi role yang sesuai dengan fungsi
    if data_pengguna[4]=="admin":
        return(True)
    else:
        return(False)

def isUsernameValid(username):
# untuk validasi tiap character pada username 
    isValid=True
    for i in range (length(username)):
        if 97<= ord(username[i]) <= 122 or 65<=ord(username[i])<=90 or 0<=ord(username[i])<=9 or username[i]=="_" or username[i]=="-" or 48<=ord(username[i])<=57:
            isValid
        else:
            isValid=False
    return(isValid)

def register(user,data_pengguna):
    if isAdmin(data_pengguna):
        nama= input("Masukkan nama: ")
        username = input("Masukkan username: ")
        # validasi username
        if isUsernameValid(username):
            print("Username valid.")
        else:
            print("Maaf, username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.")
        while isUsernameValid(username)==False:
            username=input("Masukkan username: ")
            if isUsernameValid(username):
                print("Username valid.")
                isUsernameValid(username)==True
        
        password= input("Masukkan password: ")
    
        found=False
        for i in range (7,arrayLength(user),6): # mengakses username mulai dari user id pertama
                    if user[i]==username:
                        found=True
                    else:
                        i+=1
        if found==True :
            print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
        else:
            tambahan = [round(arrayLength(user)/6),username,nama,password,"user",0]
            print("Data pengguna baru berhasil ditambahkan.")
            user = user + tambahan
        return (user)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")

        
        password= input("Masukkan password: ")
    
        found=False
        for i in range (7,arrayLength(user),6): # mengakses username mulai dari user id pertama
                    if user[i]==username:
                        found=True
                    else:
                        i+=1
        if found==True :
            print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
        else:
            tambahan = [round(arrayLength(user)/6),username,nama,password,"user",0]
            print(f"Username berhasil ditambahkan.")
            user = user + tambahan
        return (user)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
