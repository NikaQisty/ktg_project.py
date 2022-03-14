#import tanggal dan waktu hari ini
import datetime
x = datetime.datetime.now()
tanggal ='['+x.strftime('%c')+']'

#tampilan utama daftar menu 
def tampilanUtama():
    print("""
    ============================================================
    |                        WELCOME TO                        |
    |                   Rumah Makan Cikuray                    |
    ============================================================
    
    SEDIA                        
    ------------------------------------------------------------   
    |                       Menu Lauk                          |
    ------------------------------------------------------------
    | 1. Ikan Nila Goreng   : Rp.10000                         |
    | 2. Ayam Goreng        : Rp.12000                         |
    | 3. Ayam Goreng Kremes : Rp.13000                         |
    | 4. Sosis Asam Manis   : Rp.7000                          |
    | 5. Ikan Lele Goreng   : Rp.10000                         | 
    | (Diskon 20% untuk pemesanan makanan min 5 porsi)         |
    ------------------------------------------------------------
    |                       Menu Minuman                       |
    ------------------------------------------------------------
    | 1. Teh Tawar  : Rp. 2000                                 |
    | 2. Teh Manis  : Rp. 3000                                 |
    | 3. Kopi Susu  : Rp. 3000                                 |
    | 4. Nutri Sari : Rp. 3000                                 |
    ------------------------------------------------------------
    *harga belum termasuk ppn 10%
          """)

def pilihanMakanan():
    #agar variabel dapat diakses secara global
    global pesanMakanan, jumlahMakanan, namaMakanan, diskon, harga, totalHargaMakanan, listHargaMakanan, hargaMakan
    
    #masukin inputan makanan
    pesanMakanan = int(input("Menu lauk yang dipilih (1-5) = "))

    #list harga makanan
    listHargaMakanan = [10000, 12000, 13000, 7000, 10000]

    #loop harga makanan sesuai inputan pesanMakanan
    for i in range (len(listHargaMakanan)):
        if i == pesanMakanan-1:
            hargaMakan = listHargaMakanan [i]
        else:
            continue

    #saat inputan sesuai opsi diantara 1-5
    if pesanMakanan >= 1 and pesanMakanan <= 5: 

        #jumlah makanan dapat diinputkan
        jumlahMakanan = int(input("Jumlah porsi yang dipesan = "))
        if pesanMakanan == 1:
            namaMakanan  = "Ikan Nila Goreng"
            if jumlahMakanan >= 5:
                harga = (10000 * jumlahMakanan)
                diskon = int(harga*0.2)
                totalHargaMakanan = int(harga-diskon)
            else:
                diskon = 0
                harga = (10000 * jumlahMakanan)
                totalHargaMakanan = (10000 * jumlahMakanan)

        elif pesanMakanan == 2:
            namaMakanan = "Ayam Goreng"
            if jumlahMakanan >= 5:
                harga = (12000 * jumlahMakanan)
                diskon = int(harga * 0.2)
                totalHargaMakanan =int(harga-diskon)
            else:
                diskon = 0
                harga = (12000 * jumlahMakanan)
                totalHargaMakanan = (12000 * jumlahMakanan)

        elif pesanMakanan == 3:
            namaMakanan = "Ayam Goreng Kremes"
            if jumlahMakanan >= 5:
                harga = int(13000 * jumlahMakanan)
                diskon = int(harga * 0.2)
                totalHargaMakanan = int(harga-diskon)
            else:
                diskon = 0
                harga = int(13000 * jumlahMakanan)
                totalHargaMakanan = (13000 * jumlahMakanan)

        elif pesanMakanan == 4:
            namaMakanan = "Sosis Asam Manis"
            if jumlahMakanan >= 5:
                harga = int(7000 * jumlahMakanan)
                diskon = int(harga * 0.2)
                totalHargaMakanan = int(harga-diskon)
            else:
                diskon = 0
                harga = int(7000 * jumlahMakanan)
                totalHargaMakanan = (7000 * jumlahMakanan)

        elif pesanMakanan == 5:
            namaMakanan = "Ikan Lele Goreng"
            if jumlahMakanan >= 5:
                harga = int(10000 * jumlahMakanan)
                diskon = int(harga * 0.2)
                totalHargaMakanan =int(harga-diskon)
            else:
                diskon = 0
                harga = int(10000 * jumlahMakanan)
                totalHargaMakanan = (10000 * jumlahMakanan)
        else :
            pass

    #jika inputan tidak sesuai opsi yang ada !==(1 sampai 5) kembali ke manu utama
    else:
        pilih = print("Pilihan makanan tidak tersedia, pilih kembali menu yang sesuai ")
        main()


def pilihanMinuman():
    #agar variabel dapat diakses secara global
    global pesanMinuman, jumlahMinuman, namaMinuman, hargaMinuman, harga_minum, listHargaMinuman

    #masukin inputan jenis dan jumlah minuman
    pesanMinuman = int(input("Menu minuman yang dipilih (1-4) = "))
    if pesanMinuman >= 1 and pesanMinuman <= 4:
        jumlahMinuman = int(input("Jumlah minuman yang dipesan = "))
    
    #jika inputan tidak sesuai opsi yang ada atau !==(1 sampai 4) kembali ke menu utama
    else:
        pilih = print("Pilihan minuman tidak tersedia, pilih kembali menu yang sesuai")
        main()

    #list harga minuman
    listHargaMinuman = [2000, 3000, 3000, 3000]

    #looping harga minuman berdasarkan minuman yang dipesan
    for i in range (len(listHargaMinuman)): # i = (0, 4) = 0, 1, 2, 3
        if i == pesanMinuman-1: 
            harga_minum = listHargaMinuman [i]
        else:
            continue
    
    if pesanMinuman == 1:
        namaMinuman = "Teh tawar"
        hargaMinuman = int(2000*jumlahMinuman)
    
    elif pesanMinuman == 2:
        namaMinuman = "Teh Manis"
        hargaMinuman = int(3000*jumlahMinuman)
            
    elif pesanMinuman == 3:
        namaMinuman = "Kopi Susu"
        hargaMinuman = int(3000*jumlahMinuman)

    elif pesanMinuman == 4:
        namaMinuman = "Nutri Sari"
        hargaMinuman = int(3000*jumlahMinuman)

    else:
        pilih = print("Pilihan minuman tidak tersedia, pilih kembali menu yang sesuai")
        main()


def bayar():
    global total, ppn, totalBayar
    if totalHargaMakanan == 0 and hargaMinuman == 0:
        total = 0
    else:
        total = hargaMinuman + totalHargaMakanan #seluruh harga makanan dan minuman
    ppn = int(total*0.1) #ppn dihitung 10% dari keseluruhuan total harga makanan dan minuman
    totalBayar = total + ppn

def struk():
    print("""
    ============================================================
    |                    Rumah Makan Cikuray                   |
    |                   Jl. Muncak kuy No.999                  |
    |                   Telp. 022 123 321 001                  |""")
    print("    |             Today, ", tanggal, "          |") #import tanggal dan waktu saat struk dicetak
    print("""
    ------------------------------------------------------------
    |                     STRUK PEMESANAN                      |
    ------------------------------------------------------------""")
    print("    Makanan   :", namaMakanan)
    print("    Harga     : Rp", hargaMakan)
    print("    Banyaknya :", jumlahMakanan)
    print("    Total     : Rp", harga, "(sebelum diskon)")
    print("    Diskon 20%: Rp", diskon)
    print("    Total     : Rp", totalHargaMakanan, "(sesudah diskon)")
    print("    ------------------------------------------------------------")
    print("    Minuman   :", namaMinuman)
    print("    Harga     : Rp", harga_minum)
    print("    Banyaknya :", jumlahMinuman)
    print("    Total     : Rp", hargaMinuman)
    print("    ------------------------------------------------------------")
    print("    Jumlah                   : Rp", total)
    print("    ppn 10%                  : Rp", ppn)
    print("    Total yang harus dibayar : Rp", totalBayar)
    print("""
    ------------------------------------------------------------   
    |             Terima kasih atas kunjungan anda             |
    |                    Sampai jumpa lagi!!                   | 
    ============================================================""")

def main():
    tampilanUtama()
    pilihanMakanan()
    pilihanMinuman()
    bayar()
    struk()
    pilihan = input ("\nKembali ke menu utama? Y/N : ")
    if pilihan == "y" :
        main()
    else:
        exit(0)

main()
