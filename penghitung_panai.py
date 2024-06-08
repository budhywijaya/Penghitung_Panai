def penghitung_panai(pendidikan,dokter, haji, keluarga):
    uang_panai = 50000000
    if pendidikan == "S1":
        uang_panai+=25000000
    elif pendidikan == "S2":
        uang_panai+=50000000
    elif pendidikan == "S3":
        uang_panai+=100000000
    else:
        uang_panai+=10000000
    #Menghitung panai jika dokter dan/atau haji
    if dokter and haji:
        uang_panai+=300000000
    elif not dokter and haji :
        uang_panai+=100000000
    elif dokter and not haji:
        uang_panai+=200000000
    #menghitung panai jika keluarga bangsawan
    if keluarga:
        uang_panai+=50000000
    return uang_panai

if __name__ == "__main__":
    pendidikan = input("Masukkan pendidikan anda ").upper()
    keluarga_input = input("Anda termasuk keluarga bangsawan andi atau karaeng? ").lower()
    keluarga = keluarga_input in ["andi", "karaeng"]
    dokter_input = input("Apakah anda seorang dokter?(y/n) ").lower()
    dokter = dokter_input in["iya", "yes", "y"]
    haji_input = input("Apakah anda sudah berhaji?(y/n) ").lower()
    haji = haji_input in ["iya", "yes", "y"]
    uang = penghitung_panai(pendidikan, dokter, haji, keluarga)
    print("Uang ", uang)