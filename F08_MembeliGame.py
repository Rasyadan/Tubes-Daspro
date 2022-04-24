from lensplit import arrayLength

def buy_game(game, user, kepemilikan, data_pengguna) :
    ID = str(input('Masukkan ID game :'))
    #Searching lokasi dari ID game   
    for i in range(arrayLength(game)):
        if game[i] == ID:
            i_ID = i
            price_ID = game[i_ID+4]
            stok = game[i_ID+5]
               
    
    #Mencari saldo user 
    for j in range(arrayLength(user)):
        if user[j] == data_pengguna[1]:
            saldo = user[j+4]
    
    #Menentukan kepemilikan game dari user
    found = True
    for k in range(arrayLength(kepemilikan)-1):
        if kepemilikan[k] == ID and kepemilikan[k+1] == data_pengguna[0]:
            found = False
            
            
            
    if (found == True) and (saldo >= price_ID) and (stok != 0):
        print('Game','berhasil dibeli!')
    elif found == False:
        print('Anda sudah memiliki game tersebut')
    elif saldo < price_ID: 
        print('Saldo anda tidak cukup untuk membeli Game tersebut!')
    elif stok == 0:
        print('Stok Game tersebut sedang habis!')

