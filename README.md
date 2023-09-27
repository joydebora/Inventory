# TUGAS 2
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
#### Link Aplikasi: https://joy-petkeeper-inventory.adaptable.app/main/
![App1](https://i.postimg.cc/Gt5JBdcP/Whats-App-Image-2023-09-19-at-18-11-23.jpg)
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
Untuk membuat unit tes untuk model Product dalam aplikasi yang telah dibuat, tambahkan kode pada "tests.py" dalam direktori "main":
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
- File urls.py mengarahkan permintaan HTTP dan diteruskan ke view yang tepat.
- File views.py mengambil permintaan melalui template, berinteraksi dengan model jika diperlukan, dan merender template HTML.
- File models.py mendefinisikan struktur data dan berinteraksi dengan database.
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
Controller: Berfungsi sebagai perantara antara Model dan View. Mengatur alur aplikasi, menghubungkan tindakan pengguna dengan perubahan di Model, dan mengupdate View.

2. MVT (Model-View-Template)\
Model: Sama seperti dalam MVC, model adalah bagian yang menangani data dan logic aplikasi.\
View: Bertanggung jawab untuk menampilkan data kepada pengguna, tetapi dalam Django (sebuah framework Python yang menggunakan MVT), View juga mengatur logika aplikasi.\
Template: Template adalah bagian yang mirip dengan View dalam MVC. Template mengontrol tampilan halaman web dan cara data ditampilkan kepada pengguna.

3. MVVM (Model-View-ViewModel)\
Model: Seperti dalam MVC dan MVT, Model berhubungan dengan data dan logic aplikasi.\
View: View adalah bagian yang menampilkan data kepada pengguna, mirip dengan View dalam MVC dan MVT.\
ViewModel: ViewModel adalah bagian yang berfungsi sebagai penghubung antara Model dan View. Ini mempersiapkan data dari Model untuk ditampilkan di View dan mengelola tindakan pengguna yang mempengaruhi Model.

Perbedaan MVC, MVT, dan MVVM:
- Dalam MVC, Controller berperan sebagai perantara yang menghubungkan Model dan View. Model dan View tidak berinteraksi langsung satu sama lain.
- Dalam MVT (khususnya dalam Django), View dan Template berperan lebih terintegrasi dalam mengelola tampilan dan logika aplikasi.
- Dalam MVVM, ViewModel mengambil peran yang lebih kuat dalam mengelola interaksi antara View dan Model. ViewModel memungkinkan untuk mengikat data langsung ke tampilan tanpa melibatkan logika aplikasi di dalam View.

# TUGAS 3
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
#### Link Aplikasi: http://joy.debora-tutorial.pbp.cs.ui.ac.id/
![App2](https://i.postimg.cc/ydTL8Mgn/Whats-App-Image-2023-09-20-at-06-02-55.jpg)
## 1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
Mengaktifkan virtual environment (lingkungan virtual) dalam proyek Django:
```
env\Scripts\activate.bat
```
Konfigurasi URL patterns (pola URL) pada proyek Django Inventory:
```
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
Menjalankan server untuk dapat melihat aplikasi web secara lokal di komputer. Buka pada url http://localhost:8000/ untuk melihat hasilnya.
```
python manage.py runserver
```
Membuat berkas template HTML "base.html" pada root folder. Berkas ini digunakan sebagai dasar halaman web dalam proyek Django.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
Melakukan konfigurasi template engine (untuk menghasilkan tambpilan HTML) dalam Django, dengan menambahkan bagian TEMPLATES pada berkas settings.py di subdirektori Inventory:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
```
Untuk merender tampilan halaman web dalam aplikasi, ubah kode berkas main.html pada subdirektori templates di direktori main:
```
{% extends 'base.html' %}

{% block content %}
    <h1><span style="color: blueviolet">{{ inventory }}</span></h1>

    <h2>Name: <span style="color: lightcoral">{{ name }}</span></h2>
    <h2>NPM: <span style="color: lightsalmon">{{ npm }}</span></h2>
    <h2>Class: <span style="color: lightpink">{{ class }}</span></h2>
{% endblock content %}
```
Untuk mendefinisikan bentuk form yang akan digunakan dalam aplikasi, buat berkas forms.py pada direktori main:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
```
Tambahkan import modul yang diperlukan pada berkas views.py di direktori main:
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from .models import Product
```
Buat fungsi baru create_product, untuk menangani pembuatan produk baru dalam aplikasi:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Ubah fungsi show_main. Fungsi ini mengambil semua produk dari basis data menggunakan Product.objects.all(), yang nantinya akan digunakan oleh berkas template "main.html."
```
def show_main(request):
    products = Product.objects.all()
    
    context = {
        "inventory": "Petkeeper Inventory",
        "name": "Joy Debora Sitorus",
        "npm": "2206082991",
        "class": "PBP D",
        'products': products
    }

    return render(request, "main.html", context)
```
Tambahkan import modul yang diperlukan pada berkas urls.py di direktori main:
```
from main.views import show_main, create_product
```
Menambahkan path URL untuk mengarahkan permintaan ke view 'create_product':
```
path('create-product', create_product, name='create_product'),
```
Buat berkas baru 'create_product.html' pada folder templates di direktori main. 'create_product.html' merupakan berkas template yang meng-extend dari berkas "base.html":
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Tambahkan kode di dalam {% block content %} pada berkas 'main.html' pada folder templates di direktoi main. Kode ini adalah berkas template yang akan digunakan untuk menampilkan daftar produk dalam inventory:
```
...
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Category</th>
            <th>Price</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.category}}</td>
                <td>{{product.price}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
{% endblock content %}
```
Tambahkan kode di dalam class Product, untuk mendefinisikan model Product yang akan digunakan, pada berkas 'models.py' di direktoi main:
class Product(models.Model):
```
   name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
```
Jalankan perintah untuk menghasilkan file migrasi yang berisi instruksi untuk mengubah basis data sesuai dengan definisi model.
```
python manage.py makemigrations
```
Jalankan perintah untuk menerapkan perubahan ke dalam basis data sesuai dengan migrasi yang telah dibuat.
```
python manage.py migrate
```
Menjalankan server Django agar dapat mengakses aplikasi melalui browser.
```
python manage.py runserver
```

## 2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Tambahkan import modul Django yang diperlukan untuk mengambil dan mengembalikan data dalam format XML atau JSON, pada berkas 'views.py' di direktoi main:
```
from django.http import HttpResponse
from django.core import serializers
```
Tambahkan fungsi untuk mengambil semua data produk dari model Product dan mengembalikannya dalam format data yang ditentukan: 
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Tambahkan import fungsi-fungsi view yang akan digunakan dalam URL patterns, pada berkas 'urls.py' di direktori main: 
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
Untuk melakukan konfigurasi URL patterns dalam aplikasi Django, tambahkan path url kedalam urlpatterns pada berkas 'urls.py' di direktori main:
```
urlpatterns = [
...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

## Apa perbedaan antara form POST dan form GET dalam Django?
Form POST dan form GET adalah dua metode pengiriman data dalam Django yang memiliki perbedaan penting.

#### Form POST
1. Post digunakan untuk mengirim data (file, data formulir, dll.) ke server. Jika pembuatan berhasil, Post mengembalikan kode status HTTP 201 (Created).
2. Digunakan untuk mengirim data ke server dengan cara yang tidak terlihat oleh pengguna. Data yang dikirim dengan metode POST disertakan dalam body permintaan HTTP dan tidak terlihat di URL. Metode ini cocok untuk mengirim data sensitif seperti kata sandi atau informasi pribadi.

#### Form GET
1. Get digunakan untuk membaca/mengambil data dari server web. Get akan mengembalikan kode status HTTP 200 (OK) jika data berhasil diambil dari server.
2. Get digunakan untuk mengirim data ke server dengan cara yang terlihat oleh pengguna. Data yang dikirim dengan metode GET disertakan dalam URL sebagai parameter query. Metode ini cocok untuk mengirim data yang tidak sensitif, seperti permintaan pencarian atau filter.

Perbedaan utama antara kedua metode ini adalah dalam implementasi penggunaannya, form POST lebih sering digunakan ketika mengirim data sensitif seperti kata sandi, informasi kartu kredit, atau informasi pribadi lainnya. Form GET lebih umum digunakan untuk permintaan pencarian, filter, atau tautan yang dapat dibagikan.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML adalah format yang digunakan untuk pengiriman data antara aplikasi atau dalam konteks membangun halaman web. Ketiga format ini memiliki tujuan yang berbeda, yaitu menyimpan dan mengirim data secara hierarkis (XML), pertukaran data antara aplikasi (JSON), dan membangun halaman web (HTML).

#### XML (eXtensible Markup Language)
Merupakan bahasa markup yang digunakan untuk menyimpan dan mengirim data secara hierarkis. XML memberikan fleksibilitas yang tinggi dalam mendefinisikan struktur data sesuai kebutuhan pengguna. Dalam XML, pengguna dapat dengan mudah menentukan elemen dan atribut yang sesuai dengan kebutuhan mereka. Namun, XML memiliki overhead yang lebih besar dalam hal ukuran file dan kompleksitas parsing. Hal ini dapat mempengaruhi kinerja aplikasi ketika mengolah data XML yang besar.

#### JSON (JavaScript Object Notation)  
Merupakan format ringkas yang digunakan untuk pertukaran data antara aplikasi. JSON menggunakan struktur data berbasis teks dan lebih mudah dibaca oleh manusia. JSON memiliki sintaksis yang sederhana dan intuitif, dengan menggunakan objek dan array yang mirip dengan struktur data dalam bahasa pemrograman. JSON juga lebih ringan dan lebih efisien dalam hal ukuran file dan parsing dibandingkan dengan XML. Karena itulah, JSON menjadi pilihan yang populer dalam komunikasi antara aplikasi.

#### HTML (Hypertext Markup Language)  
Merupakan bahasa markup yang digunakan untuk membangun halaman web. HTML digunakan untuk mengatur tampilan dan struktur konten di web. Meskipun HTML mirip dengan XML dalam hal sintaksis, HTML memiliki aturan dan elemen yang telah ditentukan sebelumnya untuk membangun halaman web. HTML menggunakan tag-tag yang telah didefinisikan secara khusus, seperti `<html>`, `<head>`, `<body>`, dan lain-lain, untuk mengatur tampilan dan struktur halaman web. HTML juga mendukung penggunaan CSS (Cascading Style Sheets) untuk mengatur tampilan halaman web dengan lebih rinci.

Jadi, perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah format, fleksibilitas, kompleksitas, dan tujuan penggunaannya. XML menyediakan fleksibilitas dalam mendefinisikan struktur data, sementara JSON lebih ringan dan lebih mudah dibaca oleh manusia. HTML, di sisi lain, digunakan khusus untuk membangun halaman web dengan aturan dan elemen yang telah ditentukan sebelumnya.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan yang membuatnya menjadi pilihan yang populer. Berikut adalah beberapa alasan mengapa JSON sering digunakan:

1. **Ringan**: \
JSON memiliki format yang ringan dan sederhana, sehingga mudah untuk dibaca dan ditulis oleh manusia maupun mesin. Dalam pertukaran data, ukuran file JSON cenderung lebih kecil dibandingkan dengan format data lainnya seperti XML, sehingga mengurangi beban jaringan dan mempercepat waktu respons.
2. **Mudah Dipahami**: \
Struktur data dalam JSON mirip dengan struktur objek dalam banyak bahasa pemrograman, sehingga mudah dipahami dan diinterpretasikan. Hal ini memungkinkan pengembang untuk dengan cepat memahami dan mengolah data yang dikirim atau diterima dalam format JSON.
3. **Dukungan Luas**: \
JSON didukung oleh hampir semua bahasa pemrograman dan framework, menjadikannya pilihan yang serbaguna untuk pertukaran data. Hal ini memudahkan integrasi antara aplikasi web dengan berbagai teknologi dan platform yang berbeda, tanpa mengharuskan perubahan besar pada kode atau struktur data.
4. **Komunikasi Antar Platform**: \
JSON memungkinkan pertukaran data antara berbagai platform, seperti aplikasi web dengan server backend, dan antara aplikasi web dengan layanan pihak ketiga. Dalam arsitektur mikroservis dan aplikasi yang terdistribusi, JSON menjadi format standar untuk komunikasi antar layanan, sehingga mempermudah pengiriman dan penerimaan data di berbagai bagian sistem.
5. **Kecepatan**: \
JSON memiliki parsing dan serialisasi yang efisien, sehingga dapat mengurangi beban jaringan dan waktu respons dalam pertukaran data. Kemampuan JSON untuk dengan cepat diubah menjadi objek atau struktur data yang dapat digunakan oleh aplikasi membuatnya menjadi pilihan yang ideal untuk mengirim data dalam jumlah besar dan memprosesnya dengan efisien.

## Mengakses kelima URL di poin 2 menggunakan Postman.
Setelah format XML, JSON, XML by ID, dan JSON by ID berhasil ditambahkan, buka Postman dan buat request baru dengan method GET dan url berikut untuk mengetes apakah data terkirimkan dengan baik:

**URL: http://localhost:8000/**
![Html1](https://i.postimg.cc/ZK3vMcLH/Whats-App-Image-2023-09-20-at-09-35-57.jpg)
![Html2](https://i.postimg.cc/G2HHJJ2k/Whats-App-Image-2023-09-20-at-09-35-57-1.jpg)
![Html3](https://i.postimg.cc/wTWZnXTt/Whats-App-Image-2023-09-20-at-09-35-57-2.jpg)
![Html4](https://i.postimg.cc/TwqH0m43/Whats-App-Image-2023-09-20-at-09-35-57-3.jpg)
![Html5](https://i.postimg.cc/G3K5sFDM/Whats-App-Image-2023-09-20-at-09-35-57-4.jpg)

**URL: http://localhost:8000/xml**
![Xml1](https://i.postimg.cc/R0wPCK9L/Whats-App-Image-2023-09-20-at-09-36-27.jpg)
![Xml2](https://i.postimg.cc/pLFCkz9M/Whats-App-Image-2023-09-20-at-09-36-27-1.jpg)

**URL: http://localhost:8000/json**
![Json1](https://i.postimg.cc/G2qx9jfG/Whats-App-Image-2023-09-20-at-09-37-39.jpg)
![Json2](https://i.postimg.cc/wx4kp0Ld/Whats-App-Image-2023-09-20-at-09-37-39-1.jpg)
![Json3](https://i.postimg.cc/8CGRH3QL/Whats-App-Image-2023-09-20-at-09-37-39-2.jpg)

**URL: http://localhost:8000/xml/1/**
![Xml/id](https://i.postimg.cc/j5dzV7j5/Whats-App-Image-2023-09-20-at-09-37-50.jpg)

**URL: http://localhost:8000/json/1/**
![Json/id](https://i.postimg.cc/vTC962tg/Whats-App-Image-2023-09-20-at-09-38-02.jpg)

# TUGAS 4
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
![App3](https://i.postimg.cc/jdSMNrp2/Whats-App-Image-2023-09-27-at-06-34-15.jpg)
## 1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
#### Fungsi Registrasi
Mengaktifkan virtual environment (lingkungan virtual) dalam proyek Django:
```
env\Scripts\activate.bat
```
Tambahkan import modul yang diperlukan pada berkas urls.py di direktori main:
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
Menambahkan fungsi register untuk  mengelola proses pendaftaran pengguna, yang mencakup validasi formulir pendaftaran, penyimpanan data pengguna, pesan sukses, dan pengalihan ke halaman login jika pendaftaran berhasil.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Membuat berkas 'register.html' pada folder templates di subdirektori main, sebagai tampilan halaman registrasi dalam proyek Django, yang didasarkan pada berkas 'base.html' untuk komponen-komponen tampilan dasar, dan menampilkan formulir pendaftaran, pesan, dan elemen-elemen lainnya.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
Pada urls.py di subdirektori main, mengimpor fungsi register dari modul main.views agar bisa digunakan dalam konfigurasi URL proyek Django.
```
from main.views import register
```

Menambahkan path URL dengan pola 'register/' ke dalam urlpatterns, sehingga user dapat mengakses halaman registrasi melalui URL.
```
...
path('register/', register, name='register'),
...
```

#### Fungsi Login
Pada berkas 'views.py' di subdirektori main, mengimpor modul yang digunakan untuk mengelola otentikasi pengguna dalam aplikasi.
```
from django.contrib.auth import authenticate, login
```

Membuat fungsi login_user yang mengelola proses otentikasi pengguna berdasarkan data yang diterima dari formulir login. Jika otentikasi berhasil, pengguna akan diarahkan ke halaman utama, sedangkan jika gagal, pesan kesalahan akan ditampilkan.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Membuat berkas baru 'login.html' pada folder templates di subdirektori main, yang digunakan sebagai tampilan halaman login, yang didasarkan pada berkas 'base.html' untuk komponen-komponen tampilan dasar, dan menampilkan formulir login, pesan, dan tautan untuk pendaftaran akun jika belum memiliki akun.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
Mengimpor fungsi login_user dari modul main.views pada berkas 'urls.py' di subdirektori main:
```
from main.views import login_user
```

Menambahkan path URL kedalam url_patterns dengan pola 'login/', yang akan menghubungkan URL '/login/' dengan fungsi login yang telah diimpor sebelumnya.
```
...
path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
...
```

#### Fungsi Logout
Pada berkas 'views.py' di subdirektori main, mengimpor modul yang digunakan untuk mengelola proses keluar pengguna dari sesi aplikasi.
```
from django.contrib.auth import logout
```
Membuat fungsi logout_user yang menghentikan sesi pengguna (logout) dalam aplikasi dan mengarahkannya kembali ke halaman login setelah logout berhasil.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Pada berkas 'main.html' pada folder templates, subdirektori main, membuat sebuah button (link) yang ketika diklik akan mengarahkan pengguna ke halaman logout dalam proyek Django.
```
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
-- tambahkan import pada urls.py di subdirektori main:
```
Mengimpor fungsi logout_user dari modul main.views pada berkas 'urls.py' di subdirektori main:
```
Menambahkan path URL kedalam url_patterns dengan pola 'logout/', yang akan menghubungkan URL '/logout/' dengan fungsi logout yang telah diimpor sebelumnya.
```
...
path('logout/', logout_user, name='logout'),
...
```


#### Meresktriksi Akses
Pada berkas 'views.py' pada subdirektori main, menambahkan decorator login_required untuk memastikan bahwa hanya pengguna yang sudah login dapat mengakses fungsi show_main, dan jika pengguna belum login, mereka akan diarahkan ke halaman login dengan URL '/login'
```
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='/login')
def show_main(request):
...
```
Mengaktifkan server Django untuk nantinya menjalankan aplikasi dan dapat diakses melalui browser web.
```
python manage.py runserver
```
Menjalankan server untuk dapat melihat aplikasi web secara lokal di komputer. Buka pada url http://localhost:8000/ untuk melihat hasilnya.

Tampilan aplikasi:
![App3](https://i.postimg.cc/jdSMNrp2/Whats-App-Image-2023-09-27-at-06-34-15.jpg)
![App4](https://i.postimg.cc/xdg4Bybj/Whats-App-Image-2023-09-27-at-06-26-22.jpg)


## 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.


## 3. Menghubungkan model Item dengan User.
Pada berkas 'models.py' di subdirektori main, mendefinisikan model Product dalam aplikasi dengan relasi ForeignKey ke model user, sehingga setiap produk akan terkait dengan pengguna tertentu yang memilikinya.
```
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Mengubah fungsi create_product pada views.py di subdirektori main, untuk menghandle pembuatan produk dengan menghubungkan produk yang dibuat dengan user yang saat ini login dan mengarahkannya kembali ke halaman utama setelah produk berhasil dibuat.
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
Mengbah fungsi show_main pada views.py di subdirektori main, untuk mengambil produk-produk yang terkait dengan pengguna yang saat ini login dan mengatur konteks untuk halaman utama dengan daftar produk tersebut.
```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'inventory': 'Petkeeper Inventory',
    ...
    }
...
```

## 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Pada berkas 'views.py' pada subdirektori main, mengimpor modul untuk menghandle request seperti redirection dan penggunaan tanggal dan waktu dalam aplikasi Django.
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
Mengubah fungsi login_user, untuk mengatur cookie 'last_login' dengan waktu masuk terakhir pengguna dan mengarahkan pengguna ke halaman utama setelah berhasil login.
```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
Pada fungsi show_main, menambahkan waktu terakhir login pengguna, yang akan digunakan untuk ditampilkan dalam halaman utama.
```
context = {
        'inventory': 'Petkeeper Inventory',
        'name': 'Joy Debora Sitorus',
        'npm': '2206082991',
        'class': 'PBP D',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }
```
Mengubah fungsi logout_user untuk menghapus cookie 'last_login', yang mengatur waktu masuk terakhir pengguna, dan mengarahkan pengguna kembali ke halaman login setelah berhasil logout.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Pada berkas 'main.html' di folder templates, subdirektori main, menampilkan informasi tentang waktu masuk terakhir pengguna dalam halaman utama, yang diambil dari variabel konteks 'last_login'.
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm adalah salah satu formulir bawaan (built-in form) yang disediakan oleh Django untuk mempermudah proses pembuatan pengguna (user) dalam aplikasi web. Form ini digunakan untuk membuat formulir pendaftaran pengguna yang mencakup bidang seperti username, password, dan konfirmasi password.

**Kelebihan UserCreationForm:**
1. Pengelolaan Otentikasi yang Aman: Form ini memastikan bahwa password yang dimasukkan oleh pengguna disimpan dengan aman dalam bentuk terenkripsi.
2. Validasi yang Kuat: Form ini mencakup validasi bawaan seperti verifikasi password yang cocok, dan validasi keunikan untuk username.
3. Integrasi dengan Sistem Otentikasi Django: Form ini terintegrasi dengan baik dengan sistem otentikasi Django, sehingga memudahkan penggunaan otentikasi dalam proyek Django.
4. Dokumentasi yang Baik: Karena merupakan bagian dari Django, formulir ini didokumentasikan dengan baik dalam dokumentasi resmi Django.

**Kekurangan UserCreationForm:**
1. Kustomisasi Terbatas: Meskipun UserCreationForm memudahkan pembuatan pengguna dengan cepat, jika memerlukan formulir pendaftaran yang sangat disesuaikan atau memiliki persyaratan khusus, kita mungkin perlu menambahkan validasi dan bidang tambahan secara manual.
2. Tidak Cocok untuk Semua Kasus: Form ini mungkin tidak cocok untuk semua aplikasi karena setiap aplikasi memiliki persyaratan pendaftaran yang berbeda. Penggunaan formulir ini secara default mungkin tidak mencakup semua kebutuhan Anda.
3. Desain Tampilan Default: Tampilan yang dihasilkan oleh UserCreationForm mungkin perlu disesuaikan dengan desain tampilan spesifik proyek Anda.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
**Autentikasi:** proses verifikasi identitas user, yaitu memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah user yang mereka klaim.\
Dalam Django, autentikasi biasanya diimplementasikan dengan menggunakan modul django.contrib.auth, yang mencakup sistem otentikasi bawaan untuk manajemen pengguna dan otentikasi. Ini melibatkan verifikasi kredensial pengguna, seperti username dan password, token, atau metode otentikasi lainnya.

**Otorisasi:** proses pengendalian akses ke sumber daya atau fungsi dalam aplikasi berdasarkan hak akses yang dimiliki oleh pengguna setelah mereka terotentikasi.\
Dalam Django, otorisasi dapat diimplementasikan dengan menggunakan dekorator seperti @login_required untuk memastikan bahwa hanya pengguna yang terotentikasi yang dapat mengakses views tertentu. Ini menentukan apa yang diizinkan atau tidak diizinkan pengguna untuk lakukan setelah mereka masuk.

**Keduanya penting karena:**
- Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi. Tanpa autentikasi yang kuat, aplikasi dapat terbuka untuk penyalahgunaan.
- Otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan peran atau izin yang mereka miliki. Ini melindungi data dan fungsionalitas penting dalam aplikasi dan memastikan bahwa pengguna tidak dapat mengakses atau mengubah data yang tidak seharusnya.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
**Cookies dalam konteks aplikasi web adalah:**\
Potongan data yang disimpan di komputer atau perangkat pengguna saat mereka berinteraksi dengan situs web atau aplikasi web. Cookies digunakan oleh aplikasi web untuk menyimpan informasi tertentu dan mengidentifikasi pengguna saat mereka kembali ke situs atau aplikasi yang sama.

Dalam konteks Django, cookies digunakan untuk mengelola data sesi pengguna. Data sesi adalah cara untuk menyimpan informasi spesifik pengguna selama mereka berinteraksi dengan aplikasi web, bahkan jika mereka belum terdaftar atau terotentikasi. Django menggunakan cookies untuk mengidentifikasi pengguna dan menyimpan data sesi seperti:
- Identifikasi Otentikasi: Untuk mengidentifikasi pengguna yang sudah login.
- Data Sesi: Untuk menyimpan data yang perlu diingat antar permintaan, misalnya, keranjang belanja sementara, preferensi tampilan, atau status login.

Secara bawaan, Django menggunakan session cookies, yang dapat dikonfigurasi dalam berkas konfigurasi settings.py. Beberapa fitur terkait sesi dan cookies dalam Django meliputi:
- SESSION_ENGINE: Pengaturan ini memungkinkan untuk memilih penyimpanan sesi, seperti dalam database atau file.
- SESSION_COOKIE_SECURE: Mengatur apakah cookie sesi hanya boleh disampaikan melalui HTTPS.
- SESSION_COOKIE_HTTPONLY: Mengatur apakah cookie sesi hanya dapat diakses melalui JavaScript.
- SESSION_EXPIRE_AT_BROWSER_CLOSE: Mengatur apakah sesi akan berakhir ketika pengguna menutup browser.
- SESSION_COOKIE_NAME: Nama cookie sesi yang dapat disesuaikan.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat aman secara default jika diimplementasikan dengan baik dan jika praktik keamanan yang disarankan diikuti.

Namun, tetap saja ada beberapa risiko potensial yang harus diwaspadai:
- Keamanan Data: Cookies dapat digunakan untuk menyimpan data sensitif seperti token otentikasi atau ID sesi. Jika cookie ini diretas atau dicuri, maka penggunaan cookies dapat membahayakan keamanan data.
- Cross-Site Request Forgery (CSRF): Serangan CSRF dapat menggunakan cookies untuk mengirim permintaan yang tidak sah atas nama pengguna yang sudah masuk. Untuk melindungi terhadap serangan ini, kita harus memastikan cookie yang digunakan untuk otentikasi diimplementasikan dengan benar.
- Penggunaan Berlebihan: Terlalu banyak cookies dapat memperlambat performa situs web karena setiap permintaan HTTP akan membawa semua cookies yang diperlukan. Ini dapat mengganggu pengalaman pengguna, terutama pada perangkat dengan koneksi internet yang lambat.