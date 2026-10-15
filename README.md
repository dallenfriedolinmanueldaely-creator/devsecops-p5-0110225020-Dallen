# Secure Task Manager

Secure Task Manager adalah aplikasi command-line sederhana untuk menambah, melihat, menyelesaikan, dan menghapus daftar tugas. Data disimpan secara lokal dalam file JSON.

## Teknologi
- Python 3.12+
- pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomasi CI dan security scanning

## Menjalankan aplikasi
Pastikan Python terpasang. Dari folder repository, jalankan:

```powershell
py -m pip install -r requirements.txt
py -m app.main add "Belajar DevSecOps"
py -m app.main list
py -m app.main done 1
py -m app.main delete 1
```

## Menjalankan pengujian dan SAST secara lokal

```powershell
py -m pytest -q
py -m bandit -r app -ll
```

Bandit dengan opsi `-ll` memeriksa temuan berlevel severity Medium dan High. Temuan yang memenuhi ambang tersebut membuat perintah gagal dan menjadi Quality Gate pipeline.

## Overview pipeline CI/CD
Workflow `.github/workflows/devsecops.yml` dipicu oleh `push` ke branch `main` dan `pull_request` yang menargetkan `main`. Job `build` memasang dependency dan menjalankan unit test. Job `sast-scan` baru berjalan setelah `build` berhasil (`needs: build`), lalu menjalankan Bandit. Laporan JSON Bandit disimpan sebagai artifact GitHub Actions agar dapat diperiksa setelah workflow selesai.

## Quality Gate
Quality Gate dinyatakan lolos bila Bandit tidak menemukan temuan dengan severity Medium atau High pada folder `app`. Jika ditemukan temuan pada ambang tersebut, langkah Bandit gagal dan job `sast-scan` berstatus gagal. Temuan Low tetap dapat muncul dalam laporan tetapi tidak menggagalkan gate ini.
