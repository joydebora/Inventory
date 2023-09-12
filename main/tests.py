from django.test import TestCase, ItemPeliharaan

# Create your tests here.

class InventoriPeliharaanTest(TestCase):
    def setUp(self):
        # Membuat data uji coba
        ItemPeliharaan.objects.create(name="Makanan Kucing", amount=50, description="Makanan kucing premium", category="Makanan")
        ItemPeliharaan.objects.create(name="Gembok Kandang", amount=10, description="Gembok anti-korosi", category="Perlengkapan")

    def test_item_peliharaan_creation(self):
        makanan_kucing = ItemPeliharaan.objects.get(name="Makanan Kucing")
        gembok_kandang = ItemPeliharaan.objects.get(name="Gembok Kandang")
        
        self.assertEqual(makanan_kucing.amount, 50)
        self.assertEqual(gembok_kandang.amount, 10)
        self.assertEqual(makanan_kucing.category, "Makanan")
        self.assertEqual(gembok_kandang.category, "Perlengkapan")

    def test_item_peliharaan_description(self):
        makanan_kucing = ItemPeliharaan.objects.get(name="Makanan Kucing")
        gembok_kandang = ItemPeliharaan.objects.get(name="Gembok Kandang")
        
        self.assertEqual(makanan_kucing.description, "Makanan kucing premium")
        self.assertEqual(gembok_kandang.description, "Gembok anti-korosi")