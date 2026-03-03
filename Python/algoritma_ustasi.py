# ╔════════════════════════════════════════════���═════════════════════════════════╗
# ║                                                                              ║
# ║   🧠 ALGORİTMA USTASI OLMA REHBERİ                                          ║
# ║   "Algoritma mantığı güçlü olan, her dilde güçlüdür."                       ║
# ║                                                                              ║
# ║   Bu dosya seni şu konularda uzmanlaştıracak:                               ║
# ║   → Algoritma tasarlama zihniyeti                                            ║
# ║   → 5 temel algoritma stratejisi                                             ║
# ║   → Fonksiyon tasarlama sanatı                                               ║
# ║   → Recursion (özyineleme) - derinlemesine                                   ║
# ║   → Two Pointer tekniği                                                      ║
# ║   → Sliding Window tekniği                                                   ║
# ║   → Dynamic Programming (baştan sona)                                        ║
# ║   → Backtracking (geri izleme)                                               ║
# ║   → Graph düşüncesi                                                          ║
# ║                                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

import time
from typing import List, Optional, Dict, Tuple

# =============================================================================
# 📌 İÇİNDEKİLER
# =============================================================================
# BÖLÜM 1  : Algoritmik Düşüncenin 5 Altın Kuralı
# BÖLÜM 2  : Fonksiyon Tasarlama Sanatı (İleri Seviye)
# BÖLÜM 3  : Recursion - Kendi Kendini Çağıran Fonksiyonlar
# BÖLÜM 4  : Two Pointer (İki İşaretçi) Tekniği
# BÖLÜM 5  : Sliding Window (Kayan Pencere) Tekniği
# BÖLÜM 6  : Greedy (Açgözlü) Algoritma - Derinlemesine
# BÖLÜM 7  : Divide & Conquer (Böl ve Fethet)
# BÖLÜM 8  : Dynamic Programming (Dinamik Programlama) ★★★
# BÖLÜM 9  : Backtracking (Geri İzleme) ★★
# BÖLÜM 10 : Graph Düşüncesi (BFS & DFS) ★★★
# BÖLÜM 11 : Hash Map Düşüncesi ★★★
# BÖLÜM 12 : Gerçek Mülakat Soruları ve Çözüm Stratejileri
# =============================================================================


# =============================================================================
# 📖 BÖLÜM 1: ALGORİTMİK DÜŞÜNCENİN 5 ALTIN KURALI
# =============================================================================
"""
🧠 BİR PROBLEMI GÖRDÜĞÜNDE KAFANDA ŞUNLAR DÖNMELI:

KURAL 1: "ÖNCE ANLA, SONRA ÇÖZ"
─────────────────────────────────
→ Problemi kendi cümlelerinle tekrar ifade et
→ Girdiler ne? Çıktılar ne? Kısıtlar ne?
→ En küçük örnekle elle çöz
→ KODLAMA EN SON ADIM!

KURAL 2: "BRUTE FORCE İLE BAŞLA"
─────────────────────────────────
→ İlk çözümün kötü olsun, sorun değil
→ Çalışan kötü çözüm > Çalışmayan güzel çözüm
→ Sonra "Bunu nasıl iyileştirebilirim?" diye sor

KURAL 3: "KALIP TANI"
─────────────────────
→ "Bu problemi daha önce gördüm mü?"
→ "Hangi teknik burada işe yarar?"
→ Bu rehberdeki teknikleri öğrendikçe kalıpları tanıyacaksın

KURAL 4: "UÇ DURUMLARI DÜŞÜN"
──────────────────────────────
→ Boş girdi gelirse?
→ Tek elemanlı gelirse?
→ Tüm elemanlar aynıysa?
→ Negatif sayılar gelirse?
→ Çok büyük girdi gelirse?

KURAL 5: "KARMAŞIKLIĞI BİL"
────────────────────────────
→ Çözümün ne kadar zaman alır? (Time Complexity)
→ Ne kadar bellek kullanır? (Space Complexity)
→ Daha iyisi var mı?

📌 HER PROBLEMİ ÇÖZERKEN BU ADIMLARI UYGULA:
   1. Anla → 2. Örnekle → 3. Brute force → 4. Optimize et → 5. Kodla → 6. Test et
"""

print("=" * 70)
print("🧠 ALGORİTMA USTASI OLMA REHBERİ")
print("=" * 70)


# =============================================================================
# 📖 BÖLÜM 2: FONKSİYON TASARLAMA SANATI (İLERİ SEVİYE)
# =============================================================================
"""
🧠 FONKSİYON = ALGORİTMANIN YAPITAŞI

Bir fonksiyon yazarken kafanda şu 6 soru olmalı:
1. Bu fonksiyon TAM OLARAK ne yapıyor? (Tek sorumluluk)
2. Hangi girdileri alıyor? (Parametreler)
3. Ne döndürüyor? (Return değeri)
4. Hata durumunda ne olacak? (Error handling)
5. Yeniden kullanılabilir mi? (Reusability)
6. Test edilebilir mi? (Testability)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 2: FONKSİYON TASARLAMA SANATI")
print("=" * 70)


# --- İLKE 1: Fonksiyon TEK BİR İŞ Yapsın ---

# ❌ KÖTÜ: Her şeyi tek fonksiyonda yapma
def kullanici_islemleri_kotu(isim, yas, islem):
    """Bu fonksiyon çok fazla iş yapıyor - bakımı ve testi zor."""
    if islem == "dogrula":
        if not isim or len(isim) < 2:
            return "Geçersiz isim"
        if yas < 0 or yas > 150:
            return "Geçersiz yaş"
        return "Geçerli"
    elif islem == "formatla":
        return f"{isim.title()} ({yas})"
    elif islem == "kategori":
        if yas < 18:
            return "çocuk"
        elif yas < 65:
            return "yetişkin"
        return "yaşlı"


# ✅ İYİ: Her fonksiyon tek bir iş yapsın
def isim_dogrula(isim: str) -> bool:
    """
    Sadece ismi doğrular. Başka hiçbir şey yapmaz.

    NEDEN böyle?
    → Test etmesi kolay: isim_dogrula("") → False, isim_dogrula("Ali") → True
    → Başka yerlerde de kullanılabilir
    → Değiştirirken sadece burayı değiştirirsin
    → Adı ne yaptığını anlatıyor (Self-documenting code)
    """
    if not isinstance(isim, str):
        return False
    isim = isim.strip()
    return len(isim) >= 2


def yas_dogrula(yas: int) -> bool:
    """Sadece yaşı doğrular."""
    return isinstance(yas, (int, float)) and 0 <= yas <= 150


def yas_kategorisi(yas: int) -> str:
    """Sadece yaş kategorisini döndürür."""
    if yas < 13:
        return "çocuk"
    elif yas < 18:
        return "genç"
    elif yas < 65:
        return "yetişkin"
    return "yaşlı"


def kullanici_formatla(isim: str, yas: int) -> str:
    """Sadece formatlar."""
    return f"{isim.title()} ({yas} yaş, {yas_kategorisi(yas)})"


# Test et
print("\n✅ Tek Sorumluluk Prensibi:")
print(f"  isim_dogrula('Ali')  = {isim_dogrula('Ali')}")
print(f"  isim_dogrula('')     = {isim_dogrula('')}")
print(f"  yas_dogrula(25)      = {yas_dogrula(25)}")
print(f"  yas_dogrula(-5)      = {yas_dogrula(-5)}")
print(f"  yas_kategorisi(25)   = {yas_kategorisi(25)}")
print(f"  formatla             = {kullanici_formatla('abdulkadir', 25)}")


# --- İLKE 2: Pure Functions (Saf Fonksiyonlar) ---
"""
🧠 SAF FONKSİYON NEDİR?
→ Aynı girdiye HER ZAMAN aynı çıktıyı verir
→ Dış dünyayı DEĞİŞTİRMEZ (yan etkisi yok)
→ Dış dünyaya BAĞIMLI DEĞİLDİR

NEDEN ÖNEMLİ?
→ Debug etmesi çok kolay (girdi-çıktı ilişkisi açık)
→ Test etmesi çok kolay
→ Paralel çalıştırılabilir (thread-safe)
→ Önbelleğe alınabilir (memoization)
"""

# ❌ SAF DEĞİL: Dış değişkene bağımlı ve onu değiştiriyor
toplam_islem = 0  # Global değişken


def islem_yap_kotu(sayi):
    global toplam_islem
    toplam_islem += 1  # Dış dünyayı değiştiriyor! (yan etki)
    return sayi * toplam_islem  # Sonuç her çağrıda farklı!


# ✅ SAF: Sadece girdilerine bağlı, her zaman aynı sonuç
def kare_al(sayi: float) -> float:
    """
    Saf fonksiyon örneği.
    kare_al(5) HER ZAMAN 25 döner. Hiçbir dış etken bunu değiştiremez.
    """
    return sayi ** 2


def toplam_hesapla(sayilar: list) -> float:
    """Saf fonksiyon: Listeyi değiştirmez, sadece sonuç döndürür."""
    return sum(sayilar)


# --- İLKE 3: Higher-Order Functions (Yüksek Seviye Fonksiyonlar) ---
"""
🧠 HIGHER-ORDER FUNCTION NEDİR?
→ Parametre olarak fonksiyon alan veya fonksiyon döndüren fonksiyon
→ Bu, kodun esnekliğini AŞIRI artırır
→ "Strateji" yi dışarıdan geçirebilirsin

BU NEDEN ÇOK ÖNEMLİ?
→ Aynı yapıyı farklı davranışlarla kullanabilirsin
→ Kod tekrarını minimize eder
→ Python'un map, filter, sorted hepsi bu mantıkla çalışır
"""

print("\n🔧 Higher-Order Functions:")


def liste_isle(liste: list, islem) -> list:
    """
    Listedeki her elemana verilen işlemi uygula.

    NEDEN böyle yazıyoruz?
    → islem parametresi bir FONKSİYON
    → liste_isle fonksiyonunu DEĞİŞTİRMEDEN farklı işlemler yapabiliriz
    → Bu "Open/Closed Principle" dir: Değişikliğe kapalı, genişlemeye açık
    """
    return [islem(eleman) for eleman in liste]


def filtrele(liste: list, kosul) -> list:
    """Koşulu sağlayan elemanları filtrele."""
    return [eleman for eleman in liste if kosul(eleman)]


# Kullanım - Tek bir fonksiyon, farklı davranışlar!
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kareler = liste_isle(sayilar, lambda x: x ** 2)
kupler = liste_isle(sayilar, lambda x: x ** 3)
ciftler = filtrele(sayilar, lambda x: x % 2 == 0)
buyukler = filtrele(sayilar, lambda x: x > 5)

print(f"  Orijinal : {sayilar}")
print(f"  Kareler  : {kareler}")
print(f"  Küpler   : {kupler}")
print(f"  Çiftler  : {ciftler}")
print(f"  >5 olanlar: {buyukler}")


# --- İLKE 4: Closure ve Fonksiyon Fabrikası ---
def carpan_olustur(carpan):
    """
    Fonksiyon döndüren fonksiyon (Closure).

    🧠 NE İŞE YARAR?
    → Bir değeri "hatırlayan" fonksiyonlar oluşturur
    → Fabrika gibi: "3 ile çarpan bir fonksiyon üret"
    → Her çağrıda yeni ama özelleştirilmiş fonksiyon döner

    GERÇEK DÜNYA: Vergi hesaplayıcı fabrikası
    → %18 KDV hesaplayıcı üret
    → %8 KDV hesaplayıcı üret
    → İkisi de aynı mantıkla çalışır ama farklı oranla
    """
    def carp(sayi):
        return sayi * carpan  # 'carpan' dış fonksiyondan hatırlanır!
    return carp


ikiyle_carp = carpan_olustur(2)
ucle_carp = carpan_olustur(3)
kdv_hesapla = carpan_olustur(1.18)   # %18 KDV

print(f"\n  2 ile çarp(5) = {ikiyle_carp(5)}")
print(f"  3 ile çarp(5) = {ucle_carp(5)}")
print(f"  KDV ekle(100) = {kdv_hesapla(100)}")


# --- İLKE 5: Decorator (Dekoratör) ---
"""
🧠 DECORATOR NEDİR?
→ Bir fonksiyonun DAVRANIŞINI değiştirmeden EKLEME yapar
→ Fonksiyonu "sarar" (wrap eder)
→ Loglama, süre ölçme, yetki kontrolü gibi "ek işler" için kullanılır

NEDEN DECORATOR?
→ Asıl fonksiyon temiz kalır (tek işe odaklanır)
→ Ek davranışı istediğin fonksiyona takıp çıkarabilirsin
→ DRY prensibi: Her fonksiyona ayrı ayrı süre ölçme kodu yazmak yerine
  bir decorator yaz, istediğin yere tak
"""


def sure_olc(fonksiyon):
    """
    Fonksiyonun çalışma süresini ölçen decorator.

    Bu decorator'ı herhangi bir fonksiyona @sure_olc yazarak ekleyebilirsin.
    Fonksiyonun kendisi değişmez, sadece ek özellik kazanır.
    """
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"  ⏱️ {fonksiyon.__name__}() → {sure:.6f} saniye")
        return sonuc
    return sarmalayici


def log_yaz(fonksiyon):
    """Fonksiyon çağrılarını loglayan decorator."""
    def sarmalayici(*args, **kwargs):
        print(f"  📝 {fonksiyon.__name__} çağrıldı: args={args}")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"  📝 {fonksiyon.__name__} sonuç: {sonuc}")
        return sonuc
    return sarmalayici


@sure_olc  # ← Bu sat��r: toplam_bul = sure_olc(toplam_bul) ile aynı şey
def toplam_bul(n):
    """1'den n'e kadar toplam."""
    return sum(range(1, n + 1))


@log_yaz
@sure_olc  # Decorator'lar zincirlenir! Önce sure_olc, sonra log_yaz çalışır
def faktoriyel(n):
    """n! hesapla."""
    sonuc = 1
    for i in range(2, n + 1):
        sonuc *= i
    return sonuc


print("\n🎭 Decorator Örnekleri:")
toplam_bul(1_000_000)
print()
faktoriyel(10)


# =============================================================================
# 📖 BÖLÜM 3: RECURSION (ÖZYİNELEME) - DERİNLEMESİNE
# =============================================================================
"""
🧠 RECURSİON NEDİR?
→ Bir fonksiyonun KENDİ KENDİNİ çağırması
→ "Büyük problemi aynı türdeki küçük probleme indirgeme" tekniği

RECURSION'U ANLAMAK İÇİN 3 SORU SOR:
1. TABAN DURUMU ne? (Base case - durma koşulu)
   → Rekürsiyonun durduğu en küçük problem
2. KÜÇÜLTME ADIMI ne? (Recursive step)
   → Problemi nasıl küçültüyorum?
3. Her adımda GERÇEKTEN küçülüyor mu?
   → Yoksa sonsuz döngüye girer!

⭐ ALTIN KURAL: "Kendime güveniyorum ki küçük versiyonu doğru çözerim,
   ben sadece bir adım ekliyorum."

ÖNEMLİ UYARI:
→ Python'da varsayılan recursion limiti ~1000
→ Çok derin recursion Stack Overflow yapar
→ Her recursion iteratif'e çevrilebilir (ama bazen daha karmaşık olur)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 3: RECURSION DERİNLEMESİNE")
print("=" * 70)


# --- PROBLEM 1: Recursion'un Temel Mantığı ---
def geri_sayim(n, derinlik=0):
    """
    📝 PROBLEM: N'den 0'a geri say.

    🧠 DÜŞÜNCEMİZ:
    → Taban durumu: n == 0 → "Başla!" yazdır ve dur
    → Küçültme: n → n-1

    "derinlik" parametresi sadece GÖRSEL amaçlı.
    Recursion'un nasıl derinleşip geri döndüğünü gösterir.
    """
    girinti = "    " * derinlik

    if n == 0:
        print(f"{girinti}🏁 Başla!")
        return  # TABAN DURUMU: Burada recursion durur

    print(f"{girinti}📢 {n}...")
    geri_sayim(n - 1, derinlik + 1)  # KENDİNİ ÇAĞIRIYOR (n küçülüyor)
    print(f"{girinti}↩️  {n}'e geri döndüm")  # Recursion geri sarılırken çalışır


print("\n🔄 Recursion Akışı (geri_sayim(4)):")
geri_sayim(4)

"""
📌 YUKARDAKI ÇIKTIYA DİKKATLE BAK!

Recursion iki aşamada çalışır:
1. İLERİ GİDİŞ (Winding)  : Kendini çağırarak derinleşir (4→3→2→1→0)
2. GERİ DÖNÜŞ (Unwinding)  : Sonuçlar geriye doğru döner (0→1→2→3→4)

Bu "geri dönüş" aşaması çok önemli!
Merge Sort, QuickSort gibi algoritmalar bu geri dönüşte iş yapar.
"""


# --- PROBLEM 2: İç İçe Listeleri Düzleştirme ---
def duzlestir(ic_ice_liste):
    """
    📝 PROBLEM: [[1, [2, 3]], [4, [5, [6]]]] → [1, 2, 3, 4, 5, 6]

    🧠 DÜŞÜNCE SÜRECİ:
    İç içe liste = "bilinmeyen derinlikte ağaç yapısı"
    Derinlik bilinmediği için döngü ile çözmek ZOR.
    Recursion ile çözmek DOĞAL.

    MANTIK:
    → Her elemana bak:
      → Eğer liste ise → REKÜRSİF olarak onu da düzleştir
      → Eğer liste değilse → Sonuca ekle
    → Taban durumu: Eleman liste değilse, direkt ekle
    """
    sonuc = []
    for eleman in ic_ice_liste:
        if isinstance(eleman, list):
            # Bu elemanın kendisi bir liste → Rekürsif olarak düzleştir
            sonuc.extend(duzlestir(eleman))
        else:
            # Bu eleman basit bir değer → Direkt ekle
            sonuc.append(eleman)
    return sonuc


print(f"\n📦 İç İçe Liste Düzleştirme:")
test_listeler = [
    [[1, [2, 3]], [4, [5, [6]]]],
    [1, [2, [3, [4, [5]]]]],
    [[[[1]]], 2, [3]],
    [1, 2, 3],  # Zaten düz
    [],          # Boş liste
]
for liste in test_listeler:
    print(f"  {str(liste):40} → {duzlestir(liste)}")


# --- PROBLEM 3: Tüm Permütasyonları Bulma ---
def permutasyonlar(elemanlar):
    """
    📝 PROBLEM: [1, 2, 3] → [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

    🧠 DÜŞÜNCE SÜRECİ (Bu zor bir problem, adım adım düşünelim):

    Adım 1: En küçük örneği düşün
    → [1] → [[1]] (tek eleman, tek permütasyon)
    → Bu taban durumu!

    Adım 2: Biraz büyütelim
    → [1, 2] → [[1,2], [2,1]]
    → Her elemanı başa koy, kalanların permütasyonlarını bul

    Adım 3: Genel kalıp
    → Her elemanı sırayla seç
    → Seçtiğini başa koy
    → GERİ KALANLARIN permütasyonlarını bul (RECURSİON!)
    → Seçtiğin elemanı her permütasyonun başına ekle

    GÖRSEL:
    [1, 2, 3]
    ├── 1 seçildi → [2, 3]'ün permütasyonları → [2,3], [3,2] → [1,2,3], [1,3,2]
    ├── 2 seçildi → [1, 3]'ün permütasyonları → [1,3], [3,1] → [2,1,3], [2,3,1]
    └── 3 seçildi → [1, 2]'nin permütasyonları → [1,2], [2,1] → [3,1,2], [3,2,1]

    KARMAŞIKLIK: O(n!) - Çünkü n! tane permütasyon var
    → 3! = 6, 4! = 24, 5! = 120, 10! = 3.628.800
    """
    # Taban durumu
    if len(elemanlar) <= 1:
        return [elemanlar[:]]  # Kopya döndür (orijinali değiştirmemek için)

    sonuc = []

    for i in range(len(elemanlar)):
        # i'nci elemanı seç
        secilen = elemanlar[i]

        # Geri kalanları al (seçileni çıkar)
        kalanlar = elemanlar[:i] + elemanlar[i + 1:]

        # Kalanların permütasyonlarını bul (RECURSİON)
        kalan_permutasyonlar = permutasyonlar(kalanlar)

        # Seçileni her permütasyonun başına ekle
        for perm in kalan_permutasyonlar:
            sonuc.append([secilen] + perm)

    return sonuc


print(f"\n🔀 Permütasyonlar:")
for test in [[1, 2, 3], ['A', 'B', 'C']]:
    perms = permutasyonlar(test)
    print(f"  {test} → {len(perms)} permütasyon:")
    for p in perms:
        print(f"    {p}")


# --- PROBLEM 4: Üs Alma - Hızlı Üs Algoritması ---
def hizli_us(taban, us):
    """
    📝 PROBLEM: taban^us hesapla (verimli şekilde).

    🧠 DÜŞÜNCE SÜRECİ:

    NAİF YÖNTEM: taban * taban * taban * ... (us kez) → O(n)

    AKILLI YÖNTEM: "Böl ve Fethet" → O(log n)

    MANTIK:
    → 2^8 = (2^4)^2 = ((2^2)^2)^2
    → 8 adım yerine 3 adım!

    FORMÜL:
    → us çift ise: taban^us = (taban^(us/2))^2
    → us tek ise:  taban^us = taban * taban^(us-1)
    → us == 0:     taban^0 = 1  (Taban durumu)

    NEDEN LOGARİTMİK?
    → Her adımda üssü YARIYA indiriyoruz
    → 2^1000 hesaplamak için ~10 çarpma yeterli! (1000 yerine)
    """
    # Taban durumları
    if us == 0:
        return 1
    if us < 0:
        return 1 / hizli_us(taban, -us)

    if us % 2 == 0:
        # Çift üs: taban^us = (taban^(us/2))^2
        yarim = hizli_us(taban, us // 2)
        return yarim * yarim  # Sadece 1 çarpma!
    else:
        # Tek üs: taban^us = taban * taban^(us-1)
        return taban * hizli_us(taban, us - 1)


print(f"\n⚡ Hızlı Üs Alma:")
print(f"  2^10  = {hizli_us(2, 10)}")
print(f"  3^5   = {hizli_us(3, 5)}")
print(f"  5^0   = {hizli_us(5, 0)}")
print(f"  2^-3  = {hizli_us(2, -3)}")
print(f"  2^20  = {hizli_us(2, 20)}")


# =============================================================================
# 📖 BÖLÜM 4: TWO POINTER (İKİ İŞARETÇİ) TEKNİĞİ
# =============================================================================
"""
🧠 TWO POINTER NEDİR?
→ İki tane "işaretçi" (index) kullanarak listeyi tarama tekniği
→ Genellikle SIRALI listelerde çalışır
→ O(n²) çözümü O(n)'e düşürür

NE ZAMAN KULLANILIR?
→ "İki elemanın toplamı X mi?" tipi sorular
→ "Palindrome mu?" soruları
→ "Sıralı listede çift bul" soruları
→ "İki sıralı listeyi birleştir" soruları

VARYANLAR:
1. Karşıdan gelen iki pointer (sol ← → sağ)
2. Aynı yönde iki pointer (yavaş → → hızlı →→)
3. Farklı listelerde pointer
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 4: TWO POINTER TEKNİĞİ")
print("=" * 70)


# --- PROBLEM 1: İki Sayının Toplamı ---
def iki_toplam_brute(sirali_liste, hedef):
    """
    ❌ BRUTE FORCE: O(n²) - Her çifti kontrol et.
    İç içe iki döngü: YAVAŞ!
    """
    for i in range(len(sirali_liste)):
        for j in range(i + 1, len(sirali_liste)):
            if sirali_liste[i] + sirali_liste[j] == hedef:
                return (i, j)
    return None


def iki_toplam_two_pointer(sirali_liste, hedef):
    """
    📝 PROBLEM: Sıralı listede toplamı 'hedef' olan iki elemanı bul.

    🧠 TWO POINTER DÜŞÜNCE SÜRECİ:

    Brute force: Her çifti dene → O(n²)
    Two pointer: Akıllıca iki uçtan gel → O(n)

    NASIL ÇALIŞIR?
    [1, 3, 5, 7, 9, 11]  hedef = 12
     ↑                 ↑
    sol               sağ

    → sol + sağ = 1 + 11 = 12 ✅ Buldum!

    Eğer toplam < hedef → sol'u sağa kaydır (toplamı ARTIR)
    Eğer toplam > hedef → sağ'ı sola kaydır (toplamı AZALT)

    NEDEN ÇALIŞIR?
    → Liste SIRALI olduğu için:
      - Toplamı artırmak istiyorsak → daha büyük eleman lazım → sol'u ilerlet
      - Toplamı azaltmak istiyorsak → daha küçük eleman lazım → sağ'ı geri çek
    → Her adımda bir pointer hareket eder → Toplam n adım → O(n)

    BU TEKNİK ÇOK ÖNEMLİ! LeetCode'da "Two Sum" problemi en ünlü sorudur.
    """
    sol = 0
    sag = len(sirali_liste) - 1

    while sol < sag:
        toplam = sirali_liste[sol] + sirali_liste[sag]

        if toplam == hedef:
            return (sol, sag)  # Buldum!
        elif toplam < hedef:
            sol += 1  # Toplam küçük → sol ilerle (daha büyük sayıya git)
        else:
            sag -= 1  # Toplam büyük → sağ geri gel (daha küçük sayıya git)

    return None  # Bulunamadı


# Test
sirali = [1, 3, 5, 7, 9, 11, 15, 20]
hedef = 16
print(f"\n🎯 İki Toplam (Two Pointer):")
print(f"  Liste: {sirali}, Hedef: {hedef}")

sonuc = iki_toplam_two_pointer(sirali, hedef)
if sonuc:
    i, j = sonuc
    print(f"  Bulundu: index {i} ve {j} → {sirali[i]} + {sirali[j]} = {hedef}")


# --- PROBLEM 2: Palindrome Kontrolü ---
def palindrome_mi(metin):
    """
    📝 PROBLEM: Metin palindrome mu? (Tersten de aynı okunan)
    Örnek: "kayak" → True, "racecar" → True

    🧠 TWO POINTER DÜŞÜNCE SÜRECİ:

    NAİF: Metni ters çevir, karşılaştır → O(n) zaman + O(n) bellek
    TWO POINTER: Baştan ve sondan karşılaştır → O(n) zaman + O(1) bellek

    MANTIK:
    "kayak"
     ↑   ↑    k == k ✅
      ↑ ↑     a == a ✅
       ↑      Ortada buluştular → Palindrome!

    Eğer herhangi bir noktada eşleşmezse → Palindrome değil
    """
    # Ön işleme: Sadece harf ve rakamları al, küçük harfe çevir
    temiz = ""
    for c in metin.lower():
        if c.isalnum():  # Harf veya rakam mı?
            temiz += c

    sol = 0
    sag = len(temiz) - 1

    while sol < sag:
        if temiz[sol] != temiz[sag]:
            return False  # Eşleşmedi → Palindrome değil
        sol += 1
        sag -= 1

    return True  # Tüm çiftler eşleşti → Palindrome!


print(f"\n🔄 Palindrome Kontrolü:")
test_metinler = [
    "kayak",
    "racecar",
    "A man, a plan, a canal: Panama",
    "hello",
    "Was it a car or a cat I saw?",
    "12321",
]
for metin in test_metinler:
    sonuc = "✅ Evet" if palindrome_mi(metin) else "❌ Hayır"
    print(f"  '{metin}' → {sonuc}")


# --- PROBLEM 3: Suyu En Çok Tutan Kap (Container With Most Water) ---
def en_cok_su(yukseklikler):
    """
    📝 PROBLEM: (LeetCode #11 - Klasik mülakat sorusu)
    Bir dizi dikey çizgi verilmiş. İki çizgi seç ki aralarında
    en fazla su tutulsun.

    Görsel:
    |         |
    |    |    |
    |    |  | |
    | |  |  | |
    ─────────────
    1 8  6  2 5 4 8 3 7

    Su miktarı = min(sol_yükseklik, sag_yükseklik) × genişlik

    🧠 DÜŞÜNCE SÜRECİ:

    BRUTE FORCE: Her çifti dene → O(n²)
    TWO POINTER: İki uçtan başla → O(n)

    NEDEN ÇALIŞIR?
    → En geniş kapla başla (sol=0, sag=son)
    → Genişliği daraltırken yüksekliği artırma şansımız var
    → HER ZAMAN daha KISA olanı hareket ettir
    → NEDEN? Kısa olan sınırlayıcı faktör. Onu ilerletmek
      belki daha uzun bir çizgi bulacak ve alan artacak.
      Uzun olanı ilerletmek alanı kesinlikle artırmaz!
    """
    sol = 0
    sag = len(yukseklikler) - 1
    max_alan = 0

    while sol < sag:
        # Alanı hesapla
        genislik = sag - sol
        yukseklik = min(yukseklikler[sol], yukseklikler[sag])
        alan = genislik * yukseklik

        max_alan = max(max_alan, alan)

        # Kısa olanı hareket ettir
        if yukseklikler[sol] < yukseklikler[sag]:
            sol += 1
        else:
            sag -= 1

    return max_alan


print(f"\n🌊 En Çok Su Tutan Kap:")
test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"  Yükseklikler: {test}")
print(f"  Maksimum su : {en_cok_su(test)} birim²")
# Cevap: min(8,7) × (8-1) = 7 × 7 = 49


# =============================================================================
# 📖 BÖLÜM 5: SLIDING WINDOW (KAYAN PENCERE) TEKNİĞİ
# =============================================================================
"""
🧠 SLIDING WINDOW NEDİR?
→ Sabit veya değişken boyutlu bir "pencere"yi liste üzerinde kaydırma
→ Pencere içindeki elemanları izleyerek sonuç hesaplama
→ O(n²) çözümü O(n)'e düşürür

NE ZAMAN KULLANILIR?
→ "Ardışık k elemanın en büyük toplamı" → Sabit pencere
→ "Toplamı X olan en kısa alt dizi" → Değişken pencere
→ "Tekrarsız en uzun alt string" → Değişken pencere
→ Genel olarak "ardışık" veya "alt dizi" kelimelerini gördüğünde düşün!

MANTIK:
Her seferinde tüm pencereyi yeniden hesaplamak yerine:
→ Pencere kayınca: Giren elemanı EKLE, çıkan elemanı ÇIKAR
→ Böylece her adım O(1) olur → Toplam O(n)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 5: SLIDING WINDOW TEKNİĞİ")
print("=" * 70)


# --- PROBLEM 1: Sabit Pencere ---
def max_toplam_alt_dizi(liste, k):
    """
    📝 PROBLEM: Ardışık k elemanın en büyük toplamını bul.
    Örnek: [2, 1, 5, 1, 3, 2], k=3 → 5+1+3 = 9

    🧠 DÜŞÜNCE SÜRECİ:

    BRUTE FORCE: Her k'lı grubu topla → O(n×k)
    SLIDING WINDOW: Kaydır, ekle, çıkar → O(n)

    GÖRSEL:
    [2, 1, 5, 1, 3, 2]   k=3
     ─────              toplam = 2+1+5 = 8
        ─────           toplam = 8 - 2 + 1 = 7  (2 çıktı, 1 girdi)
           ─────        toplam = 7 - 1 + 3 = 9  (1 çıktı, 3 girdi)
              ─────     toplam = 9 - 5 + 2 = 6  (5 çıktı, 2 girdi)
                                          max = 9 ✅

    HER ADIMDA NE OLDU?
    → Yeni toplam = Eski toplam - Çıkan eleman + Giren eleman
    → Tüm pencereyi yeniden toplamaya gerek yok!
    → Bu fark O(n×k) ile O(n) arasındaki fark!
    """
    if not liste or k > len(liste) or k <= 0:
        return None

    # İlk pencereyi hesapla
    pencere_toplam = sum(liste[:k])
    max_toplam = pencere_toplam

    # Pencereyi kaydır
    for i in range(k, len(liste)):
        # Kaydırma: Yeni eleman girer, eski eleman çıkar
        pencere_toplam += liste[i]      # Yeni eleman girdi (sağdan)
        pencere_toplam -= liste[i - k]  # Eski eleman çıktı (soldan)

        max_toplam = max(max_toplam, pencere_toplam)

    return max_toplam


print(f"\n📊 Sabit Pencere - Max Toplam Alt Dizi:")
test = [2, 1, 5, 1, 3, 2]
for k in [2, 3, 4]:
    print(f"  {test}, k={k} → Max toplam: {max_toplam_alt_dizi(test, k)}")


# --- PROBLEM 2: Değişken Pencere ---
def en_kisa_alt_dizi_toplam(liste, hedef):
    """
    📝 PROBLEM: Toplamı >= hedef olan EN KISA ardışık alt diziyi bul.
    Örnek: [2, 3, 1, 2, 4, 3], hedef=7 → [4, 3] (uzunluk 2)

    🧠 DÜŞÜNCE SÜRECİ:

    BRUTE FORCE: Tüm alt dizileri dene → O(n²)
    SLIDING WINDOW (Değişken): İki pointer ile → O(n)

    MANTIK:
    → "sag" pointer'ı ilerle, pencereye eleman ekle
    → Toplam >= hedef olunca → "sol" pointer'ı ilerle (pencereyi küçült)
    → Minimum uzunluğu güncelle
    → Toplam < hedef olunca → tekrar "sag"ı ilerle

    NEDEN BU DOĞRU?
    → Sağı ilerletmek toplamı artırır
    → Solu ilerletmek toplamı azaltır (pencereyi küçültür)
    → Hedefi sağladıktan sonra minimum uzunluğu arıyoruz
      → Bu yüzden pencereyi mümkün olduğunca KÜÇÜLTÜYORUZ
    """
    n = len(liste)
    min_uzunluk = float('inf')  # Sonsuz ile başla (hiç bulamayabiliriz)
    pencere_toplam = 0
    sol = 0

    for sag in range(n):
        pencere_toplam += liste[sag]  # Pencereye ekle

        # Toplam yeterliyse, pencereyi küçült
        while pencere_toplam >= hedef:
            uzunluk = sag - sol + 1
            min_uzunluk = min(min_uzunluk, uzunluk)
            pencere_toplam -= liste[sol]  # Sol elemanı çıkar
            sol += 1  # Pencereyi küçült

    return min_uzunluk if min_uzunluk != float('inf') else 0


print(f"\n📊 Değişken Pencere - En Kısa Alt Dizi:")
test = [2, 3, 1, 2, 4, 3]
hedef = 7
sonuc = en_kisa_alt_dizi_toplam(test, hedef)
print(f"  {test}, hedef={hedef} → En kısa uzunluk: {sonuc}")


# --- PROBLEM 3: Tekrarsız En Uzun Alt String ---
def en_uzun_tekrarsiz(metin):
    """
    📝 PROBLEM: (LeetCode #3 - Çok klasik mülakat sorusu!)
    Tekrarsız karakterlerden oluşan en uzun alt string'i bul.
    "abcabcbb" → "abc" (uzunluk 3)
    "pwwkew"   → "wke" (uzunluk 3)

    🧠 DÜŞÜNCE SÜRECİ:

    BRUTE FORCE: Her alt string'i kontrol et → O(n³)
    SLIDING WINDOW + SET: → O(n)

    MANTIK:
    → Pencere = tekrarsız karakterler bölgesi
    → Sağ pointer ilerler, yeni karakteri pencereye ekler
    → Eğer karakter zaten penceredeyse:
      → Sol pointer'ı o karakteri geçene kadar ilerlet
    → Her adımda max uzunluğu güncelle

    NEDEN SET KULLANIYORUZ?
    → "Bu karakter pencerede var mı?" sorusu → O(1) ile cevaplanır
    → Liste kullansak → O(n) ile cevaplarız (yavaş)
    """
    karakter_seti = set()  # Penceredeki karakterler
    sol = 0
    max_uzunluk = 0
    en_iyi_baslangic = 0

    for sag in range(len(metin)):
        # Eğer karakter zaten penceredeyse, sol pointer'ı ilerlet
        while metin[sag] in karakter_seti:
            karakter_seti.remove(metin[sol])
            sol += 1

        # Yeni karakteri ekle
        karakter_seti.add(metin[sag])

        # Max uzunluğu güncelle
        if sag - sol + 1 > max_uzunluk:
            max_uzunluk = sag - sol + 1
            en_iyi_baslangic = sol

    en_iyi_substring = metin[en_iyi_baslangic:en_iyi_baslangic + max_uzunluk]
    return max_uzunluk, en_iyi_substring


print(f"\n📊 Tekrarsız En Uzun Alt String:")
for metin in ["abcabcbb", "bbbbb", "pwwkew", "abdulkadir", ""]:
    uzunluk, substring = en_uzun_tekrarsiz(metin)
    print(f"  '{metin}' → '{substring}' (uzunluk: {uzunluk})")


# =============================================================================
# 📖 BÖLÜM 6: GREEDY (AÇGÖZLÜ) ALGORİTMA
# =============================================================================
"""
🧠 GREEDY NEDİR?
→ Her adımda O ANKİ en iyi seçimi yap
→ Geleceği düşünme, şu an neyi yaparsan kârlısın onu yap
→ Basit ve hızlı, AMA her zaman optimal sonuç vermez!

NE ZAMAN KULLANILIR?
→ Problem "optimal altçözüm" özelliği taşıyorsa
→ Yani parçalar optimal → bütün optimal ise
→ Genellikle sıralama ile birlikte kullanılır

NE ZAMAN KULLANILMAZ?
→ Yerel en iyi seçim, global en iyiyi garanti etmiyorsa
→ O zaman Dynamic Programming lazım!
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 6: GREEDY ALGORİTMA")
print("=" * 70)


# --- PROBLEM: Etkinlik Seçimi (Activity Selection) ---
def etkinlik_sec(etkinlikler):
    """
    📝 PROBLEM: Birbiriyle çakışmayan MAXIMUM sayıda etkinliğe katıl.
    Her etkinliğin başlangıç ve bitiş saati var.

    Örnek:
    Etkinlik A: 09:00 - 11:00
    Etkinlik B: 10:00 - 12:00  (A ile çakışıyor!)
    Etkinlik C: 11:00 - 13:00
    Etkinlik D: 12:00 - 14:00

    En fazla: A + C veya A + D (2 etkinlik)

    🧠 GREEDY DÜŞÜNCE SÜRECİ:

    Adım 1: "Hangi kritere göre seçeyim?"
    → En erken başlayan? ❌ Uzun süren erken etkinlik diğerlerini bloklar
    → En kısa süren?    ❌ Kısa ama ortada olan diğerlerini bloklar
    → EN ERKEN BİTEN?   ✅ Doğru strateji!

    NEDEN EN ERKEN BİTEN?
    → Erken biten etkinlik, sonraki etkinliklere EN FAZLA zaman bırakır
    → Bu "açgözlü" seçim global olarak da optimal sonuç verir
    → Matematiksel olarak kanıtlanmış!

    ALGORİTMA:
    1. Etkinlikleri BİTİŞ SAATİNE göre sırala
    2. İlk etkinliği seç
    3. Sıradaki etkinliğin başlangıcı >= son seçilenin bitişi ise → Seç
    4. Değilse → Atla
    """
    if not etkinlikler:
        return []

    # Bitiş saatine göre sırala
    # NEDEN key=lambda? → Her etkinlik (isim, başlangıç, bitiş) tuple'ı
    # x[2] = bitiş saati
    sirali = sorted(etkinlikler, key=lambda x: x[2])

    secilen = [sirali[0]]  # İlk etkinliği seç (en erken biten)
    son_bitis = sirali[0][2]

    for i in range(1, len(sirali)):
        isim, baslangic, bitis = sirali[i]

        if baslangic >= son_bitis:  # Çakışmıyor!
            secilen.append(sirali[i])
            son_bitis = bitis

    return secilen


etkinlikler = [
    ("Matematik",  9,  11),
    ("Fizik",      10, 12),
    ("Kimya",      11, 13),
    ("Biyoloji",   12, 14),
    ("Tarih",      8,  10),
    ("Coğrafya",   13, 15),
    ("İngilizce",  14, 16),
    ("Müzik",      15, 17),
]

secilen = etkinlik_sec(etkinlikler)
print(f"\n📅 Etkinlik Seçimi (Greedy):")
print(f"  Toplam etkinlik: {len(etkinlikler)}")
print(f"  Seçilen ({len(secilen)} etkinlik):")
for isim, bas, bit in secilen:
    print(f"    {isim:12} → {bas:02d}:00 - {bit:02d}:00")


# --- PROBLEM: Huffman Benzeri Sıkıştırma Mantığı ---
def min_maliyet_birlestirme(dosya_boyutlari):
    """
    📝 PROBLEM: N tane dosyayı birleştirmek istiyoruz.
    İki dosyayı birleştirmenin maliyeti = boyutlarının toplamı.
    MINIMUM toplam maliyetle tüm dosyaları birleştir.

    Örnek: [2, 3, 4, 5]
    Kötü strateji: (2+3)=5 → (5+4)=9 → (9+5)=14 → Maliyet: 5+9+14 = 28
    İyi strateji:  (2+3)=5 → (4+5)=9 → (5+9)=14 → Maliyet: 5+9+14 = 28
    En iyi:        (2+3)=5 → (4+5)=9 → (5+9)=14 → Maliyet: 5+9+14 = 28

    Hmm, aynı çıktı. Daha büyük örnekle:
    [1, 2, 3, 4, 5]
    Greedy: Her zaman en küçük ikisini birleştir!

    🧠 NEDEN EN KÜÇÜK İKİSİ?
    → Küçük dosyalar daha çok birleştirme adımından geçecek
    → O yüzden onları ERKEN birleştirmek toplam maliyeti azaltır
    → Bu Huffman Coding'in temelidir (veri sıkıştırma algoritması!)
    """
    import heapq  # Min-heap (öncelik kuyruğu)

    # Min-heap oluştur
    # NEDEN HEAP?
    # → Her adımda en küçük iki elemanı bulmamız lazım
    # → Sıralı listede: ekleme O(n), minimum O(1)
    # → Heap'te: ekleme O(log n), minimum O(1) → Daha dengeli!
    heap = dosya_boyutlari[:]
    heapq.heapify(heap)  # Listeyi heap'e çevir → O(n)

    toplam_maliyet = 0
    adimlar = []

    while len(heap) > 1:
        # En küçük ikiyi çıkar
        birinci = heapq.heappop(heap)  # O(log n)
        ikinci = heapq.heappop(heap)   # O(log n)

        maliyet = birinci + ikinci
        toplam_maliyet += maliyet
        adimlar.append(f"{birinci} + {ikinci} = {maliyet}")

        # Birleştirilmişi geri koy
        heapq.heappush(heap, maliyet)  # O(log n)

    return toplam_maliyet, adimlar


boyutlar = [1, 2, 3, 4, 5]
maliyet, adimlar = min_maliyet_birlestirme(boyutlar)
print(f"\n📦 Minimum Maliyet Birleştirme:")
print(f"  Dosya boyutları: {boyutlar}")
for i, adim in enumerate(adimlar, 1):
    print(f"  Adım {i}: {adim}")
print(f"  Toplam maliyet: {maliyet}")


# =============================================================================
# 📖 BÖLÜM 7: DIVIDE & CONQUER (BÖL VE FETHET)
# =============================================================================
"""
🧠 DIVIDE & CONQUER NEDİR?
→ Problemi AYNI TÜRDE daha küçük parçalara böl
→ Her parçayı (genellikle rekürsif) çöz
→ Parçaların çözümlerini birleştir

NEREDE KULLANILIR?
→ Merge Sort, Quick Sort
→ İkili arama
→ Matris çarpımı (Strassen)
→ En yakın iki nokta problemi

GREEDY'DEN FARKI:
→ Greedy: Her adımda BİR seçim yap, geri dönme
→ D&C: Problemi BÖL, ayrı ayrı çöz, BİRLEŞTİR
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 7: DIVIDE & CONQUER")
print("=" * 70)


# --- PROBLEM: Maximum Alt Dizi Toplamı (Kadane vs D&C) ---
def max_alt_dizi_dc(liste, sol=None, sag=None):
    """
    📝 PROBLEM: Bir dizideki ardışık elemanların en büyük toplamını bul.
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] → [4, -1, 2, 1] = 6

    🧠 D&C DÜŞÜNCE SÜRECİ:

    Diziyi ikiye böl. En büyük alt dizi üç yerden birinde:
    1. Tamamen SOL yarıda
    2. Tamamen SAĞ yarıda
    3. Ortadan geçiyor (sol yarının bir kısmı + sağ yarının bir kısmı)

    Her biri için ayrı çöz, en büyüğünü döndür.

    KARMAŞIKLIK: O(n log n)
    → Her seviyede O(n) iş (ortadan geçen kısmı bulmak)
    → log n seviye derinlik
    """
    if sol is None:
        sol = 0
        sag = len(liste) - 1

    # Taban durumu
    if sol == sag:
        return liste[sol]

    orta = (sol + sag) // 2

    # 1. Sol yarıdaki max alt dizi (rekürsif)
    sol_max = max_alt_dizi_dc(liste, sol, orta)

    # 2. Sağ yarıdaki max alt dizi (rekürsif)
    sag_max = max_alt_dizi_dc(liste, orta + 1, sag)

    # 3. Ortadan geçen max alt dizi
    # Ortadan sola doğru en iyi toplamı bul
    sol_toplam = float('-inf')
    toplam = 0
    for i in range(orta, sol - 1, -1):
        toplam += liste[i]
        sol_toplam = max(sol_toplam, toplam)

    # Ortadan sağa doğru en iyi toplamı bul
    sag_toplam = float('-inf')
    toplam = 0
    for i in range(orta + 1, sag + 1):
        toplam += liste[i]
        sag_toplam = max(sag_toplam, toplam)

    orta_max = sol_toplam + sag_toplam

    # En büyüğünü döndür
    return max(sol_max, sag_max, orta_max)


# Kadane's Algorithm - O(n) ile aynı problemi çözer
def max_alt_dizi_kadane(liste):
    """
    📝 Kadane's Algorithm - Maximum Alt Dizi Toplamı

    🧠 DÜŞÜNCE SÜRECİ:

    Bu bir DP (Dynamic Programming) yaklaşımıdır.

    MANTIK (çok zarif):
    → Her elemanda karar ver:
      "Bu elemanı önceki alt diziye EKLEMEK mi kârlı,
       yoksa BU ELEMANDAN YENİ bir alt dizi BAŞLATMAK mı?"

    → Eğer önceki alt dizi toplamı negatifse → Yeni başla!
      (Negatif toplam seni geriye çekiyor, sıfırdan başlaman daha iyi)
    → Eğer pozitifse → Devam et, ekle!

    Bu BASİT ama ÇOK GÜÇLÜ bir fikir!
    Programlamanın en zarif algoritmalarından biri.
    """
    if not liste:
        return 0

    mevcut_max = liste[0]  # Mevcut alt dizinin toplamı
    global_max = liste[0]  # Şimdiye kadarki en büyük toplam

    for i in range(1, len(liste)):
        # ANA KARAR: Devam mı edeyim, yoksa yeniden mi başlayım?
        mevcut_max = max(liste[i], mevcut_max + liste[i])
        # ↑ max(yeniden başla, devam et)

        global_max = max(global_max, mevcut_max)

    return global_max


test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"\n📊 Maximum Alt Dizi Toplamı:")
print(f"  Liste: {test}")
print(f"  D&C çözüm   : {max_alt_dizi_dc(test)}")
print(f"  Kadane çözüm : {max_alt_dizi_kadane(test)}")
print(f"  (Her ikisi de 6: alt dizi [4, -1, 2, 1])")


# =============================================================================
# 📖 BÖLÜM 8: DYNAMIC PROGRAMMING (DİNAMİK PROGRAMLAMA) ★★★
# =============================================================================
"""
🧠 DYNAMİK PROGRAMLAMA (DP) NEDİR?

★★★ BU BÖLÜM ÇOK ÖNEMLİ! ★★★
DP'yi anlayan bir yazılımcı, anlayamayan birinden KAT KAT daha güçlüdür.
Mülakatların %50'si DP sorusudur. Gerçek dünya problemlerinin çoğu DP'dir.

DP = "Büyük problemi küçük alt problemlere böl, HER ALT PROBLEMİ SADECE
      BİR KEZ ÇÖZ, sonucu SAKLA ve tekrar kullan."

RECURSION'DAN FARKI:
→ Recursion: Aynı alt problemi tekrar tekrar çözer (GEREKSIZ İŞ)
→ DP: Her alt problemi BİR KEZ çözer, sonucu TABLO'da saklar

DP İÇİN 2 KOŞUL GEREKLİ:
1. Optimal Altçözüm (Optimal Substructure):
   → Büyük çözüm, küçük çözümlerden oluşturulabilir
2. Örtüşen Alt Problemler (Overlapping Subproblems):
   → Aynı alt problem birden fazla kez çözülüyor

İKİ YAKLAŞIM:
1. Top-Down (Memoization): Büyükten küçüğe, sonuçları önbelleğe al
2. Bottom-Up (Tabulation): Küçükten büyüğe, tablo doldur ← GENELLİKLE DAHA İYİ

💡 DP ÇÖZME FORMÜLÜ:
   1. "Alt problem ne?" sorusunu cevapla
   2. "Geçiş denklemi ne?" (bir hücre diğerlerinden nasıl hesaplanır?)
   3. "Taban durumları ne?" (başlangıç değerleri)
   4. "Sonuç nerede?" (tablonun hangi hücresinde?)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 8: DYNAMIC PROGRAMMING ★★★")
print("=" * 70)


# --- PROBLEM 1: Merdiven Tırmanma ---
def merdiven_tirmanma(n):
    """
    📝 PROBLEM: (LeetCode #70 - Klasik DP giriş sorusu)
    n basamaklı bir merdiveni 1 veya 2 adım atarak kaç farklı
    şekilde tırmanabilirsin?

    🧠 DP DÜŞÜNCE SÜRECİ (Adım adım):

    ADIM 1: "Alt problem ne?"
    → dp[i] = i. basamağa ulaşmanın kaç farklı yolu var?

    ADIM 2: "Geçiş denklemi ne?"
    → i. basamağa nereden gelebilirim?
      - (i-1). basamaktan 1 adım atarak
      - (i-2). basamaktan 2 adım atarak
    → dp[i] = dp[i-1] + dp[i-2]

    HEY, BU FİBONACCİ! Evet! Birçok problem tanıdık kalıplara dönüşür.

    ADIM 3: "Taban durumları ne?"
    → dp[0] = 1 (0. basamakta zaten duruyorsun: 1 yol)
    → dp[1] = 1 (1 basamak: sadece 1 adım atabilirsin: 1 yol)

    ADIM 4: "Sonuç nerede?"
    → dp[n]

    GÖRSEL (n=4):
    Basamak:  0   1   2   3   4
    dp:      [1] [1] [2] [3] [5]
                      ↑       ↑
                   1+1=2   3+2=5

    Yollar: 1111, 112, 121, 211, 22 → 5 yol ✅
    """
    if n <= 1:
        return 1

    # Bottom-Up DP
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Optimize versiyon - O(1) bellek
def merdiven_tirmanma_optimize(n):
    """
    BELLEK OPTİMİZASYONU:
    → dp[i] sadece dp[i-1] ve dp[i-2]'ye bağlı
    → O zaman tüm tabloyu tutmaya gerek yok!
    → Sadece son iki değeri tut → O(1) bellek

    Bu optimizasyon tekniği HER DP probleminde sorulabilir!
    """
    if n <= 1:
        return 1

    onceki = 1  # dp[0]
    simdiki = 1  # dp[1]

    for i in range(2, n + 1):
        onceki, simdiki = simdiki, onceki + simdiki

    return simdiki


print(f"\n🪜 Merdiven Tırmanma:")
for n in [3, 4, 5, 10, 20]:
    print(f"  {n:2d} basamak → {merdiven_tirmanma(n):6d} farklı yol")


# --- PROBLEM 2: 0/1 Sırt Çantası (Knapsack) ---
def sirt_cantasi(kapasite, agirliklar, degerler):
    """
    📝 PROBLEM: (En ünlü DP problemlerinden biri!)
    Bir hırsız çantasına sığdırabildiği kadar eşya koymak istiyor.
    Her eşyanın ağırlığı ve değeri var.
    Çantanın kapasitesi sınırlı.
    MAXİMUM değeri topla!

    Örnek:
    Kapasite: 7 kg
    Eşya 1: 1 kg, 1₺
    Eşya 2: 3 kg, 4₺
    Eşya 3: 4 kg, 5₺
    Eşya 4: 5 kg, 7₺

    En iyi: Eşya 2 + Eşya 3 = 7 kg, 9₺

    🧠 DP DÜŞÜNCE SÜRECİ:

    ADIM 1: "Alt problem ne?"
    → dp[i][w] = İlk i eşya ile w kapasitede elde edilecek MAX değer

    ADIM 2: "Geçiş denklemi ne?"
    → Her eşya için iki seçenek var:
      a) Bu eşyayı ALMA → dp[i][w] = dp[i-1][w]
      b) Bu eşyayı AL   → dp[i][w] = dp[i-1][w - agirlik[i]] + deger[i]
         (Ama sadece ağırlığı kapasiteye sığıyorsa!)
    → dp[i][w] = max(alma, al)

    ADIM 3: "Taban durumları?"
    → dp[0][w] = 0 (Hiç eşya yoksa değer 0)
    → dp[i][0] = 0 (Kapasite 0 ise hiçbir şey alamazsın)

    ADIM 4: "Sonuç nerede?"
    → dp[n][kapasite]

    NEDEN BU PROBLEM ÇOK ÖNEMLİ?
    → Kaynak tahsisi problemleri (bütçe dağılımı)
    → Yatırım portföyü optimizasyonu
    → Dosya yedekleme (hangi dosyalar yedeklenecek?)
    → Proje seçimi (sınırlı bütçeyle hangi projeler?)
    """
    n = len(agirliklar)

    # 2D DP tablosu oluştur
    # dp[i][w] = ilk i eşya ile w kapasitede max değer
    dp = [[0] * (kapasite + 1) for _ in range(n + 1)]

    # Tabloyu doldur
    for i in range(1, n + 1):
        for w in range(kapasite + 1):
            # Seçenek 1: Bu eşyayı ALMA
            dp[i][w] = dp[i - 1][w]

            # Seçenek 2: Bu eşyayı AL (eğer sığıyorsa)
            esya_agirlik = agirliklar[i - 1]
            esya_deger = degerler[i - 1]

            if esya_agirlik <= w:
                al = dp[i - 1][w - esya_agirlik] + esya_deger
                dp[i][w] = max(dp[i][w], al)

    # Hangi eşyaları seçtiğimizi geri izle (Backtracking)
    secilen = []
    w = kapasite
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # Bu eşya seçilmiş!
            secilen.append(i - 1)
            w -= agirliklar[i - 1]

    return dp[n][kapasite], secilen


# Test
agirliklar = [1, 3, 4, 5]
degerler = [1, 4, 5, 7]
kapasite = 7
esya_isimleri = ["Altın Yüzük", "Gümüş Vazo", "Kristal Top", "Elmas Kolye"]

max_deger, secilen = sirt_cantasi(kapasite, agirliklar, degerler)
print(f"\n🎒 Sırt Çantası Problemi:")
print(f"  Kapasite: {kapasite} kg")
print(f"  Eşyalar:")
for i in range(len(agirliklar)):
    print(f"    {esya_isimleri[i]:15} → {agirliklar[i]} kg, {degerler[i]}₺")
print(f"\n  ✅ Seçilen eşyalar ({max_deger}₺):")
toplam_agirlik = 0
for i in sorted(secilen):
    toplam_agirlik += agirliklar[i]
    print(f"    {esya_isimleri[i]:15} → {agirliklar[i]} kg, {degerler[i]}₺")
print(f"  Toplam ağırlık: {toplam_agirlik} kg")


# --- PROBLEM 3: En Uzun Ortak Alt Dizi (LCS) ---
def lcs(metin1, metin2):
    """
    📝 PROBLEM: (LeetCode #1143 - Çok klasik!)
    İki string'in en uzun ortak alt dizisini bul.
    "ABCBDAB" ve "BDCAB" → "BCAB" (uzunluk 4)

    NOT: Alt dizi (subsequence) ardışık olmak zorunda değil!
    "ACE" "ABCDE"nin alt dizisidir (A_C_E)

    🧠 DP DÜŞÜNCE SÜRECİ:

    ADIM 1: "Alt problem ne?"
    → dp[i][j] = metin1'in ilk i karakteri ile metin2'nin ilk j karakterinin LCS uzunluğu

    ADIM 2: "Geçiş denklemi ne?"
    → Eğer metin1[i-1] == metin2[j-1]:  (Son karakterler eşleşiyor)
        dp[i][j] = dp[i-1][j-1] + 1     (Her ikisinden bir geri git + 1 ekle)
    → Eğer eşleşmiyorsa:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (Birinden bir geri git, en iyisini al)

    ADIM 3: "Taban durumları?"
    → dp[0][j] = 0 (Boş string ile hiçbir şeyin ortak alt dizisi yok)
    → dp[i][0] = 0

    BU PROBLEM NEDEN ÖNEMLİ?
    → Git diff (iki dosya arasındaki farkı bulmak) buna dayanır!
    → DNA sekans karşılaştırma
    → Yazım denetimi
    → Dosya senkronizasyonu
    """
    m, n = len(metin1), len(metin2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if metin1[i - 1] == metin2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS'yi geri izle
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if metin1[i - 1] == metin2[j - 1]:
            lcs_str.append(metin1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    return dp[m][n], ''.join(lcs_str)


print(f"\n🔗 En Uzun Ortak Alt Dizi (LCS):")
test_ciftleri = [
    ("ABCBDAB", "BDCAB"),
    ("ALGORITMA", "ALORITMA"),
    ("PYTHON", "PATON"),
]
for m1, m2 in test_ciftleri:
    uzunluk, alt_dizi = lcs(m1, m2)
    print(f"  '{m1}' & '{m2}' → '{alt_dizi}' (uzunluk: {uzunluk})")


# --- PROBLEM 4: Para Bozma (Coin Change) ---
def para_bozma(bozukluklar, tutar):
    """
    📝 PROBLEM: (LeetCode #322)
    Verilen tutarı minimum sayıda bozuklukla öde.
    Bozukluklar: [1, 5, 10, 25]  Tutar: 41
    → 25 + 10 + 5 + 1 = 41 (4 bozukluk)

    🧠 DP DÜŞÜNCE SÜRECİ:

    ADIM 1: "Alt problem ne?"
    → dp[t] = t tutarını ödemek için gereken MİNİMUM bozukluk sayısı

    ADIM 2: "Geçiş denklemi ne?"
    → Her bozukluk c için: dp[t] = min(dp[t], dp[t - c] + 1)
    → Yani: "t TL ödemek için, her bozukluğu deneyeyim.
      Eğer c TL'lik bozukluk kullanırsam, kalan (t-c) TL'yi
      minimum bozuklukla ödemenin yolunu biliyorum."

    ADIM 3: "Taban durumu?"
    → dp[0] = 0 (0 TL ödemek için 0 bozukluk lazım)

    ⚠️ GREEDY NEDEN ÇALIŞMAZ?
    → Bozukluklar: [1, 3, 4], Tutar: 6
    → Greedy: 4+1+1 = 3 bozukluk
    → Optimal: 3+3 = 2 bozukluk ← DP bunu bulur!
    """
    # dp[i] = i tutarını ödemek için gereken min bozukluk
    dp = [float('inf')] * (tutar + 1)
    dp[0] = 0

    # Hangi bozuklukların kullanıldığını takip et
    kullanilan = [-1] * (tutar + 1)

    for t in range(1, tutar + 1):
        for c in bozukluklar:
            if c <= t and dp[t - c] + 1 < dp[t]:
                dp[t] = dp[t - c] + 1
                kullanilan[t] = c  # Bu tutarda hangi bozukluk kullanıldı

    if dp[tutar] == float('inf'):
        return -1, []  # Ödeme yapılamaz

    # Kullanılan bozuklukları geri izle
    secilen = []
    t = tutar
    while t > 0:
        secilen.append(kullanilan[t])
        t -= kullanilan[t]

    return dp[tutar], secilen


print(f"\n💰 Para Bozma (DP):")
# Normal durum
bozukluklar = [1, 5, 10, 25]
tutar = 41
adet, secilen = para_bozma(bozukluklar, tutar)
print(f"  Bozukluklar: {bozukluklar}, Tutar: {tutar}")
print(f"  Minimum {adet} bozukluk: {secilen}")

# Greedy'nin yanlış cevap verdiği durum!
print(f"\n  ⚠️ Greedy'nin Yanıldığı Durum:")
bozukluklar2 = [1, 3, 4]
tutar2 = 6
adet2, secilen2 = para_bozma(bozukluklar2, tutar2)
print(f"  Bozukluklar: {bozukluklar2}, Tutar: {tutar2}")
print(f"  Greedy cevap: [4, 1, 1] = 3 bozukluk ❌")
print(f"  DP cevap:     {secilen2} = {adet2} bozukluk ✅")


# =============================================================================
# 📖 BÖLÜM 9: BACKTRACKING (GERİ İZLEME) ★★
# =============================================================================
"""
🧠 BACKTRACKING NEDİR?
→ "Dene, yanlışsa GERİ AL, başka yolu dene"
→ Sistematik deneme-yanılma
→ Tüm olasılıkları keşfeder ama BUDAMA (pruning) ile hızlanır

ŞABLON:
def backtrack(adaylar, mevcut_cozum):
    if cozum_tamamsa(mevcut_cozum):
        sonuclara_ekle(mevcut_cozum)
        return

    for aday in adaylar:
        if gecerli_mi(aday):
            mevcut_cozum.ekle(aday)     # SEÇ
            backtrack(kalan_adaylar)      # İLERLE
            mevcut_cozum.kaldir(aday)    # GERİ AL (backtrack)

NEREDE KULLANILIR?
→ Sudoku çözücü
→ N-Queens problemi
→ Tüm kombinasyonları/permütasyonları bulma
→ Labirent çözme
→ Kelime arama (word search)
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 9: BACKTRACKING")
print("=" * 70)


# --- PROBLEM 1: N-Queens (N Vezir Problemi) ---
def n_queens(n):
    """
    📝 PROBLEM: N×N satranç tahtasına N vezir yerleştir,
    hiçbiri birbirini tehdit etmesin!

    Vezir: Yatay, dikey ve çapraz her yöne hareket edebilir.

    🧠 BACKTRACKING DÜŞÜNCE SÜRECİ:

    MANTIK:
    → Her satıra bir vezir koy (çünkü her satırda EN FAZLA 1 vezir olabilir)
    → Her sütunu dene
    → Eğer güvenli ise → koy ve bir sonraki satıra geç
    → Eğer hiçbir sütun güvensizse → GERİ DÖN (backtrack)

    GÜVENLİK KONTROLÜ:
    → Aynı sütunda başka vezir var mı?
    → Aynı sol çaprazda başka vezir var mı?
    → Aynı sağ çaprazda başka vezir var mı?
    (Aynı satırı kontrol etmeye gerek yok çünkü her satıra 1 tane koyuyoruz)

    BUDAMA (Pruning):
    → Güvensiz pozisyon bulunca o dalı TAMAMEN atla
    → Bu, tüm n^n olasılığı denememizi önler
    """
    sonuclar = []
    tahta = [-1] * n  # tahta[i] = i. satırdaki vezirin sütun numarası

    # Bu set'ler güvenlik kontrolünü O(1)'e düşürür
    sutunlar = set()      # Kullanılan sütunlar
    sol_capraz = set()    # Kullanılan sol çaprazlar (satır - sütun)
    sag_capraz = set()    # Kullanılan sağ çaprazlar (satır + sütun)

    def backtrack(satir):
        # Taban durumu: Tüm satırlara vezir koyduk
        if satir == n:
            # Tahta kopyasını kaydet
            sonuclar.append(tahta[:])
            return

        for sutun in range(n):
            # BUDAMA: Bu pozisyon güvenli mi?
            if (sutun in sutunlar or
                    satir - sutun in sol_capraz or
                    satir + sutun in sag_capraz):
                continue  # Güvensiz, atla

            # SEÇ: Veziri yerleştir
            tahta[satir] = sutun
            sutunlar.add(sutun)
            sol_capraz.add(satir - sutun)
            sag_capraz.add(satir + sutun)

            # İLERLE: Bir sonraki satıra geç
            backtrack(satir + 1)

            # GERİ AL: Veziri kaldır (backtrack)
            tahta[satir] = -1
            sutunlar.remove(sutun)
            sol_capraz.remove(satir - sutun)
            sag_capraz.remove(satir + sutun)

    backtrack(0)
    return sonuclar


def tahtayi_goster(cozum):
    """Satranç tahtasını güzel göster."""
    n = len(cozum)
    for satir in range(n):
        satirstr = ""
        for sutun in range(n):
            if cozum[satir] == sutun:
                satirstr += " ♛"
            else:
                satirstr += " ·"
        print(f"    {satirstr}")


print(f"\n♛ N-Queens Problemi:")
for n in [4, 5, 8]:
    cozumler = n_queens(n)
    print(f"\n  {n}×{n} tahta → {len(cozumler)} çözüm bulundu")
    if n <= 5 and cozumler:
        print(f"  İlk çözüm:")
        tahtayi_goster(cozumler[0])


# --- PROBLEM 2: Alt Küme Toplamı ---
def alt_kume_toplam(sayilar, hedef):
    """
    📝 PROBLEM: Verilen sayılardan hangilerinin toplamı hedef eder?
    [2, 3, 7, 8, 10], hedef=11 → [3, 8] veya [8, 3]

    🧠 BACKTRACKING DÜŞÜNCE SÜRECİ:

    Her sayı için iki seçenek:
    1. Bu sayıyı DAHİL ET → Hedefe yaklaş
    2. Bu sayıyı DIŞARIDA BIRAK → Sonraki sayıya geç

    Bu bir "karar ağacı" oluşturur:
                        []
                    /        \
               [2]            []
              /    \        /    \
          [2,3]   [2]    [3]    []
          ...     ...    ...    ...

    BUDAMA:
    → Mevcut toplam > hedef → Bu dalı kes (daha fazla ekleme)
    → Bu, çok fazla gereksiz dalı eler
    """
    sonuclar = []

    def backtrack(index, mevcut, mevcut_toplam):
        # Taban durumu: Hedefe ulaştık!
        if mevcut_toplam == hedef:
            sonuclar.append(mevcut[:])
            return

        # BUDAMA: Toplam hedefi aştıysa devam etme
        if mevcut_toplam > hedef or index >= len(sayilar):
            return

        for i in range(index, len(sayilar)):
            # Aynı seviyede tekrar eden sayıları atla (tekrarlı çözüm önleme)
            if i > index and sayilar[i] == sayilar[i - 1]:
                continue

            # SEÇ
            mevcut.append(sayilar[i])
            # İLERLE
            backtrack(i + 1, mevcut, mevcut_toplam + sayilar[i])
            # GERİ AL
            mevcut.pop()

    sayilar.sort()  # Sıralama, budamayı ve tekrar kontrolünü kolaylaştırır
    backtrack(0, [], 0)
    return sonuclar


print(f"\n🎯 Alt Küme Toplamı:")
sayilar = [2, 3, 7, 8, 10]
hedef = 11
sonuclar = alt_kume_toplam(sayilar, hedef)
print(f"  Sayılar: {sayilar}, Hedef: {hedef}")
print(f"  Çözümler:")
for cozum in sonuclar:
    print(f"    {cozum} = {sum(cozum)}")


# =============================================================================
# 📖 BÖLÜM 10: GRAPH DÜŞÜNCESİ (BFS & DFS) ★★★
# =============================================================================
"""
🧠 GRAPH (GRAF/ÇİZGE) NEDİR?

★★★ BU BÖLÜM ÇOK ÖNEMLİ! ★★★
Gerçek dünyadaki ilişkilerin %90'ı graph ile modellenebilir.

GRAPH = Düğümler (nodes) + Kenarlar (edges)

GERÇEK DÜNYA GRAPH ÖRNEKLERİ:
→ Sosyal ağ: Kişiler = düğüm, Arkadaşlık = kenar
→ Harita: Şehirler = düğüm, Yollar = kenar
→ İnternet: Web sayfaları = düğüm, Linkler = kenar
→ Dosya sistemi: Klasörler = düğüm, İçerme = kenar

İKİ TEMEL ARAMA:
1. BFS (Breadth-First Search) = Genişlik öncelikli arama
   → Komşulardan başla, katman katman genişle
   → EN KISA YOL bulmak için kullanılır
   → Queue (kuyruk) veri yapısı kullanır

2. DFS (Depth-First Search) = Derinlik öncelikli arama
   → Bir yolda sonuna kadar git, sonra geri dön
   → BAĞLANTI kontrolü, döngü tespiti için kullanılır
   → Stack (yığın) veya recursion kullanır
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 10: GRAPH DÜŞÜNCESİ")
print("=" * 70)

from collections import deque


class Graph:
    """
    Graph veri yapısı (Adjacency List ile).

    NEDEN ADJACENcy LIST?
    → Seyrek (sparse) graphlar için bellek verimli
    → Komşuları bulmak O(derece) - hızlı
    → Adjacency Matrix: O(V²) bellek, tüm kenarları saklasa da seyrek graphda israf
    """

    def __init__(self, yonlu=False):
        self.graph = {}  # {düğüm: [komşular]}
        self.yonlu = yonlu

    def dugum_ekle(self, dugum):
        if dugum not in self.graph:
            self.graph[dugum] = []

    def kenar_ekle(self, kaynak, hedef):
        self.dugum_ekle(kaynak)
        self.dugum_ekle(hedef)
        self.graph[kaynak].append(hedef)
        if not self.yonlu:
            self.graph[hedef].append(kaynak)

    def bfs(self, baslangic):
        """
        📝 BFS (Breadth-First Search / Genişlik Öncelikli Arama)

        🧠 DÜŞÜNCE SÜRECİ:

        BFS = Bir taşı suya at, dalgalar gibi yayıl
        → Önce 1 adım uzaktakileri gez
        → Sonra 2 adım uzaktakileri gez
        → Sonra 3 adım uzaktakileri gez
        → ...

        NEDEN QUEUE (KUYRUK)?
        → FIFO (First In, First Out): İlk giren ilk çıkar
        → Bu, "katman katman" gezmeyi garanti eder
        → Önce eklenen düğüm önce işlenir → yakın olanlar önce

        NE İŞE YARAR?
        → EN KISA YOL bulma (ağırlıksız graphlarda)
        → Seviye bazlı gezinme
        → "Bağlı mı?" kontrolü

        GÖRSEL:
              A
             / \
            B   C
           / \   \
          D   E   F

        BFS(A): A → B, C → D, E, F  (katman katman)
        DFS(A): A → B → D → E → C → F  (derine dal)
        """
        ziyaret_edildi = set()
        kuyruk = deque([baslangic])  # FIFO kuyruğu
        ziyaret_edildi.add(baslangic)
        sira = []

        while kuyruk:
            dugum = kuyruk.popleft()  # Kuyruğun BAŞINDAN al
            sira.append(dugum)

            for komsu in self.graph.get(dugum, []):
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append(komsu)  # Kuyruğun SONUNA ekle

        return sira

    def dfs(self, baslangic):
        """
        📝 DFS (Depth-First Search / Derinlik Öncelikli Arama)

        🧠 DÜŞÜNCE SÜRECİ:

        DFS = Bir yolda sonuna kadar git, çıkmaza girince geri dön
        → Labirenti çözmek gibi!
        → Hep ileri git, duvar görünce geri dön, başka yolu dene

        BFS'TEN FARKI:
        → BFS: Geniş gez (katman katman)
        → DFS: Derin gez (bir kolda sonuna kadar)

        KULLANIM ALANLARI:
        → Döngü tespiti
        → Topolojik sıralama
        → Bağlı bileşen bulma
        → Labirent çözme
        """
        ziyaret_edildi = set()
        sira = []

        def _dfs_recursive(dugum):
            ziyaret_edildi.add(dugum)
            sira.append(dugum)

            for komsu in self.graph.get(dugum, []):
                if komsu not in ziyaret_edildi:
                    _dfs_recursive(komsu)

        _dfs_recursive(baslangic)
        return sira

    def en_kisa_yol(self, baslangic, hedef):
        """
        📝 BFS ile en kısa yol bulma.

        🧠 MANTIK:
        → BFS zaten katman katman gezer
        → İlk hedefe ulaştığında o yol EN KISA yoldur
        → Her düğüm için "nereden geldim" bilgisini tut
        → Hedefe ulaşınca geri izle
        """
        ziyaret_edildi = set()
        kuyruk = deque([baslangic])
        ziyaret_edildi.add(baslangic)
        ebeveyn = {baslangic: None}  # "Nereden geldim?" haritası

        while kuyruk:
            dugum = kuyruk.popleft()

            if dugum == hedef:
                # Yolu geri izle
                yol = []
                mevcut = hedef
                while mevcut is not None:
                    yol.append(mevcut)
                    mevcut = ebeveyn[mevcut]
                return yol[::-1]  # Tersine çevir (başlangıçtan hedefe)

            for komsu in self.graph.get(dugum, []):
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    ebeveyn[komsu] = dugum
                    kuyruk.append(komsu)

        return None  # Yol yok


# Graph örneği: Şehir haritası
harita = Graph()
yollar = [
    ("İstanbul", "Ankara"),
    ("İstanbul", "Bursa"),
    ("Ankara", "Konya"),
    ("Ankara", "Eskişehir"),
    ("Bursa", "Eskişehir"),
    ("Eskişehir", "Konya"),
    ("Konya", "Antalya"),
    ("Antalya", "Mersin"),
    ("Ankara", "Kayseri"),
    ("Kayseri", "Mersin"),
]

for kaynak, hedef in yollar:
    harita.kenar_ekle(kaynak, hedef)

print(f"\n🗺️ Şehir Haritası Graph:")
print(f"  BFS (İstanbul'dan): {harita.bfs('İstanbul')}")
print(f"  DFS (İstanbul'dan): {harita.dfs('İstanbul')}")

# En kısa yol
print(f"\n  🛤️ En kısa yollar:")
for hedef in ["Antalya", "Mersin", "Konya"]:
    yol = harita.en_kisa_yol("İstanbul", hedef)
    if yol:
        print(f"    İstanbul → {hedef}: {' → '.join(yol)} ({len(yol)-1} adım)")


# --- Ada Sayma Problemi (BFS/DFS'in klasik uygulaması) ---
def ada_say(harita_grid):
    """
    📝 PROBLEM: (LeetCode #200 - Çok ünlü mülakat sorusu!)
    2D bir grid'de kaç ada var?
    1 = kara, 0 = su

    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1

    → 3 ada var

    🧠 DÜŞÜNCE SÜRECİ:

    BU BİR GRAPH PROBLEMİ!
    → Her hücre bir düğüm
    → Komşu kareler (yukarı, aşağı, sol, sağ) kenarlar
    → "Bağlı bileşen sayısı" = Ada sayısı

    ALGORİTMA:
    → Grid'i tara
    → "1" bulunca → ada sayısını artır
    → BFS/DFS ile o adanın TÜM hücrelerini ziyaret et
      (tekrar saymamak için "2" veya "ziyaret edildi" olarak işaretle)
    → Devam et

    NEDEN BFS/DFS?
    → Bir "1" hücresinden başlayıp o adanın tüm bağlı "1"lerini bulmak gerek
    → Bu tam olarak "bağlı bileşen bulma" problemidir
    """
    if not harita_grid or not harita_grid[0]:
        return 0

    satirlar = len(harita_grid)
    sutunlar = len(harita_grid[0])
    ada_sayisi = 0

    def bfs_ada(satir, sutun):
        """Bir adanın tüm hücrelerini BFS ile ziyaret et."""
        kuyruk = deque([(satir, sutun)])
        harita_grid[satir][sutun] = 0  # Ziyaret edildi olarak işaretle

        while kuyruk:
            r, c = kuyruk.popleft()

            # 4 yönü kontrol et (yukarı, aşağı, sol, sağ)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Sınır kontrolü + kara mı?
                if (0 <= nr < satirlar and 0 <= nc < sutunlar
                        and harita_grid[nr][nc] == 1):
                    harita_grid[nr][nc] = 0  # İşaretle
                    kuyruk.append((nr, nc))

    for i in range(satirlar):
        for j in range(sutunlar):
            if harita_grid[i][j] == 1:  # Yeni ada buldum!
                ada_sayisi += 1
                bfs_ada(i, j)  # Bu adanın tüm hücrelerini ziyaret et

    return ada_sayisi


# Test
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]
print(f"\n🏝️ Ada Sayma:")
print(f"  Grid:")
for satir in grid:
    print(f"    {satir}")
print(f"  Ada sayısı: {ada_say([satir[:] for satir in grid])}")


# =============================================================================
# 📖 BÖLÜM 11: HASH MAP DÜŞÜNCESİ ★★★
# =============================================================================
"""
🧠 HASH MAP NEDEN ★★★?

★★★ BU BELKİ EN ÖNEMLİ BÖLÜM! ★★★

"Eğer bir problemi O(n²)'den O(n)'e düşürmek istiyorsan,
muhtemelen cevap Hash Map (Dictionary)'dir."

Hash Map'in süper gücü:
→ Arama: O(1) ← LİSTEDE O(n)!
→ Ekleme: O(1)
→ Silme: O(1)

NE ZAMAN HASH MAP KULLAN?
→ "Bu elemanı daha önce gördüm mü?" → Hash Map
→ "Bu elemanın frekansı kaç?" → Hash Map
→ "İki elemanın toplamı X mi?" → Hash Map
→ "Şu ana kadar en çok/en az görülen ne?" → Hash Map

BİR YAZILIMCIYI "İYİ" YAPAN ŞEYLERDEN BİRİ:
"Hmm, bu O(n²) çözümü Hash Map ile O(n) yapabilir miyim?"
sorusunu REFLEKS olarak sormaktır.
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 11: HASH MAP DÜŞÜNCESİ ★★★")
print("=" * 70)


# --- PROBLEM 1: Two Sum (Hash Map ile) ---
def iki_toplam_hash(liste, hedef):
    """
    📝 PROBLEM: (LeetCode #1 - EN ÜNLü mülakat sorusu!)
    Listede toplamı hedef olan iki elemanın indexlerini bul.
    [2, 7, 11, 15], hedef=9 → [0, 1] çünkü 2+7=9

    🧠 DÜŞÜNCE EVRİMİ:

    BRUTE FORCE (O(n²)):
    → Her çifti dene → İç içe iki döngü

    HASH MAP (O(n)):
    → Her elemanı gezerken şunu sor:
      "Benim tamamlayıcım (hedef - ben) daha önce görüldü mü?"
    → Hash Map'te O(1)'de kontrol et!

    GÖRSEL:
    [2, 7, 11, 15], hedef = 9

    index 0: sayı=2, tamamlayıcı=9-2=7, görülen={}      → 7 yok, 2'yi ekle
    index 1: sayı=7, tamamlayıcı=9-7=2, görülen={2:0}    → 2 VAR! index 0'da!
    → Cevap: [0, 1]

    TOPLAM: Tek geçiş, O(n)!
    """
    gorulen = {}  # {sayı: index}

    for i, sayi in enumerate(liste):
        tamamlayici = hedef - sayi

        if tamamlayici in gorulen:  # O(1) arama!
            return [gorulen[tamamlayici], i]

        gorulen[sayi] = i  # Bu sayıyı kaydet

    return None


print(f"\n🎯 Two Sum (Hash Map):")
test_durumlar = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
]
for liste, hedef in test_durumlar:
    sonuc = iki_toplam_hash(liste, hedef)
    if sonuc:
        i, j = sonuc
        print(f"  {liste}, hedef={hedef} → index {sonuc}: "
              f"{liste[i]}+{liste[j]}={hedef}")


# --- PROBLEM 2: Grup Anagramları ---
def grup_anagram(kelimeler):
    """
    📝 PROBLEM: (LeetCode #49)
    Kelimeleri anagram gruplarına ayır.
    ["eat","tea","tan","ate","nat","bat"]
    → [["eat","tea","ate"], ["tan","nat"], ["bat"]]

    🧠 HASH MAP DÜŞÜNCE SÜRECİ:

    "Anagram olan kelimelerin ortak özelliği ne?"
    → Sıralandığında AYNI string olurlar!
    → "eat" → "aet", "tea" → "aet", "ate" → "aet"

    O zaman:
    → Sıralı hali ANAHTAR, orijinal kelimeler DEĞER
    → Hash Map: {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], ...}

    KARMAŞIKLIK: O(n × k log k)
    → n kelime var, her biri ortalama k uzunluğunda
    → Her kelimeyi sıralama O(k log k)
    → Hash Map'e ekleme O(1)
    """
    gruplar = {}

    for kelime in kelimeler:
        # Anahtarı oluştur: Sıralı harfler
        anahtar = ''.join(sorted(kelime))
        # NEDEN tuple değil de string? → String hash'lenir, list hash'lenmez
        # NEDEN sorted? → Anagramlar sıralandığında aynı olur

        if anahtar not in gruplar:
            gruplar[anahtar] = []
        gruplar[anahtar].append(kelime)

    return list(gruplar.values())


print(f"\n📚 Grup Anagramları:")
kelimeler = ["eat", "tea", "tan", "ate", "nat", "bat"]
gruplar = grup_anagram(kelimeler)
print(f"  Girdi: {kelimeler}")
print(f"  Gruplar:")
for grup in gruplar:
    print(f"    {grup}")


# --- PROBLEM 3: En Uzun Ardışık Seri ---
def en_uzun_ardisik(sayilar):
    """
    📝 PROBLEM: (LeetCode #128)
    Sırasız bir listede en uzun ardışık sayı serisinin uzunluğunu bul.
    [100, 4, 200, 1, 3, 2] → [1, 2, 3, 4] → uzunluk 4

    🧠 DÜŞÜNCE EVRİMİ:

    BRUTE FORCE: Sırala O(n log n), ardışıkları say
    HASH MAP: O(n)!

    AKILLI FİKİR:
    → Tüm sayıları SET'e koy (O(n))
    → Her sayı için kontrol et: "Bu sayı bir serinin BAŞLANGICI mi?"
      → Eğer sayı-1 SET'te YOKSA → Bu bir serinin başlangıcı!
      → Eğer sayı-1 SET'te VARSA → Bu zaten bir serinin ortasında, atla
    → Başlangıç noktasından ilerleyerek seriyi say

    NEDEN BU O(n)?
    → Her sayı EN FAZLA iki kez kontrol edilir:
      1. Başlangıç kontrolü sırasında
      2. Bir serinin parçası olarak sayılırken
    → Toplam: O(n)
    """
    if not sayilar:
        return 0

    sayi_seti = set(sayilar)  # O(n) ile set oluştur
    max_uzunluk = 0

    for sayi in sayi_seti:
        # BU KISI ÇOK AKILLICA:
        # Sadece seri başlangıçlarından başla!
        if sayi - 1 not in sayi_seti:  # Bu bir serinin BAŞLANGICI
            mevcut = sayi
            uzunluk = 1

            # Seriyi ilerleyerek say
            while mevcut + 1 in sayi_seti:  # O(1) arama!
                mevcut += 1
                uzunluk += 1

            max_uzunluk = max(max_uzunluk, uzunluk)

    return max_uzunluk


print(f"\n📈 En Uzun Ardışık Seri:")
test_listeleri = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
]
for liste in test_listeleri:
    sonuc = en_uzun_ardisik(liste)
    print(f"  {liste}")
    print(f"  → En uzun ardışık seri: {sonuc}")


# =============================================================================
# 📖 BÖLÜM 12: GERÇEK MÜLAKAT SORUARI VE ÇÖZÜM STRATEJİLERİ
# =============================================================================
"""
🧠 BİR PROBLEMİ GÖRDÜĞÜNDE HANGİ TEKNİĞİ KULLANACAĞINI
   NASIL ANLAYACAKSIN?

HIZLI KARAR HARİTASI:

Soru: "Sıralı dizi/listede arama"
→ İkili Arama (Binary Search)

Soru: "İki eleman toplamı", "palindrome", "sıralı dizide çift"
→ Two Pointer

Soru: "Ardışık alt dizi/substring", "pencere boyutu"
→ Sliding Window

Soru: "Minimum/maximum ... kaç farklı yol"
→ Dynamic Programming

Soru: "Tüm olasılıklar", "tüm kombinasyonlar/permütasyonlar"
→ Backtracking

Soru: "En kısa yol", "bağlantı", "ada", "seviye"
→ BFS / DFS (Graph)

Soru: "O(n²)'yi O(n) yap", "frekans", "daha önce gördüm mü"
→ Hash Map

Soru: "Her adımda en iyi seçim", "sıralama bazlı karar"
→ Greedy

Soru: "Büyük problemi küçük AYNI TÜRDE probleme böl"
→ Divide & Conquer
"""

print("\n" + "=" * 70)
print("📖 BÖLÜM 12: ÇÖZÜM STRATEJİ HARİTASI")
print("=" * 70)

# --- Kapanış: Her Şeyi Birleştiren Bir Problem ---
def kelime_merdiveni(baslangic, hedef, kelime_listesi):
    """
    📝 PROBLEM: (LeetCode #127 - Zor ama çok öğretici!)
    Bir kelimeden diğerine, her adımda sadece 1 harf değiştirerek ulaş.
    Her ara kelime sözlükte olmalı.

    "hit" → "hot" → "dot" → "dog" → "cog"

    🧠 BU PROBLEM BİRDEN FAZLA TEKNİK KULLANIR:

    1. GRAPH DÜŞÜNCESİ: Her kelime bir düğüm.
       1 harf farkla değişebilen kelimeler arasında kenar var.

    2. BFS: En kısa dönüşüm yolunu bulmak için.

    3. HASH MAP/SET: Kelime sözlüğünde hızlı arama için.

    ALGORİTMA:
    → Başlangıç kelimesinden BFS yap
    → Her adımda: kelimenin her harfini a-z ile değiştir
    → Yeni kelime sözlükte varsa → kuyruğa ekle
    → Hedefe ulaşınca → adım sayısını döndür
    """
    if hedef not in kelime_listesi:
        return 0, []

    kelime_seti = set(kelime_listesi)  # O(1) arama için
    kuyruk = deque([(baslangic, [baslangic])])  # (kelime, yol)
    ziyaret = {baslangic}

    while kuyruk:
        kelime, yol = kuyruk.popleft()

        if kelime == hedef:
            return len(yol), yol

        # Her pozisyondaki her harfi değiştir
        for i in range(len(kelime)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                yeni = kelime[:i] + c + kelime[i + 1:]

                if yeni in kelime_seti and yeni not in ziyaret:
                    ziyaret.add(yeni)
                    kuyruk.append((yeni, yol + [yeni]))

    return 0, []


print(f"\n🔤 Kelime Merdiveni (Graph + BFS + Hash):")
sozluk = ["hot", "dot", "dog", "lot", "log", "cog"]
adim, yol = kelime_merdiveni("hit", "cog", sozluk)
print(f"  'hit' → 'cog'")
print(f"  Sözlük: {sozluk}")
print(f"  Yol ({adim} adım): {' → '.join(yol)}")


# =============================================================================
# 🎯 ÖZET: USTALAŞMA YOLUNDA ÖĞRENDİKLERİN
# =============================================================================

print("\n" + "=" * 70)
print("🎯 USTALAŞMA YOLUNDA ÖĞRENDİKLERİN")
print("=" * 70)

ozet = """
📚 BU DOSYADA ÖĞRENDİKLERİN:

┌─────���───────────────────────────────────────────────────────────┐
│  TEKNİK              │  PROBLEM ÖRNEĞİ            │ ZORLUK    │
├─────────────────────────────────────────────────────────────────┤
│  Fonksiyon Tasarımı   │  Pure, Higher-Order, Closure │  ⭐⭐     │
│  Decorator            │  Süre ölçme, Loglama        │  ⭐⭐     │
│  Recursion            │  Permütasyon, Düzleştirme   │  ⭐⭐⭐   │
│  Two Pointer          │  Palindrome, İki Toplam     │  ⭐⭐     │
│  Sliding Window       │  Alt dizi, Tekrarsız string │  ⭐⭐⭐   │
│  Greedy               │  Etkinlik Seçimi, Birleştir │  ⭐⭐     │
│  Divide & Conquer     │  Max Alt Dizi (Kadane)      │  ⭐⭐⭐   │
│  Dynamic Programming  │  Knapsack, LCS, Para Bozma  │  ⭐⭐⭐⭐ │
│  Backtracking         │  N-Queens, Alt Küme Toplamı │  ⭐⭐⭐   │
│  Graph (BFS/DFS)      │  En Kısa Yol, Ada Sayma     │  ⭐⭐⭐⭐ │
│  Hash Map Düşüncesi   │  Two Sum, Anagram, Ardışık  │  ⭐⭐⭐   │
└─────────────────────────────────────────────────────────────────┘

🏆 SENİ "USTALAŞTIRAN" KONULAR (Bunları mutlaka derinlemesine öğren):

  1️⃣  DYNAMIC PROGRAMMING
     → Mülakatların en zor ama en çok sorulan konusu
     → "Alt problem tanımla + Geçiş denklemi yaz + Tablo doldur"

  2️⃣  GRAPH + BFS/DFS
     → Gerçek dünya problemlerinin çoğu graph
     → Kelime Merdiveni gibi: "Graph gibi görünmeyen graph problemleri"

  3️⃣  HASH MAP DÜŞÜNCESİ
     → O(n²) → O(n) dönüşümünün anahtarı
     → "Daha önce gördüm mü?" refleksi

🎯 SIRADAN YAZILIMCI    →    GERÇEK PROBLEM ÇÖZÜCÜ
   "Kodu çalıştırdım"        "Karmaşıklığı biliyorum"
   "İlk çözümü yazdım"       "3 farklı çözüm düşündüm"
   "Test etmedim"             "Edge case'leri kapsadım"
   "Kopyala yapıştır"         "Kalıbı tanıdım"
   "Sadece Python bilirim"    "Mantığı biliyorum, dil araç"

📌 PRATIK PLANI:
   Hafta 1-2: Two Pointer + Sliding Window (kolay)
   Hafta 3-4: Hash Map + Greedy (orta)
   Hafta 5-6: Recursion + Backtracking (orta-zor)
   Hafta 7-10: Dynamic Programming (zor)
   Hafta 11-12: Graph + BFS/DFS (orta-zor)

   Her hafta LeetCode'dan 3-5 soru çöz!
   → leetcode.com (Easy → Medium → Hard)
   → Her soruyu ÖNCE kendin çözmeye çalış (30 dk)
   → Çözemediysen çözümü oku ama NEDEN öyle olduğunu ANLA
"""

print(ozet)

print("=" * 70)
print("🚀 'Algoritma mantığı güçlü olan, her dilde güçlüdür.'")
print("    Bu dosyayı çalıştır, oku, değiştir, deney yap!")
print("    python algoritma_ustasi.py")
print("=" * 70)