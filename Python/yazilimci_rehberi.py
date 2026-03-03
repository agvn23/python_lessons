# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                              ║
# ║   🐍 PYTHON & YAZILIM DÜŞÜNCE REHBERİ                                       ║
# ║   Hazırlayan: GitHub Copilot                                                ║
# ║   Tarih: 2026-03-02                                                          ║
# ║   Amaç: Yazılımcı gibi düşünmeyi, algoritma tasarlamayı ve                  ║
# ║          problem çözme yeteneğini geliştirmeyi öğretmek.                     ║
# ║                                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# =============================================================================
# 📌 İÇİNDEKİLER
# =============================================================================
# BÖLÜM 1  : Yazılımcı Gibi Düşünmek Ne Demek?
# BÖLÜM 2  : Değişkenler, Veri Tipleri ve Bellek Mantığı
# BÖLÜM 3  : Kontrol Akışı - Karar Verme Mekanizması
# BÖLÜM 4  : Döngüler - Tekrarlayan İşlerin Otomasyonu
# BÖLÜM 5  : Fonksiyonlar - Kodun Modülerleştirilmesi
# BÖLÜM 6  : Veri Yapıları - Doğru Aracı Seçmek
# BÖLÜM 7  : Algoritma Tasarımı - Gerçek Dünya Problemleri
# BÖLÜM 8  : Hata Yönetimi - Savunmacı Programlama
# BÖLÜM 9  : Nesne Yönelimli Programlama (OOP)
# BÖLÜM 10 : Dosya İşlemleri ve Veri Kalıcılığı
# BÖLÜM 11 : Gerçek Hayat Projesi - Mini Banka Sistemi
# BÖLÜM 12 : Karmaşıklık Analizi (Big-O) ve Performans
# =============================================================================


# =============================================================================
# 📖 BÖLÜM 1: YAZILIMCI GİBİ DÜŞÜNMEK NE DEMEK?
# =============================================================================
"""
🧠 BİR YAZILIMCI OLMAK İÇİN ÖĞRENMENİN GEREKENLERİN HARİTASI:

1. PROBLEM ÇÖZME YETENEĞİ (En önemli beceri!)
   → Bir problemi küçük parçalara ayırabilmek
   → Her parçayı bağımsız çözüp birleştirebilmek
   → Bu beceriye "Decomposition" (Ayrıştırma) denir

2. ALGORİTMİK DÜŞÜNCE
   → Adım adım talimat yazabilmek
   → Bir işi en verimli şekilde nasıl yapacağını planlamak
   → "Bilgisayar bunu nasıl anlayacak?" diye sormak

3. SOYUTLAMA (Abstraction)
   → Gereksiz detayları elemek
   → Sadece önemli olan kısımlara odaklanmak
   → Örnek: Araba kullanırken motorun nasıl çalıştığını bilmene gerek yok

4. KALIP TANIMA (Pattern Recognition)
   → Farklı problemlerdeki benzerlikleri görebilmek
   → Daha önce çözdüğün bir problemi yeni duruma uyarlayabilmek

5. VERİ YAPILARI ve ALGORİTMALAR
   → Veriyi nasıl saklayacağını bilmek
   → O veri üzerinde nasıl işlem yapacağını bilmek

💡 ÖNEMLİ KURAL: "Kodlamayı öğrenmek" aslında "düşünmeyi öğrenmek"tir.
   Dil (Python, Java, C++) sadece bir araçtır.
   Asıl güç, problemi çözme mantığındadır.

Bir yazılımcıyı "gerçek sorun çözücü" yapan şeyler:
  ✅ Problemi anlamadan kod yazmaya başlamaz
  ✅ Önce kağıt üzerinde (veya kafasında) çözümü tasarlar
  ✅ Edge case'leri (uç durumları) düşünür
  ✅ Kodunu başkasının okuyabileceği şekilde yazar
  ✅ "Çalışıyor" ile "iyi çalışıyor" arasındaki farkı bilir
  ✅ Hata olasılıklarını önceden hesaba katar
"""

print("=" * 70)
print("🐍 PYTHON & YAZILIM DÜŞÜNCE REHBERİ")
print("=" * 70)
print()


# =============================================================================
# 📖 BÖLÜM 2: DEĞİŞKENLER, VERİ TİPLERİ VE BELLEK MANTIĞI
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Değişkenler, bellekteki kutulara isim vermektir.
Bilgisayar her şeyi 0 ve 1 olarak saklar, ama biz insanlar
anlamlı isimler kullanarak bu verilere erişiriz.

NEDEN ÖNEMLİ?
→ Doğru veri tipi seçimi = Daha az bellek kullanımı + Daha hızlı program
→ Yanlış veri tipi = Bug'ların (hataların) en büyük kaynağı
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 2: DEĞİŞKENLER VE VERİ TİPLERİ")
print("=" * 70)

# --- Temel Veri Tipleri ---

# 1. INTEGER (Tam Sayı) - Sayma ve hesaplama için
yas = 25
# NEDEN int? → Yaş asla 25.5 olmaz, tam sayıdır.
# BELLEKTEKİ HALİ: Python'da int dinamik boyutludur (sınırsız büyüklük)

# 2. FLOAT (Ondalıklı Sayı) - Hassas hesaplamalar için
sicaklik = 36.6
# NEDEN float? → Sıcaklık ondalıklı olabilir.
# ⚠️ DİKKAT: Float'lar tam kesin değildir!
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004 çıkar!
# Bu, bilgisayarın ondalıklı sayıları binary'de saklamasından kaynaklanır.
# ÇÖZÜM: Para hesabı gibi hassas işlemlerde 'decimal' modülü kullan!

from decimal import Decimal
fiyat_1 = Decimal("0.1")
fiyat_2 = Decimal("0.2")
print(f"Decimal ile: 0.1 + 0.2 = {fiyat_1 + fiyat_2}")  # Tam 0.3 verir

# 3. STRING (Metin) - Yazılar, isimler, mesajlar için
isim = "Abdulkadir"
# NEDEN string? → İsimler metindir.
# String'ler IMMUTABLE'dır (değiştirilemez)!
# Bu ne demek? Bir string'in bir harfini değiştiremezsin, yeni string yaratırsın.
# isim[0] = "a"  → Bu HATA verir!
yeni_isim = isim.lower()  # Yeni bir string oluşturur: "abdulkadir"

# 4. BOOLEAN (Doğru/Yanlış) - Karar verme için
aktif_mi = True
# NEDEN boolean? → Sadece iki durumu olan şeyler için mükemmeldir.
# Yazılımın TEMELİ karar vermektir ve kararlar boolean'a dayanır.

# 5. NONE (Hiçbir Şey) - Değer yokluğunu ifade etmek için
sonuc = None
# NEDEN None? → "Henüz bir değer atanmadı" demektir.
# ⚠️ None, 0 veya "" (boş string) ile AYNI DEĞİLDİR!
# None = "Hiçbir şey yok", 0 = "Sıfır sayısı var", "" = "Boş metin var"

print(f"\nİsim: {isim} (tip: {type(isim).__name__})")
print(f"Yaş: {yas} (tip: {type(yas).__name__})")
print(f"Sıcaklık: {sicaklik} (tip: {type(sicaklik).__name__})")
print(f"Aktif mi: {aktif_mi} (tip: {type(aktif_mi).__name__})")
print(f"Sonuç: {sonuc} (tip: {type(sonuc).__name__})")

# --- Tür Dönüşümleri (Type Casting) ---
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Kullanıcıdan gelen veri HER ZAMAN string'tir (input() fonksiyonu).
Bu yüzden dönüşüm yapmayı bilmek kritiktir.
"""
sayi_metin = "42"
sayi_int = int(sayi_metin)        # String → Integer
sayi_float = float(sayi_metin)    # String → Float
tekrar_metin = str(sayi_int)      # Integer → String

print(f"\n'42' string → int: {sayi_int}, float: {sayi_float}")
print(f"42 int → string: '{tekrar_metin}'")


# =============================================================================
# 📖 BÖLÜM 3: KONTROL AKIŞI - KARAR VERME MEKANİZMASI
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Programlar "akıllı" değildir. Sadece verilen kurallara göre karar verir.
if/elif/else yapısı, programın beynindeki karar mekanizmasıdır.

BİR YAZILIMCI KARARLARI NASIL PLANLAR?
1. Önce TÜM olası durumları listeler
2. Her durum için ne yapılacağını belirler
3. UÇ DURUMLARI (edge cases) düşünür
4. Default (varsayılan) bir davranış belirler
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 3: KONTROL AKIŞI")
print("=" * 70)


def not_hesapla(puan):
    """
    📝 PROBLEM: Bir öğrencinin puanına göre harf notu hesapla.

    🧠 YAZILIMCI YAKLAŞIMI:
    1. Önce geçersiz girdi kontrolü yap (savunmacı programlama)
    2. Sonra büyükten küçüğe doğru kontrol et (mantıksal sıra)
    3. Her durumu kapsadığından emin ol

    NEDEN büyükten küçüğe? → Çünkü ilk eşleşen koşulda durur.
    Eğer küçükten büyüğe gitsek, 95 puan "F >= 0" koşuluna takılırdı!
    """
    # Adım 1: Geçersiz girdi kontrolü
    # NEDEN? → Kullanıcı "abc" veya -5 veya 150 gönderebilir!
    # Gerçek yazılımcı HER ZAMAN girdileri doğrular.
    if not isinstance(puan, (int, float)):
        return "HATA: Puan sayı olmalıdır!"

    if puan < 0 or puan > 100:
        return "HATA: Puan 0-100 arasında olmalıdır!"

    # Adım 2: Not hesaplama (büyükten küçüğe)
    if puan >= 90:
        harf = "AA"
        durum = "Mükemmel! 🌟"
    elif puan >= 80:
        harf = "BA"
        durum = "Çok İyi! 👏"
    elif puan >= 70:
        harf = "BB"
        durum = "İyi 👍"
    elif puan >= 60:
        harf = "CB"
        durum = "Orta 📚"
    elif puan >= 50:
        harf = "CC"
        durum = "Geçer ✅"
    else:
        harf = "FF"
        durum = "Kaldı ❌"

    return f"Puan: {puan} → Not: {harf} - {durum}"


# Test edelim - iyi bir yazılımcı HER ZAMAN test eder
test_puanlari = [95, 85, 72, 63, 51, 30, -5, 105, "abc"]
print("\n📊 Not Hesaplama Sonuçları:")
for puan in test_puanlari:
    print(f"  {not_hesapla(puan)}")


# --- Daha karmaşık bir karar ağacı ---
def vergi_hesapla(gelir, medeni_durum="bekar"):
    """
    📝 PROBLEM: Gelir vergisi hesaplama (basitleştirilmiş)

    🧠 YAZILIMCI YAKLAŞIMI:
    Gerçek dünyada vergi dilimleri iç içe geçer.
    Bunu nasıl modelleriz?
    → Dilim bazlı hesaplama (her dilime ayrı oran uygulanır)

    Bu "kademeli hesaplama" kalıbı birçok yerde kullanılır:
    - Vergi hesaplama
    - Kargo ücreti hesaplama
    - İndirim hesaplama
    """
    if gelir < 0:
        return "HATA: Gelir negatif olamaz!"

    # Vergi dilimleri (Tuple listesi: üst sınır, oran)
    # NEDEN tuple listesi? → Dilimleri kolayca değiştirebilmek için!
    # Eğer if/elif ile yazsaydık, her değişiklikte kodu değiştirmemiz gerekirdi.
    # Bu yaklaşıma "Data-Driven Programming" denir.
    if medeni_durum == "evli":
        dilimler = [
            (50_000, 0.15),    # İlk 50.000 TL → %15
            (120_000, 0.20),   # 50.001 - 120.000 TL → %20
            (250_000, 0.27),   # 120.001 - 250.000 TL → %27
            (float('inf'), 0.35)  # 250.001+ → %35
        ]
    else:
        dilimler = [
            (32_000, 0.15),
            (70_000, 0.20),
            (170_000, 0.27),
            (float('inf'), 0.35)
        ]

    toplam_vergi = 0
    kalan_gelir = gelir
    onceki_sinir = 0

    for ust_sinir, oran in dilimler:
        if kalan_gelir <= 0:
            break

        # Bu dilimdeki vergiye tabi tutar
        dilim_tutari = min(kalan_gelir, ust_sinir - onceki_sinir)
        dilim_vergisi = dilim_tutari * oran

        toplam_vergi += dilim_vergisi
        kalan_gelir -= dilim_tutari
        onceki_sinir = ust_sinir

    efektif_oran = (toplam_vergi / gelir * 100) if gelir > 0 else 0

    return {
        "gelir": gelir,
        "vergi": round(toplam_vergi, 2),
        "efektif_oran": f"%{efektif_oran:.1f}",
        "net_gelir": round(gelir - toplam_vergi, 2)
    }


print("\n💰 Vergi Hesaplama:")
for gelir in [25_000, 80_000, 200_000, 500_000]:
    sonuc = vergi_hesapla(gelir)
    print(f"  Gelir: {sonuc['gelir']:>10,} TL → "
          f"Vergi: {sonuc['vergi']:>10,.2f} TL "
          f"(Efektif: {sonuc['efektif_oran']}) → "
          f"Net: {sonuc['net_gelir']:>10,.2f} TL")


# =============================================================================
# 📖 BÖLÜM 4: DÖNGÜLER - TEKRARLAYAN İŞLERİN OTOMASYONU
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Döngü, "aynı işi farklı verilerle tekrar tekrar yap" demektir.
Bilgisayarın en güçlü yönü milyonlarca tekrarı saniyeler içinde yapmasıdır.

FOR vs WHILE:
→ for  : "Kaç kere döneceğimi biliyorum" (koleksiyon üzerinde gezinme)
→ while : "Bir koşul sağlanana kadar dönmeye devam et" (belirsiz tekrar)

⚠️ SONSUZ DÖNGÜ TEHLİKESİ:
while True gibi döngülerde mutlaka bir çıkış koşulu olmalı!
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 4: DÖNGÜLER")
print("=" * 70)


# --- PROBLEM: Asal Sayı Bulucu ---
def asal_mi(sayi):
    """
    📝 PROBLEM: Bir sayının asal olup olmadığını belirle.

    🧠 ALGORİTMA TASARIMI (Adım adım düşünelim):

    Asal sayı nedir? → Sadece 1 ve kendisine bölünen sayı.

    NAİF YAKLAŞIM (Kötü):
    2'den sayıya kadar hepsini kontrol et → O(n) karmaşıklık

    AKILLI YAKLAŞIM (İyi):
    Sadece karekökene kadar kontrol et → O(√n) karmaşıklık

    NEDEN KAREKÖKE KADAR YETERLİ?
    → Eğer n = a × b ise, a ve b'den biri mutlaka √n'den küçük veya eşittir.
    → Örnek: 36 = 6×6 = 4×9 = 3×12 = 2×18
      Gördüğün gibi, çarpanlardan biri hep ≤6 (√36)

    EK OPTİMİZASYON:
    → 2'den büyük çift sayılar asal olamaz
    → 3'ten büyük 3'ün katları asal olamaz
    → Sadece 6k±1 formundaki sayıları kontrol et
    """
    # Uç durumlar (edge cases) - BUNLARI DÜŞÜNMEK SENİ İYİ YAZILIMCI YAPAR
    if sayi < 2:
        return False   # 0, 1 ve negatif sayılar asal değil
    if sayi < 4:
        return True    # 2 ve 3 asal
    if sayi % 2 == 0:
        return False   # Çift sayılar asal değil (2 hariç)
    if sayi % 3 == 0:
        return False   # 3'ün katları asal değil (3 hariç)

    # 6k±1 optimizasyonu
    # Her asal sayı (5'ten büyük) 6k-1 veya 6k+1 formundadır
    # NEDEN? Çünkü:
    # 6k+0 → 6'ya bölünür
    # 6k+1 → Asal OLABİLİR ✓
    # 6k+2 → 2'ye bölünür
    # 6k+3 → 3'e bölünür
    # 6k+4 → 2'ye bölünür
    # 6k+5 → Asal OLABİLİR ✓ (6k-1 ile aynı)
    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6  # 6'şar atla (sadece 6k±1'leri kontrol et)

    return True


def asal_sayilari_bul(limit):
    """Belirli bir limite kadar tüm asal sayıları bul."""
    asallar = []
    for sayi in range(2, limit + 1):
        if asal_mi(sayi):
            asallar.append(sayi)
    return asallar


print("\n🔢 İlk 50'ye Kadar Asal Sayılar:")
asallar = asal_sayilari_bul(50)
print(f"  {asallar}")
print(f"  Toplam: {len(asallar)} asal sayı")

# Performans karşılaştırması
import time


def asal_mi_yavas(sayi):
    """Naif yaklaşım - karşılaştırma için"""
    if sayi < 2:
        return False
    for i in range(2, sayi):  # Tüm sayıları kontrol eder (YAVAŞ!)
        if sayi % i == 0:
            return False
    return True


# Büyük bir sayıyla test edelim
buyuk_sayi = 1_000_003  # Bu asal bir sayı

baslangic = time.perf_counter()
sonuc1 = asal_mi_yavas(buyuk_sayi)
sure_yavas = time.perf_counter() - baslangic

baslangic = time.perf_counter()
sonuc2 = asal_mi(buyuk_sayi)
sure_hizli = time.perf_counter() - baslangic

print(f"\n⚡ Performans Karşılaştırması ({buyuk_sayi:,} sayısı için):")
print(f"  Naif Yöntem  : {sure_yavas:.6f} saniye")
print(f"  Akıllı Yöntem: {sure_hizli:.6f} saniye")
if sure_yavas > 0 and sure_hizli > 0:
    print(f"  Hız Farkı    : ~{sure_yavas / sure_hizli:.0f}x daha hızlı!")


# =============================================================================
# 📖 BÖLÜM 5: FONKSİYONLAR - KODUN MODÜLERLEŞTİRİLMESİ
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Fonksiyon = Tekrar kullanılabilir kod bloğu
DRY prensibi: "Don't Repeat Yourself" (Kendini Tekrar Etme)

İYİ FONKSİYON YAZMANIN KURALLARI:
1. Tek bir iş yapsın (Single Responsibility)
2. İsmi ne yaptığını anlatsın (fiil ile başlasın)
3. Çok uzun olmasın (20-30 satır ideal)
4. Parametreleri çok fazla olmasın (3-4 ideal)
5. Docstring (açıklama) içersin
6. Yan etkisi (side effect) minimum olsun
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 5: FONKSİYONLAR")
print("=" * 70)


# --- PROBLEM: Metin Analiz Aracı ---
def metni_analiz_et(metin):
    """
    📝 PROBLEM: Verilen bir metni çok yönlü analiz et.

    🧠 YAZILIMCI YAKLAŞIMI:
    Bu problemi alt problemlere ayıralım (Decomposition):
    1. Kelime sayısını bul
    2. Cümle sayısını bul
    3. En uzun kelimeyi bul
    4. Kelime frekanslarını hesapla
    5. Okunabilirlik skoru hesapla

    Her biri ayrı bir fonksiyon olabilirdi, ama burada
    tek fonksiyonda dictionary döndürerek çözüyoruz.
    """
    if not metin or not metin.strip():
        return {"hata": "Boş metin analiz edilemez!"}

    # Temizleme: Fazla boşlukları kaldır
    temiz_metin = " ".join(metin.split())

    # Kelime analizi
    kelimeler = temiz_metin.split()
    kelime_sayisi = len(kelimeler)

    # Cümle sayısı (nokta, soru işareti, ünlem ile biten)
    cumle_sayisi = sum(1 for c in temiz_metin if c in ".!?") or 1

    # En uzun ve en kısa kelime
    # NEDEN key=len? → sorted/max/min fonksiyonlarına özel sıralama kriteri verebiliriz
    # Bu "higher-order function" kullanımıdır - fonksiyona fonksiyon geçmek
    temiz_kelimeler = [k.strip(".,!?;:") for k in kelimeler]
    en_uzun = max(temiz_kelimeler, key=len)
    en_kisa = min(temiz_kelimeler, key=len)

    # Kelime frekansı (hangi kelime kaç kez kullanılmış)
    # NEDEN dictionary? → Anahtar-değer ilişkisi için en doğru veri yapısı
    frekans = {}
    for kelime in temiz_kelimeler:
        kelime_kucuk = kelime.lower()
        # .get() metodu: Anahtar yoksa varsayılan değer döndürür
        # NEDEN .get()? → KeyError hatası almamak için savunmacı yaklaşım
        frekans[kelime_kucuk] = frekans.get(kelime_kucuk, 0) + 1

    # En çok kullanılan 5 kelime
    # sorted() + key parametresi: Özel sıralama kriteri
    # reverse=True: Büyükten küçüğe sırala
    en_sik_5 = sorted(frekans.items(), key=lambda x: x[1], reverse=True)[:5]

    # Ortalama kelime uzunluğu
    ort_kelime_uzunlugu = sum(len(k) for k in temiz_kelimeler) / kelime_sayisi

    return {
        "kelime_sayisi": kelime_sayisi,
        "cumle_sayisi": cumle_sayisi,
        "karakter_sayisi": len(temiz_metin),
        "en_uzun_kelime": en_uzun,
        "en_kisa_kelime": en_kisa,
        "ortalama_kelime_uzunlugu": round(ort_kelime_uzunlugu, 1),
        "en_sik_kelimeler": en_sik_5,
        "benzersiz_kelime_sayisi": len(frekans)
    }


ornek_metin = """
Python programlama dili, okunabilirliği ve sadeliği ile bilinir.
Python ile web geliştirme, veri bilimi, yapay zeka ve otomasyon yapabilirsiniz.
Python öğrenmek, programlama dünyasına girmek için harika bir başlangıçtır.
Python topluluğu çok büyük ve yardımseverdir. Python ile her şey mümkün!
"""

analiz = metni_analiz_et(ornek_metin)
print("\n📝 Metin Analiz Sonuçları:")
for anahtar, deger in analiz.items():
    if anahtar == "en_sik_kelimeler":
        print(f"  {anahtar}:")
        for kelime, sayi in deger:
            print(f"    '{kelime}' → {sayi} kez")
    else:
        print(f"  {anahtar}: {deger}")


# --- Fonksiyon İleri Teknikler ---

# 1. Default Parametreler
def selamla(isim, dil="tr"):
    """
    NEDEN default parametre?
    → Çoğu kullanıcı Türkçe kullanacak, her seferinde belirtmesin.
    → Ama isterse değiştirebilsin (esneklik).
    """
    selamlar = {
        "tr": f"Merhaba {isim}!",
        "en": f"Hello {isim}!",
        "de": f"Hallo {isim}!",
        "ar": f"!مرحبا {isim}"
    }
    return selamlar.get(dil, f"Merhaba {isim}!")


# 2. *args ve **kwargs - Esnek parametre sayısı
def hesap_makinesi(islem, *sayilar):
    """
    NEDEN *args?
    → Kaç sayı geleceğini bilmiyoruz.
    → 2 sayı da olabilir, 100 sayı da olabilir.
    → Bu esneklik gerçek dünya yazılımında çok önemli.
    """
    if not sayilar:
        return "HATA: En az bir sayı gerekli!"

    islemler = {
        "topla": sum(sayilar),
        "carp": 1,  # Aşağıda hesaplanacak
        "max": max(sayilar),
        "min": min(sayilar),
        "ortalama": sum(sayilar) / len(sayilar)
    }

    if islem == "carp":
        sonuc = 1
        for s in sayilar:
            sonuc *= s
        return sonuc

    return islemler.get(islem, "HATA: Bilinmeyen işlem!")


print(f"\n🧮 Hesap Makinesi:")
print(f"  topla(1,2,3,4,5) = {hesap_makinesi('topla', 1, 2, 3, 4, 5)}")
print(f"  carp(2,3,4) = {hesap_makinesi('carp', 2, 3, 4)}")
print(f"  ortalama(10,20,30) = {hesap_makinesi('ortalama', 10, 20, 30)}")


# =============================================================================
# 📖 BÖLÜM 6: VERİ YAPILARI - DOĞRU ARACI SEÇMEK
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Doğru veri yapısını seçmek, bir marangozun doğru aleti seçmesi gibidir.
Çivi çakmak için tornavida kullanmazsın!

VERİ YAPISI SEÇİM REHBERİ:
┌─────────────┬────────────────────────────────────────────┐
│ Veri Yapısı │ Ne Zaman Kullanılır?                       │
├─────────────┼────────────────────────────────────────────┤
│ list        │ Sıralı, değiştirilebilir koleksiyon        │
│ tuple       │ Sıralı, değiştirilEMEZ koleksiyon          │
│ dict        │ Anahtar-değer çiftleri                     │
│ set         │ Benzersiz elemanlar, hızlı arama           │
│ deque       │ Her iki uçtan hızlı ekleme/çıkarma         │
└─────────────┴────────────────────────────────────────────┘
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 6: VERİ YAPILARI")
print("=" * 70)

# --- LIST (Liste) ---
"""
Liste: Python'un en çok kullanılan veri yapısı.
İç yapısı: Dinamik dizi (dynamic array)
→ Elemanlar bellekte yan yana tutulur.
→ Index ile erişim O(1) - çok hızlı.
→ Ortaya ekleme O(n) - yavaş (kaydırma gerekir).
"""
print("\n📋 LİSTE İşlemleri:")
ogrenciler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Can"]

# List Comprehension - Python'un en güçlü özelliklerinden biri
# NEDEN? → For döngüsü + append yerine tek satırda liste oluştur
# Daha okunabilir ve daha hızlı (Python C seviyesinde optimize eder)
uzun_isimler = [isim for isim in ogrenciler if len(isim) > 3]
print(f"  3 harften uzun isimler: {uzun_isimler}")

# Slicing (dilimleme) - listelerin süper gücü
print(f"  İlk 3: {ogrenciler[:3]}")
print(f"  Son 2: {ogrenciler[-2:]}")
print(f"  Tersten: {ogrenciler[::-1]}")

# --- DICTIONARY (Sözlük) ---
"""
Dictionary: Anahtar-değer çiftleri.
İç yapısı: Hash Table (karma tablo)
→ Anahtar ile erişim O(1) - çok hızlı!
→ NEDEN hızlı? Hash fonksiyonu anahtarı direkt bellek adresine çevirir.
→ Dezavantaj: Listeden daha fazla bellek kullanır.
"""
print("\n📖 SÖZLÜK İşlemleri:")

# Gerçekçi örnek: Öğrenci not sistemi
ogrenci_notlari = {
    "Ali": {"matematik": 85, "fizik": 72, "kimya": 90},
    "Ayşe": {"matematik": 95, "fizik": 88, "kimya": 92},
    "Mehmet": {"matematik": 60, "fizik": 55, "kimya": 70},
}

# Dictionary comprehension ile ortalama hesaplama
ortalamalar = {
    isim: round(sum(notlar.values()) / len(notlar), 1)
    for isim, notlar in ogrenci_notlari.items()
}
print(f"  Ortalamalar: {ortalamalar}")

# En başarılı öğrenci
en_basarili = max(ortalamalar, key=ortalamalar.get)
print(f"  En başarılı: {en_basarili} ({ortalamalar[en_basarili]})")

# --- SET (Küme) ---
"""
Set: Benzersiz elemanlar koleksiyonu.
İç yapısı: Hash Table (dictionary gibi, ama sadece anahtarlar)
→ 'in' operatörü O(1) - listede O(n)!
→ Küme işlemleri (birleşim, kesişim) matematiksel işlemlere birebir uyar.

NEDEN SET KULLANILIR?
Listede "x in liste" → Her elemanı tek tek kontrol eder (yavaş)
Set'te "x in kume"  → Hash ile direkt bakar (hızlı)
"""
print("\n🔵 SET (Küme) İşlemleri:")

python_bilenler = {"Ali", "Ayşe", "Can", "Deniz", "Ece"}
java_bilenler = {"Ayşe", "Fatma", "Can", "Gül", "Hakan"}

# Küme operasyonları - gerçek dünyada çok kullanılır
print(f"  Her ikisini bilen : {python_bilenler & java_bilenler}")  # Kesişim
print(f"  En az birini bilen: {python_bilenler | java_bilenler}")  # Birleşim
print(f"  Sadece Python     : {python_bilenler - java_bilenler}")  # Fark
print(f"  Sadece birini     : {python_bilenler ^ java_bilenler}")  # Simetrik fark

# --- Performans Karşılaştırması ---
print("\n⚡ Veri Yapısı Performans Karşılaştırması:")

# 100.000 elemanlı liste vs set'te arama
import time

buyuk_liste = list(range(100_000))
buyuk_set = set(range(100_000))
aranan = 99_999  # En kötü durum (worst case)

# Liste'de arama
baslangic = time.perf_counter()
for _ in range(1000):
    _ = aranan in buyuk_liste
sure_liste = time.perf_counter() - baslangic

# Set'te arama
baslangic = time.perf_counter()
for _ in range(1000):
    _ = aranan in buyuk_set
sure_set = time.perf_counter() - baslangic

print(f"  Liste'de arama (1000x): {sure_liste:.4f} saniye")
print(f"  Set'te arama (1000x)  : {sure_set:.6f} saniye")
print(f"  Set, ~{sure_liste / sure_set:.0f}x daha hızlı!")


# =============================================================================
# 📖 BÖLÜM 7: ALGORİTMA TASARIMI - GERÇEK DÜNYA PROBLEMLERİ
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Algoritma = Problem çözme tarifi
İyi algoritma = Doğru + Verimli + Okunabilir çözüm

ALGORİTMA TASARLAMA ADIMLARI:
1. Problemi tam olarak anla (girdiler, çıktılar, kısıtlar)
2. Küçük örneklerle elle çöz
3. Kalıp/pattern bul
4. Adımları yaz (pseudocode)
5. Kodla
6. Test et (normal + uç durumlar)
7. Optimize et (gerekirse)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 7: ALGORİTMA TASARIMI")
print("=" * 70)


# ============================================================
# 🧩 ALGORİTMA 1: İKİLİ ARAMA (Binary Search)
# ============================================================
def ikili_arama(sirali_liste, hedef):
    """
    📝 PROBLEM: Sıralı bir listede bir elemanı bul.

    🧠 ALGORİTMA TASARIM SÜRECİ:

    NAİF YAKLAŞIM: Baştan sona tara → O(n)
    → 1 milyon elemanda en kötü 1 milyon karşılaştırma

    AKILLI YAKLAŞIM: İkili arama → O(log n)
    → 1 milyon elemanda en kötü ~20 karşılaştırma!

    NASIL ÇALIŞIR?
    → Telefon rehberinde isim aramayı düşün:
    1. Ortadan aç
    2. Aradığın isim ortadakinden küçükse sol yarıya git
    3. Büyükse sağ yarıya git
    4. Her adımda arama alanı YARIYA düşer

    NEDEN LOGARİTMİK?
    → Her adımda n → n/2 → n/4 → n/8 → ... → 1
    → log₂(1.000.000) ≈ 20 adım!

    ÖN KOŞUL: Liste SIRALI olmalı! (Sırasız listede çalışmaz)
    """
    sol = 0
    sag = len(sirali_liste) - 1
    adim = 0

    while sol <= sag:
        adim += 1
        # Ortayı bul
        # NEDEN (sol + sag) // 2 yerine sol + (sag - sol) // 2 ?
        # → Çok büyük sayılarda integer overflow'u önler (C gibi dillerde önemli)
        # → Python'da sorun olmaz ama iyi alışkanlık edinmek için böyle yazıyoruz
        orta = sol + (sag - sol) // 2

        if sirali_liste[orta] == hedef:
            return {"index": orta, "adim": adim, "bulundu": True}
        elif sirali_liste[orta] < hedef:
            sol = orta + 1  # Sağ yarıya git
        else:
            sag = orta - 1  # Sol yarıya git

    return {"index": -1, "adim": adim, "bulundu": False}


# Test
sirali = list(range(0, 1_000_001, 2))  # 0, 2, 4, ..., 1000000
print(f"\n🔍 İkili Arama ({len(sirali):,} elemanlı sıralı liste):")

for hedef in [500_000, 1, 999_999, 7]:
    sonuc = ikili_arama(sirali, hedef)
    if sonuc["bulundu"]:
        print(f"  {hedef:>10,} → Bulundu! Index: {sonuc['index']:,}, "
              f"Adım: {sonuc['adim']}")
    else:
        print(f"  {hedef:>10,} → Bulunamadı! Adım: {sonuc['adim']}")


# ============================================================
# 🧩 ALGORİTMA 2: SIRALAMA - Birleştirme Sıralaması (Merge Sort)
# ============================================================
def birlestirme_siralamasi(liste):
    """
    📝 PROBLEM: Bir listeyi küçükten büyüğe sırala.

    🧠 ALGORİTMA TASARIM SÜRECİ:

    Bu algoritma "Böl ve Fethet" (Divide & Conquer) stratejisini kullanır.
    Bu strateji yazılımda EN ÖNEMLİ problem çözme tekniklerinden biridir!

    FİKİR:
    1. Listeyi ikiye böl (Böl)
    2. Her yarıyı kendi içinde sırala (Fethet - rekürsif)
    3. İki sıralı yarıyı birleştir (Birleştir)

    NEDEN BU İŞE YARAR?
    → İki sıralı listeyi birleştirmek çok kolaydır
    → Her iki listeden de en küçüğü al, yeni listeye koy
    → Bu O(n) işlem

    KARMAŞIKLIK: O(n log n) - Sıralama için en iyi genel karmaşıklık
    → n eleman var, her biri log n seviye derinlikte işleniyor

    KARŞILAŞTIRMA:
    Bubble Sort: O(n²) → 1 milyon eleman = 1 trilyon işlem 😱
    Merge Sort:  O(n log n) → 1 milyon eleman ≈ 20 milyon işlem 🚀
    """
    # Taban durumu (base case) - Rekürsiyonun durma koşulu
    # NEDEN? → 0 veya 1 elemanlı liste zaten sıralıdır
    if len(liste) <= 1:
        return liste

    # BÖL: Listeyi ikiye ayır
    orta = len(liste) // 2
    sol_yari = liste[:orta]
    sag_yari = liste[orta:]

    # FETHET: Her yarıyı rekürsif olarak sırala
    sol_sirali = birlestirme_siralamasi(sol_yari)
    sag_sirali = birlestirme_siralamasi(sag_yari)

    # BİRLEŞTİR: İki sıralı listeyi birleştir
    return _birlestir(sol_sirali, sag_sirali)


def _birlestir(sol, sag):
    """İki sıralı listeyi tek sıralı liste olarak birleştir."""
    sonuc = []
    i = j = 0  # İki pointer (işaretçi) kullanıyoruz

    # Her iki listede de eleman varken
    while i < len(sol) and j < len(sag):
        if sol[i] <= sag[j]:
            sonuc.append(sol[i])
            i += 1
        else:
            sonuc.append(sag[j])
            j += 1

    # Kalan elemanları ekle (birinden elemanlar bitmiş olabilir)
    # NEDEN extend? → append tek eleman ekler, extend tüm listeyi ekler
    sonuc.extend(sol[i:])
    sonuc.extend(sag[j:])

    return sonuc


# Test
karisik = [38, 27, 43, 3, 9, 82, 10]
print(f"\n📊 Birleştirme Sıralaması:")
print(f"  Girdi : {karisik}")
print(f"  Çıktı : {birlestirme_siralamasi(karisik)}")


# ============================================================
# 🧩 ALGORİTMA 3: Para Üstü Problemi (Greedy / Açgözlü Algoritma)
# ============================================================
def para_ustu_hesapla(tutar, birimler=None):
    """
    📝 PROBLEM: Verilen tutarı en az sayıda banknotla/bozuklukla öde.

    🧠 ALGORİTMA TASARIM SÜRECİ:

    Bu bir "Greedy" (Açgözlü) algoritmadır.
    Greedy strateji: Her adımda O ANKİ en iyi seçimi yap.

    FİKİR:
    → Her zaman en büyük birimden başla
    → O birimden kaç tane kullanabileceğini hesapla
    → Kalan tutarla bir sonraki birime geç

    NEDEN ÇALIŞIR?
    → Para birimleri özel tasarlanmıştır (her biri bir sonrakinin katı)
    → Bu yüzden açgözlü yaklaşım optimal sonuç verir

    ⚠️ DİKKAT: Greedy her zaman optimal sonuç vermez!
    → Örnek: Birimler [1, 3, 4] ve tutar 6 olsaydı:
      Greedy: 4+1+1 = 3 birim (yanlış!)
      Optimal: 3+3 = 2 birim (doğru!)
    → Bu durumda "Dynamic Programming" gerekir.
    """
    if birimler is None:
        # Türk Lirası birimleri
        birimler = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05]

    if tutar < 0:
        return "HATA: Tutar negatif olamaz!"

    sonuc = {}
    kalan = round(tutar, 2)  # Float hassasiyet sorunu için yuvarlama

    for birim in birimler:
        if kalan >= birim:
            adet = int(kalan // birim)
            sonuc[birim] = adet
            kalan = round(kalan - (adet * birim), 2)

        if kalan == 0:
            break

    toplam_birim = sum(sonuc.values())

    return {
        "tutar": tutar,
        "dagitim": sonuc,
        "toplam_birim_sayisi": toplam_birim,
        "kalan": kalan
    }


print(f"\n💵 Para Üstü Hesaplama:")
for tutar in [187.75, 43.60, 999.95]:
    sonuc = para_ustu_hesapla(tutar)
    print(f"\n  {tutar} TL için:")
    print(f"  Toplam {sonuc['toplam_birim_sayisi']} birim:")
    for birim, adet in sonuc["dagitim"].items():
        birim_str = f"{birim} TL" if birim >= 1 else f"{int(birim*100)} kuruş"
        print(f"    {birim_str} × {adet}")


# ============================================================
# 🧩 ALGORİTMA 4: Fibonacci - Farklı Yaklaşımların Karşılaştırması
# ============================================================
"""
📝 PROBLEM: N'inci Fibonacci sayısını hesapla.
F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)

Bu problemi 3 farklı yöntemle çözerek
"aynı probleme farklı yaklaşımların" etkisini görelim.
"""
print(f"\n📐 Fibonacci - 3 Farklı Yaklaşım:")


# Yöntem 1: Naif Rekürsiyon (KÖTÜ!)
def fib_rekursif(n):
    """
    ⚠️ KÖTÜ YAKLAŞIM - O(2^n) karmaşıklık!
    NEDEN KÖTÜ?
    → fib(5) hesaplarken fib(3)'ü 2 kez, fib(2)'yi 3 kez hesaplar
    → Aynı işi tekrar tekrar yapar (gereksiz iş)
    → fib(40) bile dakikalar sürer!

    Bu yaklaşımı KULLANMA, sadece neyin kötü olduğunu göstermek için burada.
    """
    if n <= 1:
        return n
    return fib_rekursif(n - 1) + fib_rekursif(n - 2)


# Yöntem 2: Memoization (Üstten Aşağı Dinamik Programlama)
def fib_memo(n, onbellek=None):
    """
    ✅ İYİ YAKLAŞIM - O(n) karmaşıklık!
    NEDEN İYİ?
    → Hesapladığımız her değeri "önbellek"te saklıyoruz
    → Aynı değer tekrar istendiğinde hesaplamak yerine önbellekten dönüyoruz
    → Bu tekniğe "Memoization" denir

    GERÇEK DÜNYA BENZETMESİ:
    → Bir telefon numarasını her aradığında rehbere bakmak yerine
      aklında tutmak gibi. İlk seferde bak, sonra hatırla!
    """
    if onbellek is None:
        onbellek = {}

    if n in onbellek:
        return onbellek[n]

    if n <= 1:
        return n

    onbellek[n] = fib_memo(n - 1, onbellek) + fib_memo(n - 2, onbellek)
    return onbellek[n]


# Yöntem 3: İteratif (Alttan Yukarı Dinamik Programlama)
def fib_iteratif(n):
    """
    ✅ EN İYİ YAKLAŞIM - O(n) zaman, O(1) bellek!
    NEDEN EN İYİ?
    → Sadece son iki değeri tutar (bellek tasarrufu)
    → Rekürsiyon yığını kullanmaz (stack overflow riski yok)
    → Basit ve anlaşılır

    BU TEKNİK NEDEN ÖNEMLİ?
    → "Aynı anda tüm geçmişi bilmeye gerek yok,
       sadece son durumu bilmek yeterli" ilkesi
    → Bu ilke birçok DP (Dynamic Programming) probleminde kullanılır
    """
    if n <= 1:
        return n

    onceki = 0    # F(0)
    simdiki = 1   # F(1)

    for _ in range(2, n + 1):
        onceki, simdiki = simdiki, onceki + simdiki
        # ↑ Python'un güzel özelliği: Tuple unpacking
        # Geçici değişken kullanmadan iki değişkeni aynı anda güncelleme

    return simdiki


# Performans karşılaştırması
n = 35

baslangic = time.perf_counter()
sonuc1 = fib_rekursif(n)
sure1 = time.perf_counter() - baslangic

baslangic = time.perf_counter()
sonuc2 = fib_memo(n)
sure2 = time.perf_counter() - baslangic

baslangic = time.perf_counter()
sonuc3 = fib_iteratif(n)
sure3 = time.perf_counter() - baslangic

print(f"\n  Fibonacci({n}) = {sonuc3:,}")
print(f"  Naif Rekürsiyon : {sure1:.4f} saniye (O(2^n) 😱)")
print(f"  Memoization     : {sure2:.6f} saniye (O(n) ✅)")
print(f"  İteratif        : {sure3:.6f} saniye (O(n), O(1) bellek 🏆)")


# ============================================================
# 🧩 ALGORİTMA 5: Anagram Kontrolü
# ============================================================
def anagram_mi(kelime1, kelime2):
    """
    📝 PROBLEM: İki kelimenin anagram olup olmadığını kontrol et.
    Anagram: Aynı harflerden oluşan farklı kelimeler.
    Örnek: "listen" ve "silent"

    🧠 YAZILIMCI YAKLAŞIMI - 3 farklı çözüm düşünelim:

    YÖNTEM 1 (Naif): Her iki kelimeyi sırala, karşılaştır → O(n log n)
    YÖNTEM 2 (Akıllı): Harf frekanslarını say, karşılaştır → O(n)
    YÖNTEM 3 (Pythonic): Counter kullan → O(n), daha kısa

    Biz YÖNTEM 2'yi kullanacağız çünkü:
    → Nasıl çalıştığını anlamak önemli
    → Kendi hash map mantığımızı kurmayı öğretir
    """
    # Ön işleme: Boşlukları kaldır, küçük harfe çevir
    k1 = kelime1.replace(" ", "").lower()
    k2 = kelime2.replace(" ", "").lower()

    # Hızlı kontrol: Uzunluklar farklıysa kesinlikle anagram değil
    # NEDEN? → Gereksiz hesaplama yapmaktan kaçınmak (early return)
    # Bu "fail fast" prensibidir - mümkün olan en erken noktada reddet
    if len(k1) != len(k2):
        return False

    # Harf frekanslarını say
    frekans = {}

    # İlk kelime: Frekansları artır
    for harf in k1:
        frekans[harf] = frekans.get(harf, 0) + 1

    # İkinci kelime: Frekansları azalt
    for harf in k2:
        frekans[harf] = frekans.get(harf, 0) - 1

    # Tüm frekanslar 0 olmalı
    # NEDEN all() kullanıyoruz? → Tüm değerlerin bir koşulu sağlayıp
    # sağlamadığını kontrol etmek için en Pythonic yol
    return all(v == 0 for v in frekans.values())


print(f"\n🔤 Anagram Kontrolü:")
test_ciftleri = [
    ("listen", "silent"),
    ("Astronomer", "Moon starer"),
    ("hello", "world"),
    ("python", "typhon"),
    ("Dormitory", "Dirty room"),
]

for k1, k2 in test_ciftleri:
    sonuc = "✅ Evet" if anagram_mi(k1, k2) else "❌ Hayır"
    print(f"  '{k1}' & '{k2}' → {sonuc}")


# =============================================================================
# 📖 BÖLÜM 8: HATA YÖNETİMİ - SAVUNMACI PROGRAMLAMA
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
"Bir şeyler HER ZAMAN ters gidebilir."
İyi yazılımcı, hataları ÖNCEDEN düşünür ve yakalar.

HATA TÜRLERİ:
1. Syntax Error    : Yazım hatası (Python çalıştırmadan yakalar)
2. Runtime Error   : Çalışma anında oluşan hata (try/except ile yakala)
3. Logic Error     : Mantık hatası (en tehlikeli! Test ile bulunur)

SAVUNMACI PROGRAMLAMA İLKELERİ:
→ Hiçbir girdiye güvenme
→ Her şeyin yanlış gelebileceğini varsay
→ Hataları sessizce yutma, kaydet (log)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 8: HATA YÖNETİMİ")
print("=" * 70)


def guvenli_bolme(bolen, bolunen):
    """
    📝 PROBLEM: İki sayıyı güvenli bir şekilde böl.

    UÇ DURUMLAR:
    → Sıfıra bölme
    → Sayı olmayan girdi
    → None girdi
    → Sonsuzluk durumu
    """
    try:
        # Girdileri doğrula
        if bolen is None or bolunen is None:
            raise ValueError("Girdiler None olamaz!")

        bolen = float(bolen)
        bolunen = float(bolunen)

        if bolunen == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılamaz!")

        sonuc = bolen / bolunen
        return {"basarili": True, "sonuc": round(sonuc, 6)}

    except ValueError as e:
        return {"basarili": False, "hata": f"Değer hatası: {e}"}
    except ZeroDivisionError as e:
        return {"basarili": False, "hata": f"Bölme hatası: {e}"}
    except Exception as e:
        # Beklenmeyen hatalar için genel yakalayıcı
        return {"basarili": False, "hata": f"Beklenmeyen hata: {e}"}


print("\n🛡️ Güvenli Bölme:")
test_durumlari = [
    (10, 3),     # Normal
    (10, 0),     # Sıfıra bölme
    ("abc", 5),  # Geçersiz girdi
    (None, 5),   # None girdi
    (100, 7),    # Normal
]

for bolen, bolunen in test_durumlari:
    sonuc = guvenli_bolme(bolen, bolunen)
    if sonuc["basarili"]:
        print(f"  {bolen} / {bolunen} = {sonuc['sonuc']}")
    else:
        print(f"  {bolen} / {bolunen} → ⚠️ {sonuc['hata']}")


# --- Özel Hata Sınıfı (Custom Exception) ---
class YasHatasi(Exception):
    """
    NEDEN özel exception?
    → Hataları kategorize etmek ve anlamlı mesajlar vermek için
    → Kodun okunabilirliğini artırır
    → Farklı hata türlerini farklı şekilde handle edebilirsin
    """
    def __init__(self, yas, mesaj="Geçersiz yaş değeri"):
        self.yas = yas
        self.mesaj = mesaj
        super().__init__(self.mesaj)


def yas_dogrula(yas):
    """Yaşı doğrula ve kategorize et."""
    if not isinstance(yas, (int, float)):
        raise YasHatasi(yas, f"Yaş sayı olmalı, '{type(yas).__name__}' verildi")
    if yas < 0:
        raise YasHatasi(yas, f"Yaş negatif olamaz: {yas}")
    if yas > 150:
        raise YasHatasi(yas, f"Yaş gerçekçi değil: {yas}")

    if yas < 18:
        return "Çocuk/Genç"
    elif yas < 65:
        return "Yetişkin"
    else:
        return "Yaşlı"


print("\n🔒 Yaş Doğrulama:")
test_yaslari = [25, 10, 70, -5, 200, "abc", 0]
for yas in test_yaslari:
    try:
        kategori = yas_dogrula(yas)
        print(f"  Yaş {yas} → {kategori}")
    except YasHatasi as e:
        print(f"  Yaş {e.yas} → ⚠️ {e.mesaj}")


# =============================================================================
# 📖 BÖLÜM 9: NESNE YÖNELİMLİ PROGRAMLAMA (OOP)
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
OOP, gerçek dünyayı kod ile modellemektir.

4 TEMEL İLKE:
1. Encapsulation (Kapsülleme)  : Veriyi gizle, arayüz sun
2. Abstraction (Soyutlama)     : Karmaşıklığı gizle
3. Inheritance (Kalıtım)       : Kod tekrarını önle
4. Polymorphism (Çok Biçimlilik): Aynı arayüz, farklı davranış

NEDEN OOP?
→ Büyük projeleri yönetilebilir parçalara böler
→ Kodu yeniden kullanılabilir yapar
→ Gerçek dünya problemlerini doğal şekilde modeller
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 9: NESNE YÖNELİMLİ PROGRAMLAMA")
print("=" * 70)


class Hayvan:
    """
    Temel sınıf (Base class / Parent class)

    NEDEN temel sınıf?
    → Tüm hayvanların ortak özellikleri var (isim, yas, ses çıkarma)
    → Bu ortaklıkları tekrar tekrar yazmak yerine bir kez yazıp kalıtıyoruz
    """

    # Sınıf değişkeni: Tüm örnekler (instances) arasında paylaşılır
    toplam_hayvan = 0

    def __init__(self, isim, yas, tur):
        """
        __init__ = Constructor (Yapıcı metot)
        Her yeni hayvan oluşturulduğunda otomatik çalışır.

        self nedir?
        → O anki nesneyi temsil eder
        → self.isim = "Bu nesnenin ismi"
        → isim (self'siz) = Sadece fonksiyon parametresi
        """
        # Instance değişkenleri: Her nesneye özel
        self.isim = isim
        self.yas = yas
        self.tur = tur
        self._saglik = 100  # _ ile başlayan = "lütfen dışarıdan değiştirme" sinyali
        # (Python'da gerçek private yoktur, convention'dır)

        # Sınıf değişkenini güncelle
        Hayvan.toplam_hayvan += 1

    def ses_cikar(self):
        """
        Bu metot alt sınıflarda override (geçersiz kılma) edilecek.
        Polymorphism burada devreye girer!
        """
        return "..."

    def bilgi(self):
        """Hayvan bilgilerini döndür."""
        return f"{self.isim} ({self.tur}, {self.yas} yaş) - Sağlık: {self._saglik}%"

    @property
    def saglik(self):
        """
        @property dekoratörü:
        → Metodu özellik gibi kullanmamızı sağlar
        → hayvan.saglik() yerine hayvan.saglik yazarız
        → Getter/Setter pattern'ı ile veri koruması sağlar

        NEDEN property?
        → Sağlık değerini 0-100 arasında tutmak istiyoruz
        → Direkt erişime izin verirsek hayvan._saglik = -50 yapabilirler
        → Property ile kontrol mekanizması ekleriz
        """
        return self._saglik

    @saglik.setter
    def saglik(self, deger):
        """Sağlık değerini güvenli şekilde ayarla."""
        if deger < 0:
            self._saglik = 0
        elif deger > 100:
            self._saglik = 100
        else:
            self._saglik = deger

    def __str__(self):
        """
        __str__ = String representation
        print(hayvan) dediğimizde ne gösterileceğini belirler.
        Dunder (double underscore) metotları = magic methods
        Python'un özel davranışlarını özelleştirmemizi sağlar.
        """
        return f"🐾 {self.isim} ({self.tur})"

    def __repr__(self):
        """
        __repr__ = Geliştirici için temsil
        Debug ederken görünen, tekrar oluşturulabilir string.
        """
        return f"Hayvan(isim='{self.isim}', yas={self.yas}, tur='{self.tur}')"


class Kedi(Hayvan):
    """
    Alt sınıf (Child class) - Hayvan'dan kalıtım alır.

    NEDEN kalıtım?
    → Kedi bir hayvandır (IS-A ilişkisi)
    → Hayvan'ın tüm özelliklerini alır + kendi özelliklerini ekler
    → Kod tekrarı sıfır!
    """

    def __init__(self, isim, yas, ic_mekan=True):
        # super() ile üst sınıfın __init__'ini çağır
        # NEDEN super()? → Üst sınıfın yapıcısını manuel çağırmak yerine
        # Python'un MRO (Method Resolution Order) mekanizmasını kullanır
        super().__init__(isim, yas, tur="Kedi")
        self.ic_mekan = ic_mekan  # Kediye özel özellik

    def ses_cikar(self):
        """Polymorphism: Hayvan.ses_cikar() override edildi."""
        return "Miyav! 🐱"

    def tirmalama(self):
        """Kediye özel davranış."""
        return f"{self.isim} mobilyayı tırmalıyor! 😼"


class Kopek(Hayvan):
    """Köpek sınıfı."""

    def __init__(self, isim, yas, cins="Melez"):
        super().__init__(isim, yas, tur="Köpek")
        self.cins = cins

    def ses_cikar(self):
        return "Hav hav! 🐕"

    def getir(self, nesne="top"):
        return f"{self.isim} {nesne}'u getiriyor! 🎾"


class Kus(Hayvan):
    """Kuş sınıfı."""

    def __init__(self, isim, yas, ucabiliyor=True):
        super().__init__(isim, yas, tur="Kuş")
        self.ucabiliyor = ucabiliyor

    def ses_cikar(self):
        return "Cik cik! 🐦"


# OOP kullanımı
print("\n🐾 Hayvanlar:")
hayvanlar = [
    Kedi("Pamuk", 3),
    Kopek("Karabaş", 5, "Golden Retriever"),
    Kus("Maviş", 2),
    Kedi("Tekir", 7, ic_mekan=False),
    Kopek("Rex", 4, "Alman Çoban"),
]

for hayvan in hayvanlar:
    # Polymorphism burada! Her hayvan kendi ses_cikar() metodunu çağırır
    print(f"  {hayvan} → {hayvan.ses_cikar()}")

print(f"\n  Toplam hayvan sayısı: {Hayvan.toplam_hayvan}")

# Property örneği
kedi = hayvanlar[0]
print(f"\n  {kedi.isim}'un sağlığı: {kedi.saglik}")
kedi.saglik = -10  # Property setter devreye girer
print(f"  -10 atandı ama: {kedi.saglik}")  # 0 olur (koruma çalıştı)
kedi.saglik = 85
print(f"  85 atandı: {kedi.saglik}")


# =============================================================================
# 📖 BÖLÜM 10: DOSYA İŞLEMLERİ VE VERİ KALICILIĞI
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Programlar kapandığında bellekteki veriler kaybolur.
Verileri kalıcı yapmak için dosyalara yazmalıyız.

DOSYA İŞLEMLERİ GÜVENLİK KURALLARI:
1. Her zaman 'with' bloğu kullan (dosyayı otomatik kapatır)
2. Encoding belirt (UTF-8 standart)
3. Dosya var mı kontrol et
4. Yazma işleminde veri kaybına dikkat et
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 10: DOSYA İŞLEMLERİ")
print("=" * 70)

import json
import os


def veri_kaydet(dosya_adi, veri):
    """
    JSON formatında veri kaydet.

    NEDEN JSON?
    → İnsan okunabilir
    → Dil bağımsız (her programlama dili destekler)
    → Web'in standart veri formatı
    → Python dict/list ile doğal uyum
    """
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            # ensure_ascii=False → Türkçe karakterler düzgün yazılsın
            # indent=2 → Güzel formatlanmış (okunabilir) JSON
            json.dump(veri, dosya, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"  ⚠️ Dosya yazma hatası: {e}")
        return False


def veri_oku(dosya_adi):
    """JSON dosyasından veri oku."""
    try:
        if not os.path.exists(dosya_adi):
            return None

        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            return json.load(dosya)
    except json.JSONDecodeError as e:
        print(f"  ⚠️ JSON parse hatası: {e}")
        return None
    except IOError as e:
        print(f"  ⚠️ Dosya okuma hatası: {e}")
        return None


# Örnek: Ayarlar dosyası
ayarlar = {
    "uygulama": "Python Rehberi",
    "versiyon": "1.0",
    "tema": "koyu",
    "dil": "tr",
    "son_acilis": "2026-03-02",
    "kullanici": {
        "isim": "Abdulkadir",
        "seviye": "başlangıç",
        "tamamlanan_bolumler": [1, 2, 3, 4, 5]
    }
}

dosya_adi = "rehber_ayarlar.json"
if veri_kaydet(dosya_adi, ayarlar):
    print(f"\n  ✅ Ayarlar '{dosya_adi}' dosyasına kaydedildi")
    okunan = veri_oku(dosya_adi)
    if okunan:
        print(f"  ✅ Okunan: {json.dumps(okunan, ensure_ascii=False, indent=4)}")

    # Temizlik
    os.remove(dosya_adi)
    print(f"  🗑️ Test dosyası temizlendi")


# =============================================================================
# 📖 BÖLÜM 11: GERÇEK HAYAT PROJESİ - MİNİ BANKA SİSTEMİ
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Şimdi öğrendiğimiz HER ŞEYİ birleştirerek gerçek bir proje yapalım.
Bu proje şunları kullanır:
→ OOP (sınıflar, kalıtım)
→ Veri yapıları (dict, list)
→ Hata yönetimi (try/except)
→ Fonksiyonlar
→ Algoritma (arama, sıralama)
→ Kontrol akışı

BU PROJENİN SENİ İYİ YAZILIMCI YAPAN YÖNÜ:
→ Bir sistemi baştan tasarlayabilmek
→ Sınıflar arası ilişkileri kurabilmek
→ Her şeyi bir arada düşünebilmek
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 11: MİNİ BANKA SİSTEMİ")
print("=" * 70)

from datetime import datetime


class IslemTuru:
    """
    Sabit değerler için sınıf (Enum alternatifi).
    NEDEN? → Yazım hatalarını önler.
    "yatirma" yerine yanlışlıkla "yatırma" yazarsan hata almaz ama bug olur!
    Sabitleri merkezi bir yerde tanımlayarak bu riski azaltıyoruz.
    """
    YATIRMA = "yatirma"
    CEKME = "cekme"
    TRANSFER = "transfer"


class Islem:
    """Bir bankacılık işlemini temsil eder."""

    def __init__(self, tur, tutar, aciklama="", bakiye_sonrasi=0):
        self.tur = tur
        self.tutar = tutar
        self.aciklama = aciklama
        self.bakiye_sonrasi = bakiye_sonrasi
        self.tarih = datetime.now()

    def __str__(self):
        isaret = "+" if self.tur == IslemTuru.YATIRMA else "-"
        return (f"  [{self.tarih.strftime('%H:%M:%S')}] "
                f"{isaret}{self.tutar:,.2f} TL "
                f"({self.aciklama}) "
                f"→ Bakiye: {self.bakiye_sonrasi:,.2f} TL")


class BankaHesabi:
    """
    Banka hesabı sınıfı.

    DİZAYN KARARLARI:
    → _bakiye private: Direkt değiştirilemez (para güvenliği!)
    → İşlem geçmişi tutulur: Audit trail (denetim izi)
    → Her işlemde doğrulama yapılır
    → Thread-safe değil (gerçek bankada mutex/lock kullanılır)
    """

    # Sınıf değişkeni: Hesap numarası üreteci
    _sonraki_hesap_no = 1000

    def __init__(self, sahip_ismi, baslangic_bakiye=0):
        BankaHesabi._sonraki_hesap_no += 1
        self.hesap_no = BankaHesabi._sonraki_hesap_no
        self.sahip = sahip_ismi
        self._bakiye = 0  # Başlangıçta sıfır
        self._islem_gecmisi = []  # İşlem kaydı
        self._aktif = True

        # Başlangıç bakiyesi varsa yatır (işlem kaydı oluşsun diye)
        if baslangic_bakiye > 0:
            self.para_yatir(baslangic_bakiye, "Hesap açılış bakiyesi")

    @property
    def bakiye(self):
        """Bakiyeyi oku (sadece okunabilir)."""
        return self._bakiye

    def para_yatir(self, tutar, aciklama="Para yatırma"):
        """
        Hesaba para yatır.

        YAZILIMCI DÜŞÜNCESİ:
        → Tutarın pozitif olduğunu doğrula
        → Hesabın aktif olduğunu kontrol et
        → İşlemi kaydet
        → Başarılı/başarısız sonuç döndür
        """
        # Doğrulamalar
        if not self._aktif:
            return {"basarili": False, "mesaj": "Hesap kapalı!"}
        if tutar <= 0:
            return {"basarili": False, "mesaj": "Tutar pozitif olmalı!"}

        # İşlemi gerçekleştir
        self._bakiye += tutar

        # İşlem kaydı oluştur
        islem = Islem(IslemTuru.YATIRMA, tutar, aciklama, self._bakiye)
        self._islem_gecmisi.append(islem)

        return {"basarili": True, "mesaj": f"{tutar:,.2f} TL yatırıldı",
                "yeni_bakiye": self._bakiye}

    def para_cek(self, tutar, aciklama="Para çekme"):
        """
        Hesaptan para çek.

        UÇ DURUMLAR:
        → Bakiye yetersiz olabilir
        → Hesap kapalı olabilir
        → Tutar negatif olabilir
        """
        if not self._aktif:
            return {"basarili": False, "mesaj": "Hesap kapalı!"}
        if tutar <= 0:
            return {"basarili": False, "mesaj": "Tutar pozitif olmalı!"}
        if tutar > self._bakiye:
            return {"basarili": False,
                    "mesaj": f"Yetersiz bakiye! Mevcut: {self._bakiye:,.2f} TL"}

        self._bakiye -= tutar

        islem = Islem(IslemTuru.CEKME, tutar, aciklama, self._bakiye)
        self._islem_gecmisi.append(islem)

        return {"basarili": True, "mesaj": f"{tutar:,.2f} TL çekildi",
                "yeni_bakiye": self._bakiye}

    def transfer(self, hedef_hesap, tutar):
        """
        Başka bir hesaba transfer.

        ATOMIK İŞLEM PRENSİBİ:
        → Ya ikisi de olur, ya ikisi de olmaz
        → Para çekildi ama yatırılamadı → Geri al!
        → Gerçek bankalarda buna "transaction" denir
        """
        if not isinstance(hedef_hesap, BankaHesabi):
            return {"basarili": False, "mesaj": "Geçersiz hedef hesap!"}
        if hedef_hesap.hesap_no == self.hesap_no:
            return {"basarili": False, "mesaj": "Kendine transfer yapılamaz!"}

        # Adım 1: Para çek
        cekme_sonuc = self.para_cek(
            tutar, f"Transfer → Hesap #{hedef_hesap.hesap_no}")

        if not cekme_sonuc["basarili"]:
            return cekme_sonuc

        # Adım 2: Karşı hesaba yatır
        yatirma_sonuc = hedef_hesap.para_yatir(
            tutar, f"Transfer ← Hesap #{self.hesap_no}")

        if not yatirma_sonuc["basarili"]:
            # GERİ AL! Yatırma başarısız olduysa çekilen parayı iade et
            self.para_yatir(tutar, "Transfer iadesi")
            return {"basarili": False, "mesaj": "Transfer başarısız, iade edildi!"}

        return {"basarili": True,
                "mesaj": f"{tutar:,.2f} TL → Hesap #{hedef_hesap.hesap_no}"}

    def hesap_ozeti(self):
        """Hesap özetini göster."""
        print(f"\n  {'═' * 50}")
        print(f"  📋 HESAP ÖZETİ")
        print(f"  {'═' * 50}")
        print(f"  Hesap No : #{self.hesap_no}")
        print(f"  Sahip    : {self.sahip}")
        print(f"  Bakiye   : {self._bakiye:,.2f} TL")
        print(f"  Durum    : {'✅ Aktif' if self._aktif else '❌ Kapalı'}")
        print(f"  İşlem    : {len(self._islem_gecmisi)} işlem")

        if self._islem_gecmisi:
            print(f"\n  📜 Son İşlemler:")
            # Son 5 işlemi göster
            for islem in self._islem_gecmisi[-5:]:
                print(f"  {islem}")
        print(f"  {'═' * 50}")


# Mini Banka Sistemi Demo
print("\n🏦 Mini Banka Sistemi Demo:")

# Hesap oluştur
hesap_ali = BankaHesabi("Ali Yılmaz", 5000)
hesap_ayse = BankaHesabi("Ayşe Kara", 3000)

# İşlemler
print("\n  📌 İşlemler gerçekleştiriliyor...")
sonuclar = [
    hesap_ali.para_yatir(2000, "Maaş"),
    hesap_ali.para_cek(500, "Market alışverişi"),
    hesap_ali.transfer(hesap_ayse, 1500),
    hesap_ali.para_cek(100000, "Büyük çekim"),  # Yetersiz bakiye
    hesap_ali.para_cek(-500, "Negatif tutar"),   # Geçersiz
]

for s in sonuclar:
    durum = "✅" if s["basarili"] else "❌"
    print(f"  {durum} {s['mesaj']}")

# Hesap özetleri
hesap_ali.hesap_ozeti()
hesap_ayse.hesap_ozeti()


# =============================================================================
# 📖 BÖLÜM 12: KARMAŞIKLIK ANALİZİ (BIG-O) VE PERFORMANS
# =============================================================================
"""
🧠 YAZILIMCI BAKIŞ AÇISI:
Bir algoritmanın "iyi" olup olmadığını nasıl ölçeriz?
→ Big-O Notasyonu ile!

Big-O, girdi boyutu büyüdükçe algoritmanın ne kadar
yavaşlayacağını tahmin eder.

YAYGIN KARMAŞIKLIKLAR (En iyiden en kötüye):
┌──────────────┬─────────────────┬──────────────────────────────┐
│ Karmaşıklık  │ İsim            │ 1 milyon eleman              │
├──────────────┼─────────────────┼──────────────────────────────┤
│ O(1)         │ Sabit           │ 1 işlem                      │
│ O(log n)     │ Logaritmik      │ ~20 işlem                    │
│ O(n)         │ Doğrusal        │ 1.000.000 işlem              │
│ O(n log n)   │ Lin-logaritmik  │ ~20.000.000 işlem            │
│ O(n²)        │ Karesel         │ 1.000.000.000.000 işlem 😱   │
│ O(2^n)       │ Üstel           │ ... EVREN YETMEZ 🌌          │
└──────────────┴─────────────────┴──────────────────────────────┘

ALTIN KURAL: "Önce doğru çalıştır, sonra hızlı çalıştır."
(Ama en baştan iyi tasarlamak her zaman daha iyidir!)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 12: BIG-O KARMAŞIKLIK ANALİZİ")
print("=" * 70)


def karmasiklik_goster():
    """Farklı karmaşıklıkların pratikte ne anlama geldiğini göster."""

    import math

    n_degerleri = [10, 100, 1_000, 10_000, 100_000]

    print(f"\n  {'n':>10} | {'O(1)':>10} | {'O(log n)':>10} | "
          f"{'O(n)':>12} | {'O(n log n)':>14} | {'O(n²)':>18}")
    print(f"  {'-' * 85}")

    for n in n_degerleri:
        o_1 = 1
        o_logn = int(math.log2(n))
        o_n = n
        o_nlogn = int(n * math.log2(n))
        o_n2 = n * n

        print(f"  {n:>10,} | {o_1:>10,} | {o_logn:>10,} | "
              f"{o_n:>12,} | {o_nlogn:>14,} | {o_n2:>18,}")


karmasiklik_goster()


# Pratik Karmaşıklık Örnekleri
print("\n📊 Pratik Örnekler:")


def ornek_o1(liste):
    """O(1) - Sabit zaman: Girdi boyutundan bağımsız."""
    # Liste ne kadar büyük olursa olsun, ilk elemana erişim sabit sürer
    return liste[0] if liste else None


def ornek_on(liste):
    """O(n) - Doğrusal zaman: Her eleman bir kez ziyaret edilir."""
    toplam = 0
    for eleman in liste:  # n kez döner
        toplam += eleman
    return toplam


def ornek_on2(liste):
    """O(n²) - Karesel zaman: İç içe iki döngü."""
    # Her eleman diğer tüm elemanlarla karşılaştırılır
    ciftler = 0
    for i in range(len(liste)):         # n kez
        for j in range(i + 1, len(liste)):  # ortalama n/2 kez
            if liste[i] + liste[j] == 10:
                ciftler += 1
    return ciftler


# Performans ölçümü
boyutlar = [1000, 5000, 10000]
print(f"\n  {'Boyut':>8} | {'O(1)':>12} | {'O(n)':>12} | {'O(n²)':>12}")
print(f"  {'-' * 55}")

for boyut in boyutlar:
    test_liste = list(range(boyut))

    # O(1) ölçümü
    baslangic = time.perf_counter()
    for _ in range(10000):
        ornek_o1(test_liste)
    sure_o1 = (time.perf_counter() - baslangic) / 10000

    # O(n) ölçümü
    baslangic = time.perf_counter()
    ornek_on(test_liste)
    sure_on = time.perf_counter() - baslangic

    # O(n²) ölçümü
    baslangic = time.perf_counter()
    ornek_on2(test_liste[:min(boyut, 2000)])  # n²'yi sınırla yoksa çok uzun sürer
    sure_on2 = time.perf_counter() - baslangic

    print(f"  {boyut:>8,} | {sure_o1:>10.8f}s | {sure_on:>10.6f}s | {sure_on2:>10.4f}s")


# =============================================================================
# 🎯 SONUÇ VE TAVSİYELER
# =============================================================================
print("\n" + "=" * 70)
print("🎯 SONUÇ: İYİ BİR YAZILIMCI OLMAK İÇİN YOL HARİTASI")
print("=" * 70)

yol_haritasi = """
📍 ADIM 1: TEMELLER (1-2 ay)
   □ Python söz dizimi (syntax)
   □ Değişkenler ve veri tipleri
   □ Kontrol akışı (if/elif/else)
   □ Döngüler (for, while)
   □ Fonksiyonlar
   → Bu dosyadaki Bölüm 2-5'i çalış

📍 ADIM 2: VERİ YAPILARI (2-3 ay)
   □ Liste, Tuple, Set, Dictionary
   □ Stack, Queue, Linked List
   □ Hash Table nasıl çalışır
   □ Tree ve Graph temelleri
   → Bu dosyadaki Bölüm 6'yı çalış

📍 ADIM 3: ALGORİTMALAR (2-3 ay)
   □ Arama algoritmaları (Linear, Binary)
   □ Sıralama algoritmaları (Bubble, Merge, Quick)
   □ Greedy yaklaşım
   □ Dynamic Programming temelleri
   □ Recursion (Özyineleme)
   → Bu dosyadaki Bölüm 7'yi çalış

📍 ADIM 4: OOP ve TASARIM (1-2 ay)
   □ Sınıflar ve Nesneler
   □ Kalıtım, Kapsülleme, Polymorphism
   □ SOLID prensipleri (araştır!)
   □ Design Patterns temelleri
   → Bu dosyadaki Bölüm 9'u çalış

📍 ADIM 5: GERÇEK PROJELER (Sürekli)
   □ Mini projeler yap (hesap makinesi, to-do app, vs.)
   □ GitHub'da kod paylaş
   □ Başkalarının kodunu oku
   □ LeetCode / HackerRank'te algoritma çöz
   → Bu dosyadaki Bölüm 11'i çalış ve genişlet

📍 ADIM 6: UZMANLIK ALANI SEÇ
   □ Web Geliştirme (Django, Flask)
   □ Veri Bilimi (Pandas, NumPy)
   □ Yapay Zeka (TensorFlow, PyTorch)
   □ Mobil Uygulama (Kivy, React Native)
   □ DevOps (Docker, CI/CD)
   □ Oyun Geliştirme (Pygame)

🏆 SENİ "GERÇEK SORUN ÇÖZÜCÜ" YAPAN ŞEYLER:
   ✅ Bir problemi parçalara ayırabilmek (Decomposition)
   ✅ Doğru veri yapısını seçebilmek
   ✅ Algoritma karmaşıklığını anlayabilmek
   ✅ Uç durumları (edge cases) düşünebilmek
   ✅ Temiz ve okunabilir kod yazabilmek
   ✅ Hataları önceden tahmin edip yönetebilmek
   ✅ Test yazmayı alışkanlık haline getirmek
   ✅ Başkasının kodunu okuyup anlayabilmek
   ✅ Sürekli öğrenmeye açık olmak

💡 SON SÖZ:
   "Programlama bir dil öğrenmek değil, düşünmeyi öğrenmektir."
   "Mükemmel kodu değil, çalışan kodu hedefle. Sonra iyileştir."
   "Her gün 1 saat kod yaz. 1 yılda hayal edemeyeceğin yerde olursun."
"""

print(yol_haritasi)

print("=" * 70)
print("✨ Bu rehberi çalıştırarak tüm örnekleri görebilirsin!")
print("   python yazilimci_rehberi.py")
print("=" * 70)