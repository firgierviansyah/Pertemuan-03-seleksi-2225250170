print("=" * 40)
print("      SISTEM CEK KELULUSAN")
print("=" * 40)

nilai = float(input("Masukkan nilai akhir   : "))
kehadiran = float(input("Masukkan kehadiran (%) : "))

print("\n" + "-" * 40)
print("              HASIL")
print("-" * 40)

if nilai >= 60 and kehadiran >= 80:
    print("Status : LULUS")
    print("Keterangan : Nilai dan kehadiran memenuhi syarat.")
else:
    print("Status : BELUM LULUS")
    print("Keterangan : Ada syarat yang belum terpenuhi.")

print("=" * 40)