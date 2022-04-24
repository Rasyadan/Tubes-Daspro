from lensplit import arrayLength 

def riwayatPembelian(data_riwayat): #fungsi yang akan menampilkan riwayat
    if arrayLength(data_riwayat) == 0: #jika tidak punya riwayat pembelian
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah','\033[1m' + 'beli_game' + '\033[0m', 'untuk membeli.')
    else: #jika memiliki riwayat pembelian
        if arrayLength(data_riwayat) == 5: #jika daftar game tidak ada
            print("User tidak memilik game.")
        else:
            for i in range(6,arrayLength(data_riwayat),5):
                print((str(int((i-1)/5)))+ '.',data_riwayat[i-1], end = " | ")
                print("{:10.12}|".format(data_riwayat[i-1]), end=" ")
                print("{:30.32}|".format(data_riwayat[i]), end=" ")
                print("{:13.15}|".format(data_riwayat[i+1]), end=" ")
                print("{:7.6}|".format(data_riwayat[i+2]), end=" ")
                print(data_riwayat[i+3],'   |')
