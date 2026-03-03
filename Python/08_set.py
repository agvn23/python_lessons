# --- SET (KÜME) ---
# Set = sırasız, benzersiz elemanlar tutan yapı
# Aynı eleman iki kez bulunamaz
# Arama hızı O(1) → Dict gibi hızlı

sayilar = {1, 2, 3, 3, 4, 4, 5}
print(sayilar)           # {1, 2, 3, 4, 5} → Tekrarlar silindi

# .add(x) → Eleman ekle
sayilar.add(6)

# .discard(x) → Eleman sil (yoksa hata vermez)
sayilar.discard(3)

# Set işlemleri
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # {1, 2, 3, 4, 5, 6}  → Birleşim (Union)
print(a & b)    # {3, 4}               → Kesişim (Intersection)
print(a - b)    # {1, 2}               → Fark (Difference)