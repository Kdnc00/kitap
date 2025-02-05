class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self._ad = ad
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi
        self._isbn = isbn

    def __str__(self):
        return f"{self._ad} - {self._yazar} ({self._sayfa_sayisi} sayfa, ISBN: {self._isbn})"

    def get_isbn(self):
        return self._isbn


class Kutuphane:
    def __init__(self):
        self._kitaplar = []

    def kitap_ekle(self, kitap):
        for mevcut_kitap in self._kitaplar:
            if mevcut_kitap.get_isbn() == kitap.get_isbn():
                raise ValueError("Bu kitap zaten kütüphanede var!")
        self._kitaplar.append(kitap)
        print(f"Kitap eklendi: {kitap}")

    def kitap_sil(self, isbn):
        for kitap in self._kitaplar:
            if kitap.get_isbn() == isbn:
                self._kitaplar.remove(kitap)
                print(f"Kitap silindi: {kitap}")
                return
        print("Böyle bir ISBN numarasına sahip kitap bulunamadı!")

    def kitaplari_goster(self):
        if not self._kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki Kitaplar:")
            for kitap in self._kitaplar:
                print(kitap)
# Kütüphane nesnesi oluştur
kutuphane = Kutuphane()

# Kitaplar oluştur
kitap1 = Kitap("1984", "George Orwell", 328, "12345")
kitap2 = Kitap("Hayvan Çiftliği", "George Orwell", 152, "67890")

# Kitapları ekleyelim
kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)

# Aynı kitabı tekrar eklemeye çalışalım (hata verecek)
try:
    kutuphane.kitap_ekle(kitap1)
except ValueError as e:
    print(f"Hata: {e}")

# Kitapları listeleyelim
kutuphane.kitaplari_goster()

# Kitap silelim
kutuphane.kitap_sil("12345")

# Kütüphane durumunu tekrar gösterelim
kutuphane.kitaplari_goster()

# Olmayan bir kitabı silmeye çalışalım (hata mesajı verecek)
kutuphane.kitap_sil("00000")
#pass