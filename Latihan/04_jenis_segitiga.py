print("=" * 40)
print("       SISTEM IDENTIFIKASI SEGITIGA")
print("=" * 40)

a = float(input("Masukkan sisi pertama  : "))
b = float(input("Masukkan sisi kedua    : "))
c = float(input("Masukkan sisi ketiga   : "))

print("\n" + "-" * 40)
print("              HASIL ANALISIS")
print("-" * 40)

if a == b and b == c:
    print("Jenis : SEGITIGA SAMA SISI")
    print("Keterangan : Ketiga sisi memiliki panjang yang sama.")
else:
    if a == b or a == c or b == c:
        print("Jenis : SEGITIGA SAMA KAKI")
        print("Keterangan : Ada dua sisi yang memiliki panjang sama.")
    else:
        print("Jenis : SEGITIGA SEMBARANG")
        print("Keterangan : Ketiga sisi memiliki panjang yang berbeda.")

print("=" * 40)