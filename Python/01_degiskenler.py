# --- DEĞİŞKENLER (Variables) ---
# Değişken = bir değeri hafızada tutan isimlendirilmiş kutu

isim = "Abdulkadir"      # str   (string - metin)
yas = 25                  # int   (integer - tam sayı)
boy = 1.78                # float (ondalıklı sayı)
ogrenci_mi = True         # bool  (boolean - True/False)

# type() fonksiyonu: bir değişkenin tipini söyler
print(type(isim))         # <class 'str'>
print(type(yas))          # <class 'int'>
print(type(boy))          # <class 'float'>
print(type(ogrenci_mi))   # <class 'bool'>

# --- TEMEL OPERATÖRLER ---
a = 10
b = 3

print(a + b)    # 13   → Toplama
print(a - b)    # 7    → Çıkarma
print(a * b)    # 30   → Çarpma
print(a / b)    # 3.33 → Bölme (her zaman float döner)
print(a // b)   # 3    → Tam bölme (floor division - ondalığı atar)
print(a % b)    # 1    → Mod (kalan) → 10'u 3'e böl, kalan 1
print(a ** b)   # 1000 → Üs alma → 10³ = 1000