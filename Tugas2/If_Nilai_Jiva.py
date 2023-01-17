Nilai = int(input("Masukkan Jumlah Nilai:  "))

if Nilai > 100:
    n = "A+"
elif Nilai >= 80:
    n = "A"
elif Nilai >= 70:
    n = "B+"
elif Nilai >= 60:
    n = "C"
elif Nilai >= 50:
    n = "D"
else:
    n = "E"

print(f"Nilai Tugas = {n}")
