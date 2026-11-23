# THE COPPER PLATE — news-image-20261122 — Akun 3

Entry gambar berita milik @cicihandayani (Akun 3) untuk bounty
news-image-20261122 di make.fun, dikerjakan pada gelombang 7.

## Gelombang 7

Gelombang ketujuh ini berdiri di atas pool segar Minggu 22 Nov
2026 — gabungan 15 kartu dan 21 brief yang membentuk 36 cerita
dari 7 region. Kanvasnya memuat strip angka 186 / 161 / 35% /
$120bn / 720 / 9 / 50. Bahan yang tidak lolos DATE CHECK dibuang
sebagai buangan bernama, tercatat jelas dan tidak dipakai lagi.

## Entry

- Dimensi: 1024x1024 piksel, memenuhi gerbang 1024x1024
- Ukuran: 228024 byte
- SHA256: 996a076c626166c755beabe1e37be589cb170b4f3372411d471a2210d6572e23
- Margin checker: 13/13 lulus

`main.py` memakai pustaka standar Python saja. Alurnya: membaca
33 byte pertama `entry.png` untuk memverifikasi signature PNG dan
IHDR serta dimensinya, menolak sisi di atas 1024, menyalin berkas
ke direktori keluaran byte-for-byte, lalu memverifikasi salinan
itu identik lewat sha256 dan ukuran.
