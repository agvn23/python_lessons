# --- SÖZLÜKLER (Dictionaries) ---
# Dict = anahtar:değer (key:value) çiftleri tutan yapı
# Arama hızı O(1) → Çok hızlı!

ogrenci = {
    "isim": "Abdulkadir",
    "yas": 25,
    "dersler": ["Python", "Algoritmalar"]
}

# Erişim
print(ogrenci["isim"])          # "Abdulkadir"
print(ogrenci.get("yas"))       # 25
print(ogrenci.get("adres", "Bulunamadı"))  # "Bulunamadı" → Yoksa varsayılan döner

# Ekleme / Güncelleme
ogrenci["email"] = "test@test.com"   # Yeni anahtar ekler
ogrenci["yas"] = 26                   # Var olan anahtarı günceller

# Silme
del ogrenci["email"]

# --- ÖNEMLİ DICT FONKSİYONLARI ---
print(ogrenci.keys())    # dict_keys(['isim', 'yas', 'dersler'])  → Tüm anahtarlar
print(ogrenci.values())  # dict_values([...])                      → Tüm değerler
print(ogrenci.items())   # dict_items([('isim','Abdulkadir'),...]) → Çiftler

# "in" operatörü → Anahtarın sözlükte olup olmadığını kontrol eder
print("isim" in ogrenci)   # True
print("adres" in ogrenci)  # False