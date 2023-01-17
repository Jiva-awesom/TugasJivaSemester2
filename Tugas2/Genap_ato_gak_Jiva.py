
def even_no(lobster):
    for lele in lobster:
        if lele % 2 == 0:
            print("list berisi bilangan genap")
            break
    else:
        print("list ini TIDAK berisi bilangan genap")

baba = int((input("Berapa ulang?  ")))

no1 = int(input("Bilanang ke-1:  "))
no2 = int(input("Bilanang ke-2:  "))
no3 = int(input("Bilanang ke-3:  "))

for bobo in range(baba):
    print("for List bobo: ")
    even_no([no1, no2, no3])
    bobo += 1