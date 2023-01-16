# dekdlasllarasi
array = []
total = 0
# i nput kjumkladh elemen
n = int(input("Masukkan jumlah INPUT ARRAY:   "))

for x in range(n):
    nilai = float(input("Masukkan Nilai ke- {} :" .format(x+1)))
    array.append(nilai)
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    print("Hasil rata - rata adalah : {}".format(sum(array)/n))
