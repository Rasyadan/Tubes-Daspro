# Gunakan di file lain dengan meletakkan kode berikut (tanpa # dan contoh penggunaan):
# import lensplit
# txtlength = lensplit.length (Hanya bisa digunakan untuk mencari length dari string saja)
# (Contoh penggunaan : txtlength("Test1") hasilnya 5)
# split = lensplit.splittext 
# (Contoh penggunaan : split("Test1;Test2", ";") dengan hasil ["Test1", "Test2"])
# arrayLength = lensplit.arrayLength
# Contoh penggunaan : arrayLength([0,1,2,3,4]) menghasilkan 5


def splittext(text, separator):
    # text : string, berupa teks yang akan di split
    # separator : string, berupa jenis separator yang akan digunakan untuk melakukan split pada string
    text_length = length(text)
    text_array = [text[i] for i in range(text_length)]
    temp_result = ["" for i in range (text_length)]
    array_pos = 0
    total_index = 0
    for i in range(text_length):
        if (text_array[i] != separator):
            temp_result[array_pos] += text[i]
        else :
            array_pos += 1

    for k in range(text_length):
        if (temp_result[k] != ""):
            total_index += 1
    result = [temp_result[i] for i in range(total_index)]
    
    return(result)

def length(text): 
    # text berupa string yang akan dihitung panjangnya
    stop = False
    txtlength = 0
    i = 0
    while (stop != True):
        try :
            char = text[i]
            i += 1
            txtlength += 1
        except :
            stop = True
    return (txtlength)

def arrayLength(array):
    # array nerupa array yang akan dihitung panjangnya
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
