from lensplit import arrayLength

def buy_game(game, user, kepemilikan, data_pengguna) :
    ID = str(input('Masukkan ID game :'))
    #Searching lokasi dari ID game   
    for i in range(arrayLength(game)):
        if game[i] == ID:
            i_ID = i
            price_ID = int(game[i_ID+4])
            stok = int(game[i_ID+5])
               
    
    #Mencari saldo user 
    for j in range(arrayLength(user)):
        if user[j] == data_pengguna[1]:
            saldo = int(user[j+4])
    
    #Menentukan kepemilikan game dari user
    found = True
    for k in range(arrayLength(kepemilikan)-1):
        if kepemilikan[k] == ID and kepemilikan[k+1] == data_pengguna[0]:
            found = False
            
            
            
    if (found == True) and (saldo >= price_ID) and (stok != 0):
        print('Game','berhasil dibeli!')
        x = [0] * (arrayLength(kepemilikan)+2)
        for i in range(0,arrayLength(x)):
            if i <= arrayLength(kepemilikan) - 1:
                x[i] = kepemilikan[i]
            elif i == arrayLength(kepemilikan)  :
                x[i] = ID
            elif i == arrayLength(kepemilikan) + 1:
                x[i] = data_pengguna[0]
        data_pengguna = x
        user[j+4] = str(saldo - price_ID)
        return data_pengguna, user       
    elif found == False:
        print('Anda sudah memiliki game tersebut')
    elif saldo < price_ID: 
        print('Saldo anda tidak cukup untuk membeli Game tersebut!')
    elif stok == 0:
        print('Stok Game tersebut sedang habis!')

