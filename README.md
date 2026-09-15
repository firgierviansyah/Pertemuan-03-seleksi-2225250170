# Pertemuan 03 Seleksi Python

Nama: Firgi Erviansyah
NIM: 2225250170
Kelas: 3B

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Struktur Folder

```text
pertemuan-03-seleksi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_genap_ganjil.py
│   ├── 02_bandingkan_dua_bilangan.py
│   ├── 03_kelulusan_bersyarat.py
│   └── 04_jenis_segitiga.py
└── tugas/
    └── analisis_persamaan_kuadrat.py
```

## Cara Menjalankan

Jalankan program melalui terminal VS Code:

```bash
python3 tugas/analisis_persamaan_kuadrat.py
```

Program akan meminta input berupa koefisien `a`, `b`, dan `c`.

## Algoritma Tugas

1. Masukkan nilai `a`, `b`, dan `c`.
2. Jika `a = 0`, program menampilkan bahwa input bukan persamaan kuadrat.
3. Jika `a ≠ 0`, hitung diskriminan dengan rumus `D = b² - 4ac`.
4. Jika `D > 0`, program menghitung dua akar real yang berbeda.
5. Jika `D = 0`, program menghitung satu akar real kembar.
6. Jika `D < 0`, program menampilkan bahwa tidak ada akar real.

## Hasil Pengujian

### Test Case 1

```text
Input:
a = 1
b = -5
c = 6

Keluaran yang diharapkan:
D = 1
x₁ = 3
x₂ = 2

Keluaran aktual:
D = 1.00
(x₁) = 3.00
(x₂) = 2.00

Status: Berhasil
```

### Test Case 2

```text
Input:
a = 1
b = 2
c = 1

Keluaran yang diharapkan:
D = 0
x = -1

Keluaran aktual:
D = 0.00
(x) = -1.00

Status: Berhasil
```

### Test Case 3

```text
Input:
a = 1
b = 0
c = 1

Keluaran yang diharapkan:
D = -4
Tidak ada akar real

Keluaran aktual:
D = -4.00
Tidak ada akar real

Status: Berhasil
```

### Test Case 4

```text
Input:
a = 0
b = 2
c = 3

Keluaran yang diharapkan:
Bukan persamaan kuadrat

Keluaran aktual:
Bukan persamaan kuadrat

Status: Berhasil
```

## Refleksi

Satu kesalahan logika yang perlu diperhatikan adalah ketika nilai `a = 0`. Jika tidak diperiksa terlebih dahulu, program dapat melakukan perhitungan akar dengan pembagi `2a` yang bernilai 0.

Cara memperbaikinya adalah dengan mengecek kondisi `a == 0` terlebih dahulu sebelum menghitung diskriminan dan akar.
