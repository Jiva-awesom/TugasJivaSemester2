import Mod_Aritmatika_Jiva

def utama():
    a = int(input("Asupkean Nilai A :   "))
    b = int(input("Asupkean Nilai B :   "))


    print("a\t: %d" %a)
    print("b\t: %d" %b)


    print("a + b\t: %d" % Mod_Aritmatika_Jiva.tambah(a, b))
    print("a - b\t: %d" % Mod_Aritmatika_Jiva.korang(a, b))
    print("a x b\t: %d" % Mod_Aritmatika_Jiva.kalie(a, b))
    print("a ÷ b\t: %d" % Mod_Aritmatika_Jiva.bagi(a, b))

if __name__ == "__main__":
    utama()