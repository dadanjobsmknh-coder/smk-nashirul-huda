# Website SMK Nashirul Huda Bojonggambir

## Status

Phase 2 Foundation. Homepage penuh dan halaman konten akan dibangun pada phase berikutnya.

## Teknologi

- HTML5 multi-page
- CSS modular dan custom properties
- Vanilla JavaScript ES6 modules
- JSON data
- Tanpa framework dan tanpa backend

## Menjalankan secara lokal

`fetch()` untuk partial dan JSON tidak berjalan baik melalui `file://`. Jalankan server lokal dari folder project:

```bash
python -m http.server 5500
```

Lalu buka `http://localhost:5500`.

## File foundation utama

- `assets/css/tokens.css`: design tokens
- `assets/css/components.css`: komponen global
- `partials/header.html`: header dan navigasi bersama
- `partials/footer.html`: footer bersama
- `assets/js/component-loader.js`: partial loader
- `assets/js/data-loader.js`: JSON loader dan state error
- `assets/js/modal.js`: modal dengan focus trap
- `data/site.json`: identitas sekolah terpusat

## Relative path

Setiap halaman memiliki atribut `data-root` pada elemen `<html>`. Loader menggunakan atribut ini untuk membangun URL partial dan JSON.

## Data placeholder

Data yang belum diverifikasi memakai label `needs-review`, `placeholder`, atau teks dalam kurung siku. Jangan mengubahnya menjadi `verified` tanpa persetujuan sekolah.

## Deployment Vercel

Import repository sebagai proyek baru. Framework preset dapat diatur ke **Other**. Tidak diperlukan build command dan output directory menggunakan root project.

## Keamanan

Jangan menyimpan password, token, API key, data siswa, NIP/NUPTK, atau dokumen internal di repository publik.


## Phase 3 Homepage

Homepage kini membaca `data/homepage.json` dan dataset domain melalui `assets/js/homepage.js`. Gambar masih memakai placeholder SVG lokal agar proyek tidak bergantung pada layanan eksternal. Ganti file di `assets/images/placeholders/` dengan dokumentasi resmi sekolah tanpa perlu mengubah struktur komponen.


## Phase 4 Profile

Modul Profil menggunakan `assets/js/profile.js` dan dataset `profile.json`, `visi-misi.json`, `guru.json`, `staf.json`, `ekskul.json`, serta `fasilitas.json`. Direktori dapat dicari dan difilter. Detail personel menggunakan parameter `slug` dan `type`.


## Phase 5 Kompetensi

Halaman PPLG dan MPLB dirender melalui `assets/js/competency.js` dari `data/pplg.json` dan `data/mplb.json`. Struktur kurikulum ringkas juga tersedia pada `data/kurikulum.json`.


## Phase 6 Informasi

Sistem berita menggunakan `data/berita.json` dan `assets/js/information.js`. Contoh struktur tersedia pada `data/berita-schema.json`. Struktur organisasi memakai `data/organisasi.json`; detail stakeholder menggunakan parameter `slug`.


## Phase 7 Pembelajaran

Modul pembelajaran menggunakan `assets/js/learning.js` serta data `pembelajaran.json`, `kurikulum.json`, `jadwal.json`, `kalender-akademik.json`, `kegiatan.json`, dan `organisasi-siswa.json`. Jadwal per kelas belum diisi karena dokumen resminya belum tersedia.


## Phase 8 Layanan

Halaman layanan dirender melalui `assets/js/services.js` dari `data/layanan.json`. Biaya, durasi, jam layanan, formulir, dan ketentuan perwakilan tetap berupa placeholder sampai SOP resmi diberikan.


## Phase 9 Prestasi

Modul prestasi menggunakan `assets/js/achievements.js`, `data/prestasi.json`, dan `data/prestasi-schema.json`. Data resmi belum tersedia, sehingga semua halaman menggunakan empty state. Tambahkan record hanya setelah bukti dan izin publikasi diperoleh.


## Phase 10 Lulusan

Modul lulusan menggunakan `assets/js/graduates.js`, `data/lulusan.json`, `data/mitra.json`, dan `data/lulusan-schema.json`. Persentase tracer study serta mitra aktif tetap kosong sampai data agregat dan bukti kerja sama resmi tersedia.


## Phase 11 SPMB

Modul SPMB menggunakan `assets/js/spmb.js` dan `data/spmb.json`. Jadwal daftar ulang 11 Juli 2026 diperlakukan sebagai arsip. Jadwal baru, kuota, biaya, dan persyaratan final tetap menggunakan placeholder sampai data resmi diberikan. Formulir minat hanya menyusun pesan WhatsApp dan tidak menyimpan data.


## Phase 12 Kontak dan Utilitas

Menambahkan halaman Hubungi Kami, formulir WhatsApp tanpa penyimpanan data, pencarian global berbasis `data/search-index.json`, kebijakan privasi, sitemap HTML, dan halaman 404. Alamat footer diperbarui berdasarkan brosur resmi.


## FAQ Sekolah

Halaman `faq/index.html` menyediakan 30 pertanyaan berbasis `data/faq.json`, dengan pencarian, filter kategori, accordion, dan tautan kontekstual. FAQ juga ditambahkan ke header, menu mobile, footer, sitemap, dan indeks pencarian.


## Phase 14 Performance

Menambahkan WebP untuk pratinjau brosur, lazy loading global, service worker dan halaman offline, cache headers Vercel/Netlify, content-visibility, manifest relatif, serta `scripts/performance-audit.py`. PDF brosur tidak dimasukkan ke cache otomatis.
