# Fungsi untuk menghasilkan kunci yang akan digunakan dalam enkripsi dan dekripsi
def generate_key(key):
    key = key.replace(" ", "")  # Hapus spasi dari kunci
    key = key.upper()
    
    key_without_duplicates = []  # Inisialisasi list untuk menyimpan huruf unik
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Alfabet tanpa huruf 'J'

    # Tambahkan huruf-huruf dari kunci ke key_without_duplicates (tanpa 'J')
    for c in key:
        if c != 'J' and c not in key_without_duplicates:
            key_without_duplicates.append(c)
    
    # Tambahkan huruf-huruf tersisa dari alfabet (tanpa 'J')
    for letter in alphabet:
        if letter != 'J' and letter not in key_without_duplicates:
            key_without_duplicates.append(letter)
    
    # Konversi key_without_duplicates menjadi string
    key_string = ''.join(key_without_duplicates)
    
    return key_string

# Membuat matriks berukuran x * y yang diinisialisasi dengan nilai initial
# Matriks ini akan digunakan dalam proses enkripsi dan dekripsi.
def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

result = list()

while True:
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
    if choice == 1:
        key = input("Enter key: ")
        key_string = generate_key(key)
        print("Key used for encryption: ", key_string)

        def locindex(c): # Mendapatkan lokasi setiap karakter
            loc = list()
            if c == 'J':
                c = 'I'
            for i, j in enumerate(my_matrix):
                for k, l in enumerate(j):
                    if c == l:
                        loc.append(i)
                        loc.append(k)
                        return loc

        def encrypt(key_string):
            msg = str(input("ENTER MSG: "))
            msg = msg.upper()
            msg = msg.replace(" ", "")             
            i = 0
            
            # Jika ada pasangan huruf yang sama bersebelahan,
            # maka sebuah 'X' akan dimasukkan di antara mereka.
            for s in range(0, len(msg) + 1, 2):
                if s < len(msg) - 1:
                    if msg[s] == msg[s + 1]:
                        msg = msg[:s + 1] + 'X' + msg[s + 1:]
                        
            # Jika panjang pesan setelah penanganan pasangan huruf sama adalah ganjil,
            # maka 'X' tambahan akan ditambahkan pada akhir pesan.
            if len(msg) % 2 != 0:
                msg = msg[:] + 'X'
            
            print("CIPHER TEXT: ", end=' ')
            while i < len(msg):
                # Menggunakan fungsi locindex untuk mendapatkan lokasi (indeks baris dan kolom)
                # dari masing-masing huruf dalam matriks yang digunakan dalam Playfair Cipher.
                # Lokasi ini akan digunakan untuk menentukan huruf pengganti.
                loc = list()
                loc = locindex(msg[i])
                loc1 = list()
                loc1 = locindex(msg[i + 1])
                
                # Jika kedua huruf memiliki indeks kolom yang sama,
                # maka huruf pengganti diambil dari baris yang sama dan kolom berikutnya
                if loc[1] == loc1[1]: 
                    print("{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]), end=' ')
                
                # Jika kedua huruf memiliki indeks baris yang sama,
                # maka huruf pengganti diambil dari kolom yang sama dan baris berikutnya
                elif loc[0] == loc1[0]:
                    print("{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]), end=' ')  
                
                # Jika kedua huruf memiliki indeks baris dan kolom yang berbeda,
                # maka huruf pengganti diambil dari baris pertama pada indeks baris pertama dan kolom kedua pada indeks kolom kedua.
                else:
                    print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')    
                i = i + 2

        my_matrix = matrix(5, 5, 0)  #initialize matrix
        for i in range(0, 5):  #making matrix
            for j in range(0, 5):
                my_matrix[i][j] = key_string[i * 5 + j]

        encrypt(key_string)

    elif choice == 2:
        key = input("Enter key: ")
        key_string = generate_key(key)
        print("Key used for decryption:", key_string)

        def decrypt(key_string):
            msg = str(input("ENTER CIPHER TEXT: "))
            msg = msg.upper()
            msg = msg.replace(" ", "")
            print("PLAIN TEXT: ", end=' ')
            i = 0
            while i < len(msg):
                loc = list()
                loc = locindex(msg[i])
                loc1 = list()
                loc1 = locindex(msg[i + 1])
                if loc[1] == loc1[1]:
                    print("{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]), end=' ')
                elif loc[0] == loc1[0]:
                    print("{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]), end=' ')  
                else:
                    print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')    
                i = i + 2

        my_matrix = matrix(5, 5, 0)  #initialize matrix
        for i in range(0, 5):  #making matrix
            for j in range(0, 5):
                my_matrix[i][j] = key_string[i * 5 + j]

        decrypt(key_string)

    elif choice == 3:
        exit()
    else:
        print("Choose the correct choice")