# TUGAS 2
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
#### Link Aplikasi: https://joy-petkeeper-inventory.adaptable.app/main/
## 1. Membuat sebuah proyek Django baru.
Membuat virtual environment dengan nama "env".
``` 
python -m venv env
```
Mengaktifkan virtual environment yang telah dibuat sebelumnya. Ketika virtual environment aktif, semua perintah Python dan pip yang akan dijalankan akan terisolasi.
``` 
env\Scripts\activate.bat 
```
Membuat file requirements.txt dan menambahkan daftar dependensi yang dibutuhkan oleh proyek Django.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Menginstal semua dependensi tersebut ke dalam virtual environment.
```
pip install -r requirements.txt
```
Membuat proyek Django dengan nama "inventory".
```
django-admin startproject inventory .
```
Menambahkan konfigurasi ALLOWED_HOSTS = ["*"] ke dalam berkas settings.py proyek Django. Pengaturan ini memungkinkan Django untuk menerima permintaan dari semua host.\

Menjalankan server pengembangan Django.
```
python manage.py runserver
```
Membuka browser web http://localhost:8000 untuk memeriksa apakah proyek Django telah berhasil dibuat. Jika terlihat ikon roket, maka proyek Django telah aktif.\
Menekan tombol Ctrl+C dalam jendela command prompt untuk menghentikan server pengembangan Django.\

Menonaktifkan virtual environment yang telah diaktifkan sebelumnya.
```
deactivate
```

## 2. Membuat aplikasi dengan nama main pada proyek tersebut.
Membuat aplikasi Django baru dengan nama "main".
```
python manage.py startapp main
```
Menambahkan INSTALLED_APPS = [..., 'main', ...] dalam berkas settings.py.\
Membuat direktori baru bernama "templates" di dalam direktori "main".\
Membuat file baru bernama "main.html" di dalam direktori "templates" yang telah dibuat sebelumnya, dengan isi:
```
<h1><span style="color: blueviolet">{{ project }}</span></h1>
<h2>Name: <span style="color: lightcoral">{{ name }}</span></h2>
<h2>NPM: <span style="color: lightsalmon">{{ npm }}</span></h2>
<h2>Class: <span style="color: lightpink">{{ class }}</span></h2>
```

## 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Untuk melakukan routing agar dapat menjalankan aplikasi main, tambahkan kode pada "urls.py" dalam direktori "inventory" sebagai berikut:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
Mengaktifkan server Django untuk nantinya menjalankan aplikasi dan dapat diakses melalui browser web. 
```
python manage.py runserver
```

## 4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
- name sebagai nama item dengan tipe CharField.
- amount sebagai jumlah item dengan tipe IntegerField.
- description sebagai deskripsi item dengan tipe TextField.

Untuk mendefinisikan model data dalam aplikasi Django, tambahkan kode pada "models.py" dalam direktori "main":
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
```
Membuat migrasi untuk menggambarkan struktur tabel dalam database.
```
python manage.py makemigrations
```
Menerapkan migrasi tersebut ke database.
```
python manage.py migrate
```

## 5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Untuk mendefinisikan sebuah view dalam aplikasi Django, tambahkan kode pada "views.py" dalam direktori "main":
```
from django.shortcuts import render

def show_main(request):
    context = {
        "project": "Petkeeper Inventory",
        "name": "Joy Debora Sitorus",
        "npm": "2206082991",
        "class": "PBP D",
    }
    return render(request, "main.html", context)
```

## 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Untuk mengimpor fungsi view "show_main" dari modul "main.views", tambahkan kode pada "urls.py" dalam direktori "main":
```
from django.urls import path
from main.views import show_main

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
```

## 7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Sign in menggunakan akun GitHub pada Adaptable.io.\
Jika sudah sign in, tekan tombol New App, pilih Connect an Existing Repository.\ 
Pilihlah repositori proyek inventory sebagai basis aplikasi yang akan di-deploy.\
Pilih main branch sebagai branch yang ingin dijadikan deployment.\
Pilih Python App Template sebagai template deployment.\
Pilih PostgreSQL sebagai tipe basis data yang akan digunakan.\
Sesuaikan versi python dengan spesifikasi aplikasi, yaitu 3.11.\
Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn inventory.wsgi.\
Masukkan nama aplikasi yang akan menjadi nama domain situs web aplikasimu, yaitu joy-petkeeper-inventory.\
Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.\

## 8. Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Menginisialisasi repositori Git di direktori saat ini.
```
git init
```
Menambahkan file "README.md" pada git.
```
git add README.md
```
Menampilkan status repositori Git. Git status akan menunjukkan file-file yang telah diubah atau ditambahkan.
```
git status
```
Membuat commit dengan pesan commit "Inventory", untuk menyimpan perubahan yang dilakukan.
```
git commit -m "Inventory"
```
Mengganti nama branch default dari "master" ke "main".
```
git branch -M main
```
Menghubungkan repositori lokal dengan repositori remote di GitHub.
```
git remote add origin https://github.com/joydebora/Inventory.git
```
Mengirimkan perubahan yang telah di-commit dari repositori lokal ke repositori remote di GitHub. 
```
git push -u origin main
```

## 9. Testing Dasar (Bonus)
Untuk membuat unit tes untuk model Product dalam aplikasi yang telah dibuat, tambhakan kode pada "tests.py" dalam direktori "main":
```
from django.test import TestCase
from .models import Product

class PetkeeperInventoryTest(TestCase):
    def setUp(self):
        # Membuat data uji coba
        Product.objects.create(name="Makanan Kucing", amount=50, description="Makanan kucing premium", category="Makanan")
        Product.objects.create(name="Gembok Kandang", amount=10, description="Gembok anti-korosi", category="Perlengkapan")

    def test_item_create(self):
        makanan_kucing = Product.objects.get(name="Makanan Kucing")
        gembok_kandang = Product.objects.get(name="Gembok Kandang")
        
        self.assertEqual(makanan_kucing.amount, 50)
        self.assertEqual(gembok_kandang.amount, 10)
        self.assertEqual(makanan_kucing.category, "Makanan")
        self.assertEqual(gembok_kandang.category, "Perlengkapan")

    def test_item_description(self):
        makanan_kucing = Product.objects.get(name="Makanan Kucing")
        gembok_kandang = Product.objects.get(name="Gembok Kandang")
        
        self.assertEqual(makanan_kucing.description, "Makanan kucing premium")
        self.assertEqual(gembok_kandang.description, "Gembok anti-korosi")
```
Penjelasan:
- PetkeeperInventoryTest adalah kelas tes yang diturunkan dari TestCase yang disediakan oleh Django. Ini adalah kelas utama untuk menulis tes dalam Django.
- setUp adalah metode yang dijalankan sebelum setiap tes. Di dalamnya, terdapat dua objek Product dengan data uji coba.
- test_item_create adalah metode tes pertama. Di dalamnya, akan mengambil dua objek Product berdasarkan nama dan kemudian menggunakan pernyataan self.assertEqual untuk memeriksa apakah atribut amount dan category sesuai dengan yang diharapkan. 
- test_item_description adalah metode tes kedua. Di dalamnya, akan mengambil lagi dua objek Product berdasarkan nama dan kemudian menggunakan pernyataan self.assertEqual untuk memeriksa apakah atribut description sesuai dengan yang diharapkan.

Jalankan tes.
```
python manage.py test
```
Jika tes berhasil dilakukan, maka akan mengeluarkan informasi berikut:
```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
Destroying test database for alias 'default'... 
```

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Framework](https://i.postimg.cc/KcftbPHR/MTV-Framework.png)
Penjelasan:
- File urls.py mengarahkan permintaan HTTP dan diteruskan ke view yang tepat.\
- File views.py mengambil permintaan melalui template, berinteraksi dengan model jika diperlukan, dan merender template HTML.\
- File models.py mendefinisikan struktur data dan berinteraksi dengan database.\
- File HTML digunakan untuk merancang tampilan halaman web yang akan ditampilkan kepada user, dan mereka dapat menerima data dari views untuk menampilkan informasi yang diperlukan.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita menggunakan virtual environment karena:
1. Dependensi proyek --agar setiap proyek memiliki lingkungan kerja terisolasi. Ini seperti memiliki rak khusus untuk setiap proyek, sehingga kita tidak mencampuradukkan alat dan bahan antara proyek-proyek yang berbeda.
2. Menghindari konflik --virtual environment juga membantu dalam menghindari konflik versi. Kita bisa memiliki versi berbeda dari alat yang sama untuk setiap proyek tanpa menyebabkan masalah di proyek lain.
3. Proyek rapih dan bersih --dengan virtual environment, kita dapat menjaga proyek kita tetap bersih dan tertib. Kita dapat dengan mudah menghapus atau mengupdate alat yang kita perlukan tanpa memengaruhi proyek lain.
4. Mengontrol versi python --virtual environment juga memungkinkan kita mengontrol versi Python yang digunakan dalam setiap proyek. Ini bermanfaat jika kita perlu menjaga kompatibilitas dengan versi Python tertentu.

Dalam pengembangan aplikasi yang cukup kompleks atau yang bekerja dengan beberapa proyek sekaligus, penggunaan virtual environment menjadi keharusan untuk menjaga kerapihandan dan kebersihan proyek. Jika kita tidak menggunakan virtual environment, maka dalam prosesnya kita dapat menghadapi sejumlah masalah yang melibatkan konflik dependensi, kesulitan dalam mengelola versi Python, dan kesulitan dalam mengisolasi proyek dari sistem global host. Oleh karena itu, sangat disarankan untuk melakukan penggunaan virtual environment saat mengembangkan aplikasi web, terutama yang berbasis Django atau proyek Python lainnya.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Model-View-Controller (MVC), Model-View-Template (MVT), dan Model-View-ViewModel (MVVM) adalah pola desain (design pattern) yang digunakan dalam pengembangan perangkat lunak untuk memisahkan berbagai komponen dalam aplikasi. Di bawah ini adalah penjelasan singkat tentang masing-masing dari mereka dan perbedaannya:

1. MVC (Model-View-Controller)\
Model: Representasi dari data dan logic aplikasi. Model mengelola data dan mengatur aturan aplikasi.\
View: Bertanggung jawab untuk menampilkan data kepada pengguna dan menerima input dari mereka. View adalah bagian yang terlihat oleh pengguna.\
Controller: Berfungsi sebagai perantara antara Model dan View. Mengatur alur aplikasi, menghubungkan tindakan pengguna dengan perubahan di Model, dan mengupdate View.\
Perbedaan Utama: Dalam MVC, Controller berperan sebagai perantara yang menghubungkan Model dan View. Model dan View tidak berinteraksi langsung satu sama lain.

2. MVT (Model-View-Template)\
Model: Sama seperti dalam MVC, model adalah bagian yang menangani data dan logic aplikasi.\
View: Bertanggung jawab untuk menampilkan data kepada pengguna, tetapi dalam Django (sebuah framework Python yang menggunakan MVT), View juga mengatur logika aplikasi.\
Template: Template adalah bagian yang mirip dengan View dalam MVC. Template mengontrol tampilan halaman web dan cara data ditampilkan kepada pengguna.\
Perbedaan Utama: Dalam MVT (khususnya dalam Django), View dan Template berperan lebih terintegrasi dalam mengelola tampilan dan logika aplikasi.

3. MVVM (Model-View-ViewModel)\
Model: Seperti dalam MVC dan MVT, Model berhubungan dengan data dan logic aplikasi.\
View: View adalah bagian yang menampilkan data kepada pengguna, mirip dengan View dalam MVC dan MVT.\
ViewModel: ViewModel adalah bagian yang berfungsi sebagai penghubung antara Model dan View. Ini mempersiapkan data dari Model untuk ditampilkan di View dan mengelola tindakan pengguna yang mempengaruhi Model.\
Perbedaan Utama: Dalam MVVM, ViewModel mengambil peran yang lebih kuat dalam mengelola interaksi antara View dan Model. ViewModel memungkinkan untuk mengikat data langsung ke tampilan tanpa melibatkan logika aplikasi di dalam View.