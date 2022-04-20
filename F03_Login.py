from lensplit import arrayLength

def login(user):
    username = (input("Masukkan username: "))
    password = (input("Masukkan password: "))
    logged_in=True
    found=False
    i=1
    while i<=(arrayLength(user)-1) and not found:
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
                        print("Halo",data_pengguna[2]+"!","Selamat datang di Binomo")
                        logged_in=True
                        print("=="*24)
                        found=True
                        return data_pengguna
                    else:
                        print("Password Anda salah.")
                        found=True
                else:
                    i+=1
    if not found:
        print("Username tidak ditemukan")
    return logged_in==False