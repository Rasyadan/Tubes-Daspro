def splittext(text, separator):
    # Memisahkan string dengan pemisah tertentu
    # text : string, berupa teks yang akan di split
    # separator : string, berupa jenis separator yang akan digunakan untuk melakukan split pada string
    text_length = length(text) 
    text_array = ["" for char in range(text_length)]
    index = 0
    for char in text : # Iterasi tiap character dalam text dan dimasukkan ke array
        text_array[index] = char
        index += 1 
    temp_result = ["" for i in range (text_length)]
    array_pos = 0
    total_index = 0
    for i in range(text_length): # Konkatenasi semua char ke dalam satu index, jika char adalah separator maka pindah index array berikutnya
        if (text_array[i] != separator):
            temp_result[array_pos] += text_array[i] 
        else :
            array_pos += 1

    for k in range(text_length): # Menghapus elemen kosong dalam array hasil
        if (temp_result[k] != ""):
            total_index += 1
    result = [temp_result[i] for i in range(total_index)]
    
    return(result)

def length(text): 
    # Menghitung panjang sebuah string
    # text berupa string yang akan dihitung panjangnya
    txtlength = 0
    i = 0
    for e in text :
        txtlength += 1
    return (txtlength)

def arrayLength(array): 
    # Menghitung banyak isi sebuah array
    stop = False
    j = 0
    len = 0
    while (stop == False):
        try :
            temp = array[j]
            j += 1
            len += 1
        except :
            stop = True
    return len

