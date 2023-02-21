def hitung_luas():
    alas = float(input("Masukkan alas (cm): "))
    tinggi = float(input("Masukkan tinggi (cm): "))
    print("Luas =", 0.5 * alas * tinggi, "cm")


def diulang2():
    ulang = (input("apakah, mau di ulang? (y/n):   "))
    if ulang == "y":
        for i in range (1):
            hitung_luas()
            diulang2()
            i = 1
    else:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


hitung_luas()
diulang2()
