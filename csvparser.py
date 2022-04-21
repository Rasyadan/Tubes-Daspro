import lensplit
length = lensplit.length
split = lensplit.splittext
arrayLen = lensplit.arrayLength
game = ((open("game.csv", "r").readlines()))
#Import parsenya aja buat parse csv

def removen(array): # Menghapus "\n dari data yang diperoleh dari csv"
    for j in range(arrayLen(array)): 
        array[j] = (split(array[j], "\n"))
    result = ["" for i in range(arrayLen(array))]
    
    for i in range(arrayLen(array)):
        result[i] = (array[i])[0]
    return(result)       


def toArray(array,jumlah_kategori): 
    # Mengubah bentuk file csv menjadi array sehingga bisa diubah dalam memori/variabel
    # jumlah_kategori adalah jumlah kategori dalam sebuah file csv
    raw_csv_array = removen(array)
    result_array = ["" for i in range(jumlah_kategori*(arrayLen(raw_csv_array)))]
    temp_array = ["" for i in range(jumlah_kategori)]

    for i in range(0, arrayLen(raw_csv_array)):
        temp_array = split(raw_csv_array[i], ";") # Memisahkan tiap data dengan separator ";" dan memasukkan ke dalam temporary array
        for j in range(1,jumlah_kategori+1):
            result_array[(j-1) + (jumlah_kategori*(i))] = temp_array[j-1] # Memindahkan hasil dari temporary array ke array result
    
    return(result_array)

def tocsv(array, jumlah_kategori): 
    #Mengubah bentuk array data menjadi bentuk csv
    csv_array = ["" for i in range(arrayLen(array)//jumlah_kategori)]
    temp_string = ""
    for i in range(arrayLen(array)//jumlah_kategori):
        temp_string = ""
        for j in range(jumlah_kategori):
            if (j != 5) :
                temp_string += (array[j + (jumlah_kategori*i)] + ";") # Menambahkan separator ";"
            else :
                temp_string += array[j + (jumlah_kategori*i)] + "\n" # Menambahkan endline \n untuk akhir data csv
        csv_array[i] = temp_string
    return(csv_array)
