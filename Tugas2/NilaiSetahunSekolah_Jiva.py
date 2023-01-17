tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

Nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

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

if Nilai > 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("Angka Nilai Akhir: %0.2f" % Nilai)
print("Huruf Nilai Setahun Sekolah: {}".format(n))
print("Status Siswa: {}".format(status))
