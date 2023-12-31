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
Username: catlovers
![cat](https://i.postimg.cc/g0Lb7mRC/Whats-App-Image-2023-09-27-at-10-41-43.jpg)

Username: doglovers
![dog](https://i.postimg.cc/CL9NN0hB/Whats-App-Image-2023-09-27-at-10-46-27.jpg)

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
2. Tidak Cocok untuk Semua Kasus: Form ini mungkin tidak cocok untuk semua aplikasi karena setiap aplikasi memiliki persyaratan pendaftaran yang berbeda. Penggunaan formulir ini secara default mungkin tidak mencakup semua kebutuhan aplikasi.
3. Desain Tampilan Default: Tampilan yang dihasilkan oleh UserCreationForm mungkin perlu disesuaikan dengan desain tampilan spesifik proyek.

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

# TUGAS 5
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
## 1. Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
### Halaman login
![Login](https://i.postimg.cc/W1fhDBc1/Whats-App-Image-2023-10-04-at-08-54-07-1.jpg)

Mengubah code pada berkas `login.html` menjadi:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petkeeper Inventory</title>
    <link rel="stylesheet" href="path/to/bootstrap.min.css"> <!-- Sertakan Bootstrap CSS -->
    <style>
        body {
            background-color: #fce4ec; /* Warna latar belakang halaman (pink muda) */
            color: #6a0572; /* Warna teks (ungu tua) */
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .container {
            max-width: 400px;
        }

        .page-title {
            color: #d81b60; /* Warna judul halaman (pink tua) */
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 2rem;
            white-space: nowrap; /* Memastikan judul tidak terputus */
        }

        .login-container {
            background-color: #ffffff;
            box-shadow: 0px 10px 30px rgba(90, 24, 154, 0.2);
            border-radius: 10px;
            padding: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-control {
            width: calc(100% - 40px); /* Lebar input dikurangi dengan padding horizontal */
            padding: 1rem;
            font-size: 1rem;
            border: 2px solid #d81b60; /* Warna border input (pink tua) */
            border-radius: 25px;
            transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        }

        .form-control:focus {
            border-color: #6a0572; /* Warna border input saat focus (ungu tua) */
            box-shadow: 0 0 0 0.2rem rgba(106, 5, 114, 0.25); /* Efek shadow saat focus */
        }

        .btn-primary {
            background-color: #d81b60; /* Warna latar belakang tombol (pink tua) */
            color: #ffffff;
            border: none;
            border-radius: 25px;
            transition: background-color 0.3s ease;
            font-size: 1rem;
            padding: 1rem 2rem;
        }

        .btn-primary:hover {
            background-color: #6a0572; /* Warna latar belakang tombol saat hover (ungu tua) */
        }

        .error-messages {
            color: #d81b60; /* Warna teks pesan error (pink tua) */
            list-style: none;
            padding: 0;
        }

        .error-messages li {
            margin-bottom: 0.5rem;
        }

        .fun-emoji {
            font-size: 2rem;
            margin-right: 0.5rem;
        }
    </style>
</head>

<body>

    <div class="container my-4">
        <h1 class="text-center mb-4 page-title">
            <span class="fun-emoji">🐾</span>Welcome to the Petkeeper Inventory App! <span class="fun-emoji">🐾</span>
        </h1>
        
        <div class="login-container card">
            <h2 class="text-center mb-4">Login</h2>
            <form method="POST" action="">
                {% csrf_token %}
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" name="username" id="username" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" name="password" id="password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Login</button>
            </form>
    
            {% if messages %}
                <ul class="error-messages mt-4">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
    
            <p class="mt-3">Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
        </div>
    </div>

    <script src="path/to/bootstrap.bundle.min.js"></script> <!-- Sertakan Bootstrap JS (optional) -->
</body>

</html>
```
**Penjelasan alur pada berkas `login.html`**
1. *HTML Structure:*
Halaman dimulai dengan mendeklarasikan tipe dokumen (`<!DOCTYPE html>`) dan mengatur bahasa (Bahasa Inggris) serta menghubungkan file CSS Bootstrap (path/to/bootstrap.min.css).
Struktur halaman terdiri dari `<head>` yang berisi meta tag, judul halaman, dan referensi ke file CSS.
Konten halaman berada dalam `<body>` tag. Dalam `<body>`, ada sebuah `<div>` dengan kelas container yang mengandung elemen-elemen lainnya.

2. *CSS Styling:*
Elemen-elemen halaman, seperti body, container, judul halaman, formulir, dan tombol diberi gaya menggunakan CSS. Warna latar belakang, ukuran teks, efek bayangan, border, dan transisi saat interaksi dengan elemen (seperti hover) telah ditentukan.

3. *Formulir Login:*
Halaman ini adalah formulir login yang meminta pengguna untuk memasukkan username dan password.
Formulir menggunakan metode POST untuk mengirimkan data. Ada dua input: username (`<input type="text">`) dan password (`<input type="password">`), masing-masing dengan label yang sesuai.
CSRF token ({% csrf_token %}) disertakan untuk keamanan formulir.

4. *Error Messages:*
Jika ada pesan kesalahan ({% if messages %}), pesan-pesan itu ditampilkan dalam bentuk daftar (unordered list) dengan kelas error-messages.
Setiap pesan kesalahan ditampilkan sebagai item daftar.

5. *Register Link:*
Terdapat juga tautan untuk mendaftar jika pengguna belum memiliki akun. Tautan ini mengarahkan ke URL yang dihasilkan oleh tag URL Django ({% url 'main:register' %}).

6. *JavaScript:*
File Bootstrap JavaScript bundle (path/to/bootstrap.bundle.min.js) disertakan. Ini penting jika ingin menggunakan komponen JavaScript dari Bootstrap, meskipun dalam halaman ini, tidak ada komponen Bootstrap JavaScript yang digunakan.

7. *Django Template Tags:*
Beberapa tag template Django ({% csrf_token %}, {% if messages %}, {% url 'main:register' %}) digunakan untuk menyertakan CSRF token, menampilkan pesan kesalahan, dan menghasilkan URL untuk tautan mendaftar.

### Halaman register
![Register](https://i.postimg.cc/6qw3JwnY/Whats-App-Image-2023-10-04-at-08-54-07-2.jpg)

Mengubah code pada berkas `register.html` menjadi:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Inventori</title>
    <link rel="stylesheet" href="path/to/bootstrap.min.css"> <!-- Sertakan Bootstrap CSS -->
    <style>
        body {
            background-color: #fce4ec; /* Warna latar belakang halaman (pink muda) */
            color: #6a0572; /* Warna teks (ungu tua) */
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .container {
            max-width: 400px;
        }

        .page-title {
            color: #d81b60; /* Warna judul halaman (pink tua) */
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 2rem;
            white-space: nowrap; /* Memastikan judul tidak terputus */
        }

        .login-container {
            background-color: #ffffff;
            box-shadow: 0px 10px 30px rgba(90, 24, 154, 0.2);
            border-radius: 10px;
            padding: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-control {
            width: calc(100% - 40px); /* Lebar input dikurangi dengan padding horizontal */
            padding: 1rem;
            font-size: 1rem;
            border: 2px solid #d81b60; /* Warna border input (pink tua) */
            border-radius: 25px;
            transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        }

        .form-control:focus {
            border-color: #6a0572; /* Warna border input saat focus (ungu tua) */
            box-shadow: 0 0 0 0.2rem rgba(106, 5, 114, 0.25); /* Efek shadow saat focus */
        }

        .btn-primary {
            background-color: #d81b60; /* Warna latar belakang tombol (pink tua) */
            color: #ffffff;
            border: none;
            border-radius: 25px;
            transition: background-color 0.3s ease;
            font-size: 1rem;
            padding: 1rem 2rem;
        }

        .btn-primary:hover {
            background-color: #6a0572; /* Warna latar belakang tombol saat hover (ungu tua) */
        }

        .fun-emoji {
            font-size: 2rem;
            margin-right: 0.5rem;
        }
    </style>
</head>


<body>
    <div class="container my-4">
        <h1 class="text-center mb-4 page-title">
            <span class="fun-emoji">🌟</span>Create Your Magical Account! <span class="fun-emoji">🌟</span>
        </h1>
    
        <div class="login-container card p-4">
            <h2 class="text-center mb-4">Join the Petkeeper Family!</h2>
            <form method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="{{ form.username.id_for_label }}" class="input-label">Username:</label>
                    {{ form.username }}
                </div>
                <div class="form-group">
                    <label for="{{ form.password1.id_for_label }}" class="input-label">Password:</label>
                    {{ form.password1 }}
                </div>
                <div class="form-group">
                    <label for="{{ form.password2.id_for_label }}" class="input-label">Confirm Password:</label>
                    {{ form.password2 }}
                </div>
                <button type="submit" class="btn btn-primary btn-block mt-3">Join the Magic!</button>
            </form>
    
            {% if messages %}
                <ul class="error-messages mt-4">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
    
            <p class="mt-3 text-center">Already have an account? <a href="{% url 'main:login' %}">Login here</a></p>
        </div>
    </div>
    
    <script src="path/to/bootstrap.bundle.min.js"></script> <!-- Sertakan Bootstrap JS (optional) -->
</body>

</html>
```
**Penjelasan alur pada berkas `register.html`**
1. *HTML Structure:*
Halaman dimulai dengan mendeklarasikan tipe dokumen (`<!DOCTYPE html>`) dan mengatur bahasa (Bahasa Inggris) serta menghubungkan file CSS Bootstrap (path/to/bootstrap.min.css).
Struktur halaman terdiri dari `<head>` yang berisi meta tag, judul halaman, dan referensi ke file CSS.
Konten halaman berada dalam `<body>` tag. Dalam `<body>`, ada sebuah `<div>` dengan kelas container yang mengandung elemen-elemen formulir dan pesan error.

2. *CSS Styling:*
Elemen-elemen halaman, seperti body, container, judul halaman, formulir, dan tombol diberi gaya menggunakan CSS. Warna latar belakang, ukuran teks, efek bayangan, border, dan transisi saat interaksi dengan elemen (seperti hover) telah ditentukan.

3. *Formulir Pendaftaran Pengguna Baru:*
Halaman ini adalah formulir pendaftaran pengguna baru. Formulir ini memiliki input untuk username, password, dan konfirmasi password.
Setiap input memiliki label dan menggunakan Django template tags ({{ form.username }}, {{ form.password1 }}, {{ form.password2 }}) untuk menghubungkan input dengan formulir Django terkait.
CSRF token ({% csrf_token %}) disertakan untuk keamanan formulir.
Jika ada pesan kesalahan ({% if messages %}), pesan-pesan itu ditampilkan dalam bentuk daftar (unordered list) dengan kelas error-messages. Setiap pesan kesalahan ditampilkan sebagai item daftar.

4. *JavaScript:*
File Bootstrap JavaScript bundle (path/to/bootstrap.bundle.min.js) disertakan. Ini penting jika ingin menggunakan komponen JavaScript dari Bootstrap, meskipun dalam halaman ini, tidak ada komponen Bootstrap JavaScript yang digunakan.

5. *Django Template Tags:*
Beberapa tag template Django ({% csrf_token %}, {% if messages %}) digunakan untuk menyertakan CSRF token dan menampilkan pesan kesalahan (jika ada).


### Halaman tambah inventori
![Create_product](https://i.postimg.cc/BQS6mSqv/Whats-App-Image-2023-10-04-at-08-54-07-3.jpg)

Mengubah code pada berkas `create_product.html` menjadi:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petkeeper Inventory</title>
    <link rel="stylesheet" href="path/to/bootstrap.min.css"> <!-- Sertakan Bootstrap CSS -->
    <style>
        body {
            background-color: #fce4ec; /* Warna latar belakang halaman (pink muda) */
            color: #6a0572; /* Warna teks (ungu tua) */
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .container {
            max-width: 400px;
        }

        .page-title {
            color: #d81b60; /* Warna judul halaman (pink tua) */
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 2rem;
            white-space: nowrap; /* Memastikan judul tidak terputus */
        }

        .product-form-container {
            background-color: #ffffff;
            box-shadow: 0px 10px 30px rgba(90, 24, 154, 0.2);
            border-radius: 10px;
            padding: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-control {
            width: calc(100% - 40px); /* Lebar input dikurangi dengan padding horizontal */
            padding: 1rem;
            font-size: 1rem;
            border: 2px solid #d81b60; /* Warna border input (pink tua) */
            border-radius: 25px;
            transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        }

        .form-control:focus {
            border-color: #6a0572; /* Warna border input saat focus (ungu tua) */
            box-shadow: 0 0 0 0.2rem rgba(106, 5, 114, 0.25); /* Efek shadow saat focus */
        }

        .btn-primary {
            background-color: #d81b60; /* Warna latar belakang tombol (pink tua) */
            color: #ffffff;
            border: none;
            border-radius: 25px;
            transition: background-color 0.3s ease;
            font-size: 1rem;
            padding: 1rem 2rem;
        }

        .btn-primary:hover {
            background-color: #6a0572; /* Warna latar belakang tombol saat hover (ungu tua) */
        }

        .error-messages {
            color: #d81b60; /* Warna teks pesan error (pink tua) */
            list-style: none;
            padding: 0;
        }

        .error-messages li {
            margin-bottom: 0.5rem;
        }

        .fun-emoji {
            font-size: 2rem;
            margin-right: 0.5rem;
        }
    </style>
</head>

<body>

    <div class="container my-4">
        <h1 class="text-center mb-4 page-title">
            <span class="fun-emoji">🌈</span>Welcome to the Petkeeper Inventory App!<span class="fun-emoji">🐾</span>
        </h1>
        
        <div class="product-form-container card">
            <h2 class="text-center mb-4">Add New Product</h2>
            <form method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="{{ form.name.id_for_label }}" class="form-label">Product Name:</label>
                    {{ form.name }}
                </div>
                <div class="form-group">
                    <label for="{{ form.description.id_for_label }}" class="form-label">Description:</label>
                    {{ form.description }}
                </div>
                <div class="form-group">
                    <label for="{{ form.price.id_for_label }}" class="form-label">Price:</label>
                    {{ form.price }}
                </div>
                <div class="form-group">
                    <label for="{{ form.amount.id_for_label }}" class="form-label">Amount:</label>
                    {{ form.amount }}
                </div>
                <button type="submit" class="btn btn-primary btn-block">Add Product</button>
            </form>

            {% if messages %}
                <ul class="error-messages mt-4">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        </div>
    </div>

    <script src="path/to/bootstrap.bundle.min.js"></script> <!-- Sertakan Bootstrap JS (optional) -->
</body>

</html>
```
**Penjelasan alur pada berkas `create_product.html`**
1. *HTML Structure:*
Halaman dimulai dengan mendeklarasikan tipe dokumen (`<!DOCTYPE html>`) dan mengatur bahasa (Bahasa Inggris) serta menghubungkan file CSS Bootstrap (path/to/bootstrap.min.css).
Struktur halaman terdiri dari `<head>` yang berisi meta tag, judul halaman, dan referensi ke file CSS.
Konten halaman berada dalam `<body>` tag. Dalam `<body>`, ada sebuah `<div>` dengan kelas container yang mengandung elemen-elemen formulir dan pesan error.

2. *CSS Styling:*
Elemen-elemen halaman, seperti body, container, judul halaman, formulir, dan tombol diberi gaya menggunakan CSS. Warna latar belakang, ukuran teks, efek bayangan, border, dan transisi saat interaksi dengan elemen (seperti hover) telah ditentukan.

3. *Formulir Penambahan Produk:*
Halaman ini adalah formulir untuk menambahkan produk baru. Formulir ini memiliki input untuk nama produk, deskripsi produk, harga produk, dan jumlah produk yang ingin ditambahkan.
Setiap input memiliki label dan menggunakan Django template tags ({{ form.name }}, {{ form.description }}, {{ form.price }}, {{ form.amount }}) untuk menghubungkan input dengan formulir Django terkait.
CSRF token ({% csrf_token %}) disertakan untuk keamanan formulir.
Jika ada pesan kesalahan ({% if messages %}), pesan-pesan itu ditampilkan dalam bentuk daftar (unordered list) dengan kelas error-messages. Setiap pesan kesalahan ditampilkan sebagai item daftar.

4. *JavaScript:*
File Bootstrap JavaScript bundle (path/to/bootstrap.bundle.min.js) disertakan. Ini penting jika ingin menggunakan komponen JavaScript dari Bootstrap, meskipun dalam halaman ini, tidak ada komponen Bootstrap JavaScript yang digunakan.

5. *Django Template Tags:*
Beberapa tag template Django ({% csrf_token %}, {% if messages %}) digunakan untuk menyertakan CSRF token dan menampilkan pesan kesalahan (jika ada).

## 2. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
### Halaman daftar inventori
![Main](https://i.postimg.cc/25WbsCVB/Whats-App-Image-2023-10-04-at-09-44-35.jpg)

Mengubah code pada berkas `main.html` menjadi:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Inventori</title>
    <link rel="stylesheet" href="path/to/bootstrap.min.css"> <!-- Sertakan Bootstrap CSS -->
    <style>
        body {
            background-color: #f4a29e; /* Warna latar belakang halaman (pink coral pastel) */
            color: #b19cd9; /* Warna teks (ungu pastel) */
            font-family: 'Comic Sans MS', cursive, sans-serif; /* Ganti dengan font pilihan */
        }

        .container {
            max-width: 960px; /* Lebar maksimum kontainer */
        }

        .card {
            background-color: #ffffff; /* Warna latar belakang kartu (putih) */
            color: #5a189a; /* Warna teks pada kartu */
            border: none; /* Hapus border kartu jika ada */
            box-shadow: 0px 10px 30px rgba(90, 24, 154, 0.2); /* Efek bayangan pada kartu */
            border-radius: 10px; /* Sudut melengkung kartu */
            transition: all 0.3s ease; /* Efek transisi pada kartu */
            margin: 20px 10px; /* Ruang dari tepi halaman */
            width: 45%; /* Lebar kartu 45% dari lebar parent */
            float: left; /* Floating kartu ke kiri */
            height: 100%; /* Tentukan tinggi kartu */
            min-height: 300px; /* Tentukan tinggi minimum kartu */
        }

        .card:hover {
            transform: translateY(-10px); /* Mengangkat kartu saat dihover */
            box-shadow: 0px 20px 40px rgba(90, 24, 154, 0.3); /* Bayangan yang lebih tebal saat dihover */
        }

        .navbar {
            background-color: #f4a29e; /* Warna latar belakang navbar (pink coral pastel) */
            color: #b19cd9; /* Warna teks navbar */
        }

        .navbar-nav li {
            list-style: none; /* Menghilangkan poin bulatan dari elemen li */
        }

        .navbar-nav .nav-link {
            display: flex;
            align-items: center;
            margin-left: -40px;
        }

        .navbar-brand {
            font-weight: bold; /* Teks brand navbar lebih tebal */
        }

        h1, h2, h3, h4, h5, h6 {
            color: #d0005e; /* Warna teks judul halaman (pink tua) */
        }

        .btn-primary {
            background-color: #ffacda; /* Warna latar belakang tombol primary (pink pastel) */
            color: #6a0572; /* Warna teks tombol (ungu tua) */
            border: none; /* Hapus border tombol */
            border-radius: 25px; /* Sudut melengkung tombol */
            transition: background-color 0.3s ease; /* Transisi perubahan warna saat hover */
            font-size: 0.9em; /* Ukuran teks tombol */
            margin: 5px; /* Ruang dari tepi tombol */
            padding: 8px 16px; /* Padding tombol */
            border: 2px solid #5a189a; /* Border tombol */
            position: relative; /* Relatif terhadap posisi normal */
            overflow: hidden; /* Sembunyikan konten yang melampaui batas tombol */
            width: fit-content; /* Menyesuaikan lebar dengan isi tombol */
        }

        .btn-primary:before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0;
            height: 0;
            border: 2px solid #ff6b98;
            border-radius: 50%;
            opacity: 0;
            transition: width 0.3s ease, height 0.3s ease, opacity 0.3s ease;
        }

        .btn-primary:hover:before {
            width: 200px;
            height: 200px;
            opacity: 1;
        }

        .btn-primary:hover {
            background-color: #ff6b98; /* Warna latar belakang tombol primary saat dihover (pink pastel lebih terang) */
            color: #ffffff; /* Warna teks tombol saat dihover (putih) */
        }

        .card-title {
            color: #ff6b98; /* Warna teks judul halaman (pink pastel) */
            font-size: 1.5em; /* Ukuran teks judul kartu */
            text-transform: uppercase; /* Ubah teks judul menjadi huruf kapital */
            margin-bottom: 0.2em; /* Ruang bawah judul kartu */
        }

        .card-body {
            border-top: 2px solid #ff6b98; /* Garis atas pada bagian dalam kartu (pink pastel) */
            padding: 1em; /* Ruang di dalam kartu */
        }

        .card-table th, .card-table td {
            color: #ffacda; /* Warna teks header tabel (pink pastel) */
        }

        .card-table th {
            width: 30%; /* Lebar kolom header tabel */
            color: #ffacda; /* Warna teks header tabel (pink pastel) */
            text-align: left; /* Teks dalam header tabel berada di sebelah kiri */
        }

        .card-table td {
            color: #5a189a; /* Warna teks sel tabel */
        }

        .info-table {
            font-family: 'Arial', sans-serif; /* Menggunakan font Arial untuk tabel */
            margin-top: 10px; /* Ruang atas dari tabel */
            border-collapse: collapse; /* Menggabungkan garis batas antar sel tabel */
            width: 50%; /* Lebar tabel 100% dari lebar parent */
            background-color: #ffacda; /* Warna latar belakang tabel (pink pastel) */
            border-radius: 20px; /* Sudut melengkung tabel */
        }

        .info-table th, .info-table td {
            border: 2px solid #e03859; /* Garis batas sel tabel */
            padding: 10px; /* Ruang dalam sel tabel */
            text-align: left; /* Teks dalam sel tabel berada di sebelah kiri */
        }

        .info-table th {
            background-color: #e03859; /* Warna latar belakang header tabel (pink tua) */
            font-weight: bold; /* Teks header tabel lebih tebal */
            color: #ffffff; /* Warna teks header tabel (putih) */
        }

        .info-table td.description {
            font-style: italic; /* Teks deskripsi tabel menjadi miring */
            color: #d0005e; /* Warna teks deskripsi tabel (pink tua) */
        }

        .info-table tr:nth-child(even) {
            background-color: #ffedf2; /* Warna latar belakang setiap baris genap (pink muda) */
        }

        .info-table tr:nth-child(odd) {
            background-color: #ffdde1; /* Warna latar belakang setiap baris ganjil (pink pastel) */
        }

    </style>
</head>

<body>

    <div class="container my-4">
        <h1 class="text-center mb-4 page-title">Welcome to the Petkeeper Inventory App!🐾</h1>

        <table class="info-table">
            <tr>
                <th>Nama</th>
                <td class="description">Joy Debora Sitorus</td>
            </tr>
            <tr>
                <th>NPM</th>
                <td class="description">2206082991</td>
            </tr>
            <tr>
                <th>Class</th>
                <td class="description">PBP D</td>
            </tr>
        </table>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'main:create_product' %}">
                        <div class="btn-primary">Add New Super Cute Product💖</div>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'main:logout' %}">
                        <div class="btn-primary">Logout and Have a Magical Day With Your Pet🌈</div>
                    </a>
                </li>
            </ul>
        </div>

        <div class="row">
            {% for product in products %}
                <div class="col-md-6 mb-3">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <table class="card-table">
                                <tr>
                                    <th>Quantity</th>
                                    <td>{{ product.amount }}</td>
                                </tr>
                                <tr>
                                    <th>Description</th>
                                    <td>{{ product.description }}</td>
                                </tr>
                                <tr>
                                    <th>Category</th>
                                    <td>{{ product.category }}</td>
                                </tr>
                                <tr>
                                    <th>Price</th>
                                    <td>{{ product.price }}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>

    <script src="path/to/bootstrap.bundle.min.js"></script> <!-- Sertakan Bootstrap JS (optional) -->
</body>

</html>
```
**Penjelasan alur pada berkas `main.html`**
1. *HTML Structure:*
Halaman dimulai dengan mendeklarasikan tipe dokumen (`<!DOCTYPE html>`) dan mengatur bahasa (Bahasa Inggris) serta menghubungkan file CSS Bootstrap (path/to/bootstrap.min.css).
Struktur halaman terdiri dari `<head>` yang berisi meta tag, judul halaman, dan referensi ke file CSS.
Konten halaman berada dalam `<body>` tag. Dalam `<body>`, ada elemen-elemen seperti judul halaman, informasi pengguna (Nama, NPM, Kelas), tombol untuk menambah produk baru, tombol logout, dan daftar produk yang ditampilkan dalam bentuk kartu (`<div class="card">`).

2. *CSS Styling:*
Elemen-elemen halaman, seperti body, container, kartu, navbar, tombol, judul kartu, dan tabel, diberi gaya menggunakan CSS. Warna latar belakang, ukuran teks, efek bayangan, border, dan transisi saat interaksi dengan elemen telah ditentukan.

3. *User Information Table:*
Informasi pengguna (Nama, NPM, Kelas) ditampilkan dalam bentuk tabel (`<table class="info-table">`). Setiap baris tabel memiliki kolom judul (Nama, NPM, Kelas) dan deskripsi yang berisi informasi pengguna.

4. *Navbar and Buttons:*
Terdapat navbar dengan dua tombol. Tombol pertama mengarah ke halaman penambahan produk baru ({% url 'main:create_product' %}), dan tombol kedua mengarah ke fungsi logout ({% url 'main:logout' %}). Tombol-tombol ini dibuat dengan warna latar belakang dan efek hover yang berbeda untuk menarik perhatian pengguna.

5. *Product Cards:*
Produk-produk yang ada ditampilkan dalam bentuk kartu. Setiap kartu memiliki judul produk, jumlah produk, deskripsi, kategori, dan harga. Informasi ini diambil dari model produk dalam aplikasi Django.
Kartu-kartu ini dibuat dengan efek bayangan dan sedikit melayang saat dihover, memberikan sentuhan interaktif kepada pengguna.
Produk-produk ini diambil dari variabel products yang kemungkinan besar berasal dari hasil query ke database pada sisi server.

6. *JavaScript:*
File Bootstrap JavaScript bundle (path/to/bootstrap.bundle.min.js) disertakan. Ini penting jika kita ingin menggunakan komponen JavaScript dari Bootstrap, meskipun dalam halaman ini, tidak ada komponen Bootstrap JavaScript yang digunakan.

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
CSS selectors adalah pola atau pola pencocokan yang digunakan untuk memilih dan menggaya elemen HTML pada halaman web. Setiap aturan CSS membutuhkan sebuah selector untuk menentukan elemen mana yang akan diberi gaya. CSS selector dapat berupa nama elemen, class, ID, pseudo-class, pseudo-element, atribut, atau kombinasi dari beberapa tipe ini.

Berikut adalah beberapa jenis CSS selectors:
- Element Selector: Memilih elemen berdasarkan nama elemennya. Contoh: `p { color: blue; }`
- Class Selector: Memilih elemen berdasarkan class atributnya. Contoh: `.my-class { font-weight: bold; }`
- ID Selector: Memilih elemen berdasarkan ID atributnya. Contoh: `#unique-id { background-color: yellow; }`

**Element Selector:**
Element selector merupakan salah satu dari 3 bagian CSS selectors. Element sector memungkinkan kita menerapkan gaya pada semua elemen dengan jenis yang sama. Ini sangat berguna ketika kita ingin menerapkan gaya umum ke beberapa elemen sekaligus tanpa menambahkan kelas atau ID ke masing-masing elemen tersebut.

1. Element selector memungkinkan untuk dengan jelas dan pasti menggaya semua elemen dengan nama tertentu pada halaman. Ini berguna saat ingin mengaplikasikan gaya yang sama pada semua elemen dengan nama tersebut, tanpa harus memberikan class atau ID khusus pada setiap elemen tersebut.\
*Kapan Menggunakannya?*\
Gunakan element selector ketika ingin menggaya semua elemen dengan nama elemen tertentu, seperti `<p>`, `<h1>`, `<ul>`, dan lainnya.
Berguna saat kita ingin mengaplikasikan gaya global yang berlaku untuk semua elemen dengan nama elemen tersebut.

2. Penggunaan element selector bisa lebih efisien dalam hal kinerja dibandingkan dengan class selector atau ID selector karena browser lebih cepat dalam menerapkan gaya ke elemen berdasarkan nama elemen. Ini penting saat kita ingin menggaya banyak elemen pada halaman, seperti paragraf, judul, atau daftar.\
*Kapan Menggunakannya?*\
Ketika ingin mempengaruhi banyak elemen dengan nama elemen yang sama, gunakan element selector untuk meminimalkan beban kinerja browser.

## Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 adalah versi terbaru dari bahasa markup HTML (HyperText Markup Language) yang digunakan untuk membuat dan merancang konten web. Berikut adalah beberapa tag HTML5 yang penting dan umum digunakan:

1. `<!DOCTYPE html>`: Mendefinisikan jenis dokumen dan versi HTML yang digunakan (HTML5).
2. `<html>`: Menandakan awal dan akhir dari dokumen HTML.
3. `<head>`: Mengandung informasi meta tentang dokumen, termasuk judul halaman, link ke stylesheet, skrip, dan elemen-elemen lainnya yang tidak ditampilkan secara langsung pada halaman web.
4. `<title>`: Mendefinisikan judul dokumen HTML, yang ditampilkan pada bilah judul atau tab browser.
5. `<meta>`: Menyediakan informasi meta tentang dokumen, seperti karakter encoding, deskripsi, dan kata kunci untuk mesin pencari.
6. `<style>`: Mengandung aturan gaya CSS yang diterapkan pada elemen-elemen dalam dokumen HTML.
7. `<body>`: Berisi semua konten yang ditampilkan pada halaman web, termasuk teks, gambar, tautan, elemen formulir, dll.
8. `<h1>, <h2>, <h3>, <h4>, <h5>, <h6>`: Menandai judul berjenjang (heading) pada halaman web, dengan `<h1>` sebagai judul utama dan `<h6>` sebagai judul terkecil.
9. `<p>`: Mendefinisikan paragraf teks.
10. `<a>`: Membuat tautan (hipertaut) ke halaman web lain atau ke halaman dalam situs yang sama.
11. `<img>`: Menyisipkan gambar ke dalam halaman web.
12. `<ul>, <ol>, <li>`: Mengatur daftar tidak berurutan (unordered list) dan daftar berurutan (ordered list) serta item dalam daftar.
13. `<div>`: Menandai blok elemen yang dapat digunakan untuk mengelompokkan elemen-elemen lainnya dan memungkinkan penerapan gaya atau perilaku tertentu.
14. `<form>`: Membuat formulir interaktif yang dapat digunakan untuk mengumpulkan data dari pengguna, dengan elemen-elemen seperti input, textarea, dan tombol submit.
15. `<input>`: Menyediakan berbagai jenis elemen input, seperti teks, sandi, checkbox, radio button, dll.
16. `<button>`: Membuat tombol pada formulir, yang dapat digunakan untuk mengirimkan formulir atau menjalankan skrip JavaScript tertentu saat diklik.
17. `<header>, <footer>, <section>, <article>, <aside>` Elemen-elemen ini digunakan untuk memberi struktur lebih spesifik pada halaman web, membantu mesin pencari dan pembaca layar memahami konten dengan lebih baik.

## Jelaskan perbedaan antara margin dan padding.
Margin dan Padding adalah dua properti dalam CSS yang digunakan untuk mengatur ruang di sekitar dan di dalam elemen HTML. 
1. **Margin:**
Margin adalah ruang di luar batas elemen. Margin mengontrol jarak antara batas elemen dan elemen-elemen lain di sekitarnya. Elemen-elemen yang berdekatan dengan elemen yang memiliki margin akan menghormati ruang margin tersebut. Margin bersifat transparan, yang berarti latar belakang elemen di belakangnya akan terlihat melalui margin.
2. **Padding:**
Padding adalah ruang di dalam batas elemen. Padding mengontrol jarak antara batas elemen dan kontennya. Dalam hal ini, "konten" merujuk pada teks, gambar, atau elemen lain di dalam elemen yang bersangkutan. Padding tidak bersifat transparan; jika kita memberikan latar belakang pada elemen, latar belakang tersebut akan mencakup area padding.

Perbedaan Utama:
- Area yang Dipengaruhi: Margin mempengaruhi ruang di luar elemen, sementara padding mempengaruhi ruang di dalam elemen.
- Transparansi: Margin bersifat transparan, sementara padding tidak. Artinya, latar belakang elemen di belakang margin akan terlihat melalui margin, tetapi tidak melalui padding.
- Interaksi dengan Elemen Lain: Margin mempengaruhi jarak antara elemen dengan elemen-elemen lain di sekitarnya. Padding, di sisi lain, mempengaruhi jarak antara konten elemen dan batasnya sendiri.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS dan Bootstrap adalah dua framework CSS yang populer digunakan dalam pengembangan web. Mereka memiliki pendekatan dan filosofi yang berbeda, dan pilihan antara keduanya tergantung pada kebutuhan proyek dan preferensi pengembang. Berikut adalah perbedaan utama antara keduanya dan kapan sebaiknya kita menggunakan salah satu daripadanya:

**Tailwind CSS:**
1. Utility-First Approach: Tailwind CSS menggunakan pendekatan "utility-first", yang berarti membangun tampilan dengan menggabungkan berbagai kelas ke dalam elemen HTML. Ini memberikan tingkat fleksibilitas yang tinggi dan memungkinkan pengembang untuk membuat tampilan yang sangat kustom sesuai kebutuhan.
2. Konfigurasi yang Kuat: Tailwind CSS memungkinkan kita mengkonfigurasi setiap aspek gaya dalam proyek, termasuk warna, jenis font, margin, padding, dan lain-lain. Ini membuatnya sangat dapat disesuaikan.
3. File CSS yang Kecil: Tailwind CSS menghasilkan file CSS yang relatif kecil karena hanya menghasilkan CSS yang benar-benar digunakan dalam proyek .
4. Tidak Ada Gaya Bawaan: Tailwind CSS datang dengan sedikit atau tanpa gaya bawaan, yang berarti kita perlu merancang tampilan dari awal atau membangunnya dengan komponen yang tersedia dari pihak ketiga.

**Bootstrap:**
1. Component-Based: Bootstrap adalah framework CSS yang berbasis komponen, yang berarti kita dapat dengan cepat membangun tampilan menggunakan komponen yang telah tersedia. Ini mempercepat pengembangan.
2. Desain Responsif: Bootstrap menyertakan desain responsif secara bawaan, sehingga tampilan aplikasi akan baik di perangkat desktop maupun mobile tanpa banyak kerumitan.
3. Gaya Bawaan: Bootstrap memiliki gaya bawaan yang memberikan tampilan dasar yang baik. Kita dapat menyesuaikannya sesuai kebutuhan, tetapi jika ingin tampilan yang benar-benar unik, kita mungkin perlu menulis lebih banyak kode CSS kustom.
4. Mudah Digunakan: Bootstrap adalah pilihan yang baik untuk pengembang yang ingin cepat membangun tampilan yang baik dengan komponen-komponen yang sudah ada.

*Kapan Menggunakan Tailwind CSS:*
- Tailwind CSS cocok digunakan ketika kita ingin tingkat fleksibilitas tinggi dalam merancang tampilan web aplikasi.
- Ini berguna jika ingin menghindari gaya bawaan dan memiliki kendali penuh atas tampilan aplikasi.
- Tailwind cocok untuk pengembang yang sudah terbiasa dengan pendekatan "utility-first" dalam pengembangan tampilan.

*Kapan Menggunakan Bootstrap:*
- Bootstrap sangat berguna ketika ingin membangun tampilan dengan cepat menggunakan komponen yang telah ada.
- Ini cocok untuk proyek yang memerlukan responsivitas dan desain yang dapat diandalkan di berbagai perangkat.
- Bootstrap adalah pilihan yang baik jika ingin menghemat waktu dalam pengembangan.

# TUGAS 6
**Nama: Joy Debora Sitorus**\
**NPM: 2206082991**\
**Kelas: PBP D**

# CHECKLIST TUGAS
![AppAjax](https://i.postimg.cc/X7LBCqkC/Whats-App-Image-2023-10-13-at-09-12-09-1.jpg)
\
\
![AppAjax1](https://i.postimg.cc/VNxJ8Cm3/Whats-App-Image-2023-10-13-at-09-12-35-1.jpg)

## AJAX GET
## 1. Ubahlah kode cards data item agar dapat mendukung AJAX GET dan Lakukan pengambilan item menggunakan AJAX GET.
### Membuat Modal Sebagai Form untuk Menambahkan Produk
Pada berkas `main.html` di folder templates, subdirektori main, menambahkan class modal sebagai berikut:
```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="category" class="col-form-label">Category:</label>
                        <input type="text" class="form-control" id="category" name="category"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="addProduct" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>
```
**Penjelasan alur:**
1. *Pemanggilan Modal:*
Modal ditentukan dalam HTML dengan ID exampleModal. Saat sebuah elemen, seperti tombol atau link, mengarahkan untuk membuka modal, atribut data-bs-toggle dan data-bs-target digunakan untuk mengidentifikasi modal yang akan muncul. Ketika elemen ini ditekan atau diklik, modal muncul di atas halaman.

2. *Isi Modal:*
Di dalam modal, terdapat elemen-elemen seperti judul `<h1>`, formulir `<form>`, dan tombol-tombol `<button>` untuk mengelola operasi-operasi yang ingin dilakukan pengguna.

3. *Formulir dan Pengiriman Data:*
Pengguna memasukkan data produk seperti nama, jumlah, deskripsi, kategori, dan harga melalui input dan area teks. Formulir memilik atribut onsubmit="return false;" untuk mencegah pengiriman formulir secara tradisional. Ini menghentikan pengiriman formulir bawaan browser dan memungkinkan kita menangani pengiriman data dengan JavaScript.

4. *Penanganan Data dengan JavaScript:*
Ketika pengguna mengklik tombol "Add Product," fungsi JavaScript (addProduct()) akan dipanggil. Dalam fungsi addProduct(), data dari formulir diambil menggunakan JavaScript (menggunakan document.getElementById atau metode serupa) dan dapat diteruskan ke server melalui permintaan AJAX (Fetch API, XMLHttpRequest, dll.).

5. Penutup Modal:
Modal dapat ditutup dengan beberapa cara: mengklik tombol "Close" di sudut kanan atas modal atau dengan menggunakan metode JavaScript. Dalam contoh ini, tombol "Close" diimplementasikan dengan atribut data-bs-dismiss="modal" pada elemen button.


## AJAX POST
## 2. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.
```
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
```
    
## 3. Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
### Membuat Fungsi untuk Menambahkan Produk dengan AJAX
 
```
from django.views.decorators.csrf import csrf_exempt
```

```
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))
```

```
@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        price = request.POST.get("price")
        user = request.user

        new_product = Product(name=name, amount=amount, description=description, category=category, price=price, user=user)
        new_product.save()

        return HttpResponse("CREATED", status=201)

    return HttpResponseNotFound()
```

## 4. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
### Menambahkan routing untuk fungsi yang telah dibuat
```
from main.views import get_product_json, create_ajax
```

```
path('get-product/', get_product_json, name='get_product_json'),
path('create-ajax/', create_ajax, name='create_ajax'),
```

## 5.  Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
### Menambahkan routing untuk fungsi yang telah dibuat
```
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}")
            .then(response => response.json())
    }
</script>
```

```
<script>
    ...
    function addProduct() {
        fetch("{% url 'main:create_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("addProduct").onclick = addProduct
</script>
```

## 6.  Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
```
<script>
    ...
    async function refreshProducts() {
        document.getElementById("products").innerHTML = ""
        const products = await getProducts()
        const length = Object.keys(products).length
        let html = '<div class="container">'
        html += '<p class="lead text-muted">Total Item: ' + length + '</p>'
        html += '<div class="row row-cols-3">';
        products.forEach((item) => {
            html += '<div class="col-md-6 col-lg-4 mb-5">'
            html += '<div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">'
            html += '<div class="card-body">'
            html += '<h5 class="card-title" style="color: #B0578D">' + item.fields.name + '</h5>'
            html += '<p class="card-text">Amount: ' + item.fields.amount + '</p>'
            html += '<p class="card-text">Description: ' + item.fields.description + '</p>'
            html += '<p class="card-text">Category: ' + item.fields.category + '</p>'
            html += '<p class="card-text">Price: ' + item.fields.price + '</p>'
            html += '<a href="/item/add/' + item.pk + '" class="btn btn-outline-dark mx-2">Add</a>'
            html += '</div>'
        })
        html += '</div>'
        html += '</div>'
        document.getElementById("products").innerHTML = html
    }
    refreshProducts();
</script>
```
**Penjelasan alur:**
1. *Penetapan Produk Element Kosong:*
Pertama-tama, fungsi ini mengosongkan elemen dengan ID products. Dalam hal ini, isi dari elemen ini akan digantikan dengan produk-produk yang akan diambil dari server.

2. *Permintaan Produk Melalui getProducts:*
Selanjutnya, fungsi menunggu permintaan data produk menggunakan fungsi getProducts. Dengan menggunakan kata kunci await, fungsi refreshProducts berhenti mengeksekusi sampai permintaan data produk selesai dan hasilnya tersedia.

3. *Pembuatan HTML untuk Produk:*
Setelah data produk diterima, fungsi ini membuat HTML untuk menampilkan produk. Ini melibatkan membuat tag HTML yang sesuai dengan data produk yang diterima. Setiap produk ditampilkan dalam sebuah kartu `<div class="card">` dengan informasi seperti nama, jumlah, deskripsi, kategori, dan harga.

4. *Penyisipan HTML Produk ke dalam Halaman:*
Setelah HTML produk dibuat, variabel html yang berisi HTML produk disisipkan ke dalam elemen dengan ID products. Dengan ini, data produk akan ditampilkan secara dinamis pada halaman web tanpa memuat ulang seluruh halaman.

5. Pemanggilan Fungsi refreshProducts:*
Terakhir, fungsi refreshProducts dipanggil pada akhir kode, yang berarti setiap kali halaman dimuat atau fungsi ini dipanggil secara manual, data produk akan diambil dan ditampilkan ulang sesuai dengan alur di atas.

## 7. Melakukan perintah collectstatic
Jalankan perintah `python manage.py collectstatic`

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
1. **Synchronous Programming:**
- Dalam synchronous programming, kode dieksekusi secara berurutan dari atas ke bawah. Setiap operasi I/O atau pemrosesan yang memerlukan waktu akan menghentikan eksekusi kode sampai operasi tersebut selesai.
- Pemrograman sinkronus sederhana dan mudah dipahami, tetapi dapat menghambat aplikasi dalam situasi di mana ada banyak operasi I/O yang perlu dijalankan secara bersamaan.

2. **Asynchronous Programming:**
- Dalam asynchronous programming, kita dapat menjalankan beberapa tugas atau operasi I/O secara bersamaan tanpa harus menunggu satu tugas selesai sebelum menjalankan yang lain.
- Pemrograman asinkronus memungkinkan aplikasi untuk tetap responsif dan menjawab permintaan tanpa penundaan yang berlebihan, terutama dalam situasi dengan banyak operasi I/O seperti server web yang harus menangani banyak permintaan sekaligus.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
**Paradigma Event-Driven Programming** adalah pendekatan pemrograman di mana logika aplikasi merespons peristiwa atau tindakan yang terjadi pada program. Peristiwa ini dapat melibatkan tindakan pengguna seperti mengklik tombol, memasukkan teks, atau menggerakkan mouse. Paradigma ini memungkinkan program untuk berinteraksi secara dinamis dengan pengguna dan lingkungannya, merespons perubahan tanpa perlu memeriksa kondisi secara berulang atau melakukan polling terus-menerus.

**Contoh Penerapan Paradigma Event-Driven**
1. Ketika Tombol "Add Product by AJAX" Diklik
```
document.getElementById("addProduct").onclick = addProduct;
```
Saat tombol dengan ID "addProduct" diklik, event click dipicu. Fungsi `addProduct()` akan dieksekusi ketika event ini terjadi. Di dalamnya, terjadi penggunaan AJAX untuk mengirim data formulir ke server.

2. Ketika Data Produk Diterima dari Server
```
function getProducts() {
    return fetch("{% url 'main:get_product_json' %}")
        .then(response => response.json())
        .then(products => {
            // Logika untuk memproses produk yang diterima dari server
        });
}
```
Dalam fungsi `getProducts()`, event-driven programming terlihat melalui penggunaan fetch API. Saat permintaan AJAX selesai dan data produk diterima dari server, event `then()` dipicu, memungkinkan untuk merespons data yang diterima dari server.

## Jelaskan penerapan asynchronous programming pada AJAX.
**Asynchronous programming** adalah paradigma pemrograman di mana operasi-operasi yang memerlukan waktu, seperti permintaan jaringan (seperti AJAX), file I/O, atau operasi basis data, dapat dieksekusi secara non-blokcing.\
Dalam konteks AJAX, asynchronous programming memungkinkan kita membuat permintaan ke server tanpa menghentikan eksekusi program yang lain. Ini berarti bahwa sementara permintaan ke server sedang dalam proses, aplikasi tetap responsif dan dapat menjalankan operasi-operasi lain.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API dan jQuery adalah dua pendekatan yang berbeda untuk melakukan permintaan AJAX dalam pengembangan web. Perbandingan keduanya:
1. **Fetch API:**
- Native JavaScript: Fetch API adalah bagian dari JavaScript modern dan merupakan bagian dari standar web. Ini berarti kita tidak perlu mengunduh atau menginstal perpustakaan tambahan. Ini adalah solusi native yang berfungsi baik pada berbagai platform dan peramban.
- Promise-Based: Fetch API menggunakan promise, yang memungkinkan menulis kode asynchronous yang bersih dan mudah dimengerti dengan async/await. Ini mempermudah penanganan permintaan asynchronous dan menghindari callback hell.
- Lebih Ringan: Fetch API lebih ringan daripada jQuery karena fokusnya hanya pada fitur permintaan HTTP, tanpa menyertakan banyak fitur tambahan yang mungkin tidak digunakan.

2. **jQuery:**
- Kompatibilitas Lintas Peramban: jQuery dirancang untuk mengatasi perbedaan dalam perilaku peramban. Ini dapat membuatnya berguna jika kita harus mendukung peramban lama yang mungkin tidak mendukung fitur modern seperti Fetch API.
- Sintaksis yang Mudah: jQuery memiliki sintaksis yang sederhana dan mudah dimengerti, terutama bagi pengembang yang kurang berpengalaman. Ini memungkinkan untuk melakukan permintaan AJAX dengan hanya beberapa baris kode.
- Plugin Ekstensif: jQuery memiliki beragam plugin dan ekstensi yang dapat membantu dengan tugas-tugas khusus seperti animasi, manipulasi DOM, dan validasi formulir.

Pilihan antara Fetch API dan jQuery akan sangat tergantung pada **kebutuhan dan konteks proyek**.\
\
Untuk proyek PBP kali ini, menurut saya Fetch API merupakan teknologi yang lebih baik untuk digunakan. Karena jika kita mengembangkan aplikasi web modern dan ingin menulis kode yang bersih dan efisien, Fetch API dengan async/await adalah pilihan yang baik. Fetch API memberikan fleksibilitas dan mempercepat performa aplikasi.\
\
Tetapi di satu sisi, jika dalam pembuatan suatu app perlu mendukung peramban lama atau kita merasa lebih nyaman dengan sintaksis jQuery, maka menggunakan jQuery bisa menjadi solusi yang baik. Namun, harus ingat bahwa jQuery cenderung lebih besar dari Fetch API sehingga dapat memperlambat performa aplikasi.

## Melakukan add-commit-push ke GitHub.
Jalankan perintah:
```
git add .
git commit -m "Tugas6"
git push -u origin main
```

## Melakukan deployment ke PaaS PBP Fasilkom UI dan sertakan tautan aplikasi pada file README.md.
Buka berkas `requirements.txt` pada root folder dan tambahkan `django-environ` di baris terakhir berkas.\
\
Jalankan perintah `pip install -r requirements.txt` untuk menginstal perubahan pada berkas `requirements.txt`\
\
Buat berkas baru bernama Procfile (tanpa format ekstensi file) pada root folder dan isi berkas tersebut dengan kode berikut.
```
release: django-admin migrate --noinput
web: gunicorn Inventory.wsgi
```
Buat folder baru bernama `.github` pada root folder dan buat folder baru di dalam folder dengan nama `workflows`\
\
Buat berkas baru bernama `pbp-deploy.yml` di dalam folder workflows dan isi berkas tersebut dengan kode:
```
name: Deploy

on:
  push:
    branches:
      - main
      - master

jobs:
  Deployment:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - name: Cloning repo
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Push to Dokku server
      uses: dokku/github-action@master
      with:
        branch: 'main'
        git_remote_url: ssh://dokku@${{ secrets.DOKKU_SERVER_IP }}/${{ secrets.DOKKU_APP_NAME }}
        ssh_private_key: ${{ secrets.DOKKU_SSH_PRIVATE_KEY }}
```
Buat berkas baru bernama `.dockerignore` pada root folder dan isi berkas tersebut dengan kode:
```
**/*.pyc
**/*.pyo
**/*.mo
**/*.db
**/*.css.map
**/*.egg-info
**/*.sql.gz
**/__pycache__/
.cache
.project
.idea
.pydevproject
.idea/workspace.xml
.DS_Store
.git/
.sass-cache
.vagrant/
dist
docs
env
logs
src/{{ project_name }}/settings/local.py
src/node_modules
web/media
web/static/CACHE
stats
Dockerfile
.gitignore
Dockerfile
db.sqlite3
**/*.md
logs/
```
Buat berkas baru bernama `Dockerfile` pada root folder dan isi berkas tersebut dengan kode:
```
FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=Inventory.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2

# Install system packages required Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code
COPY . .

RUN python manage.py collectstatic --noinput --clear

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
# CMD gunicorn Inventory.wsgi:application
```
Buka berkas `settings.py` yang ada di dalam folder Inventory
```
...
import environ
import os
...
env = environ.Env()
...
PRODUCTION = env.bool("PRODUCTION", False)
...
if PRODUCTION:
    DATABASES = {
        "default": env.db("DATABASE_URL")
    }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True
...
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Menambahkan environment variables pada GitHub repository dengan nama DOKKU_APP_NAME, DOKKU_SERVER_IP, dan DOKKU_SSH_PRIVATE_KEY dengan nilai yang sesuai.

Menjalankan perintah git push untuk melakukan push ke GitHub repository. Setelah itu, GitHub Actions akan menjalankan workflow pbp-deploy.yml dan melakukan deployment aplikasi ke PaaS PBP Fasilkom UI.

Aplikasi telah berhasil di-deploy ke PaaS PBP Fasilkom UI. Aplikasi dapat diakses pada http://joy-debora-tugas.pbp.cs.ui.ac.id./