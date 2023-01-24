def luas_persegi(sisi):
    return sisi*sisi


# Tidak Menghasilkan Output Apa Pun
luas_persegi(10)

# Menghasilkan Output
print("Luas persegi dengan sisi 4 adalah", luas_persegi(4))

# Kita Juga Bisa Simpan Di Dalam Variable
persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)

print("Total luas persegi besar dan kecil adalah ", persegi_besar + persegi_kecil)