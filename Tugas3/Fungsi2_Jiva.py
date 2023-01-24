# membuat variabel globeal
nama = "Python"
ver = "1.0.0"


def jahanam():
    # var lokal
    nama = "C#"
    ver = "1.0.2"
    # akses var lokal
    print("Nama: %s" % nama)
    print("Versi : %s" % ver)


# akses var blobal
print(f"Nama: {nama}")
print(f"Versoi: {ver}")

# memanggil fungsi jahanam
jahanam()
