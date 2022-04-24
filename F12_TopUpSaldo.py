from lensplit import arrayLength 

def topup(game, user): #menghasilkan return berupa saldo akhir
    username = str(input('Masukan username: '))
    saldo = int(input('Masukan saldo: '))
    found = True   
    for i in range(arrayLength(game)):
        if user[i] == username:
            found = True
            i_username = i
            saldoawal = int(user[i_username + 4])
            break
        else: #user[i] != username
            found = False
    
    if found == True :
        if saldoawal + saldo < 0 :
            print('Masukan tidak valid.')
        else: #found == False
            print('Top up berhasil. Saldo', username , 'bertambah menjadi', str(saldoawal + saldo))
            user[i_username + 4] = str(saldoawal+saldo)
            return user
    else:
        print('Username', str(username), 'tidak ditemukan.')
