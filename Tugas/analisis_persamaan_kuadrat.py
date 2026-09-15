print("=" * 48)
print("       ANALISIS PERSAMAAN KUADRAT")
print("=" * 48)

a = float(input("Masukkan koefisien a : "))
b = float(input("Masukkan koefisien b : "))
c = float(input("Masukkan koefisien c : "))

print("\n" + "-" * 48)
print("                 HASIL ANALISIS")
print("-" * 48)

if a == 0:
    print("Status      : BUKAN PERSAMAAN KUADRAT")
    print("Keterangan  : Koefisien a tidak boleh bernilai 0.")

else:
    d = b ** 2 - 4 * a * c

    print(f"Persamaan   = {a:.2f}x² + {b:.2f}x + {c:.2f} = 0")
    print(f"Diskriminan = {d:.2f}")

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)

        print("Jenis akar  : DUA AKAR REAL BERBEDA")
        print(f"(x₁)        = {x1:.2f}")
        print(f"(x₂)        = {x2:.2f}")

    else:
        if d == 0:
            x = -b / (2 * a)

            print("Jenis akar  : AKAR REAL KEMBAR")
            print(f"(x)         = {x:.2f}")

        else:
            print("Jenis akar  : TIDAK ADA AKAR REAL")
            print("Keterangan  : Persamaan memiliki akar kompleks.")

print("=" * 48)