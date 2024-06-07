
def penghitung_panai(pendidikan,dokter, haji, keluarga):
    uang_panai = 50000000
    pendidikan = pendidikan.upper()
    keluarga = keluarga.lower()
    if pendidikan == "S1":
        uang_panai+=25000000
    elif pendidikan == "S2":
        uang_panai+=50000000
    elif pendidikan == "S3":
        uang_panai+=100000000
    else:
        uang_panai+=10000000
    if dokter == True and haji == True:
        uang_panai+=300000000
    elif dokter == False and haji == True:
        uang_panai+=100000000
    elif dokter == True and haji == False:
        uang_panai+=200000000
    else:
        uang_panai+=0
    if keluarga == "andi" or keluarga == "karaeng":
        uang_panai+=50000000
    else:
        uang_panai+=0
    return uang_panai

if __name__ == "__main__":
    pendidikan = input("Masukkan pendidikan anda ")
    keluarga = input("Anda termasuk keluarga bangsawan andi atau karaeng? ")
    dokter = True
    haji = True
    uang = penghitung_panai(pendidikan, dokter, haji, keluarga)
    print("Uang ", uang)