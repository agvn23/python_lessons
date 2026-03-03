# --- FONKSİYONLAR ---
# Fonksiyon = belirli bir görevi yapan, tekrar kullanılabilir kod bloğu
# def anahtar_kelimesi ile tanımlanır

def selamla(isim):
    """Bu fonksiyon verilen ismi selamlar."""  # Docstring (açıklama)
    return f"Merhaba, {isim}!"

sonuc = selamla("Abdulkadir")
print(sonuc)  # "Merhaba, Abdulkadir!"

# --- PARAMETRELER ---

# Varsayılan parametre (Default parameter)
def us_al(taban, us=2):
    """Varsayılan olarak kare alır."""
    return taban ** us

print(us_al(5))      # 25  → 5² (us varsayılan 2)
print(us_al(5, 3))   # 125 → 5³

# Birden fazla değer döndürme
def bolme_islemi(a, b):
    """Bölüm ve kalanı döner."""
    bolum = a // b
    kalan = a % b
    return bolum, kalan   # Tuple olarak döner

b, k = bolme_islemi(17, 5)
print(f"Bölüm: {b}, Kalan: {k}")  # Bölüm: 3, Kalan: 2