from lensplit import arrayLength

def login(user):
    # fungsi login menerima input username, password lalu mereturn data pengguna jika sudah login

    # KAMUS: 
        # nama,username,password: String
        # logged_in,found : Boolean
        # i : integer
        # data_pengguna: Array
        # function arrayLength {mengembalikan panjang suatu array}
    # ALGORITMA:
    username = (input("Masukkan username: "))
    password = (input("Masukkan password: "))
    logged_in=True # State awal adalah true, jika pengguna tidak berhasil login maka state diganti false
    found=False # state awal apakah username ditemukan atau tidak
    for i in range (7,arrayLength(user),6): # mengakses username mulai dari user id pertama
        if user[i]==username:
            if user[i+2]==password:
                    id=user[i-1]
                    username=user[i]
                    nama=user[i+1]
                    password=user[i+2]
                    role=user[i+3]
                    saldo=user[i+4]
                    data_pengguna= [id,username,nama,password,role,saldo]
                    print("=="*24)
                    print()
                    print("Halo",data_pengguna[2]+"!","Selamat datang di Binomo")
                    logged_in=True
                    found=True
                    return data_pengguna # jika berhasil login maka data_pengguna direturn
            else:
                    print("Password Anda salah.")
                    print("=="*24)
                    print()
                    found=True
 
    if not found:
        print("Username tidak ditemukan")
        print("=="*24)
        print()
    return logged_in==False # jika logged_in==False, pengguna tidak dapat mengakses fitur lain selain log in
