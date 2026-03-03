# --- LİSTELER (Lists) ---
# Liste = sıralı, değiştirilebilir, birden fazla değer tutan yapı
# Index: 0'dan başlar!

meyveler = ["elma", "armut", "muz", "çilek"]
#  index:     0       1       2       3
# negatif:   -4      -3      -2      -1

# Erişim (Accessing)
print(meyveler[0])     # "elma"   → İlk eleman
print(meyveler[-1])    # "çilek"  → Son eleman
print(meyveler[1:3])   # ["armut", "muz"] → Slicing: index 1'den 3'e kadar (3 hariç)

# --- TEMEL LİSTE FONKSİYONLARI ---

# len() → Listenin uzunluğunu (eleman sayısını) döner
print(len(meyveler))   # 4

# .append(x) → Listenin SONUNA bir eleman ekler
meyveler.append("kivi")
print(meyveler)        # ["elma", "armut", "muz", "çilek", "kivi"]

# .insert(index, x) → Belirtilen index'e eleman ekler
meyveler.insert(1, "portakal")
print(meyveler)        # ["elma", "portakal", "armut", "muz", "çilek", "kivi"]

# .remove(x) → İlk bulduğu x değerini siler
meyveler.remove("muz")
print(meyveler)        # ["elma", "portakal", "armut", "çilek", "kivi"]

# .pop(index) → Belirtilen index'teki elemanı çıkarır ve döner
cikarilan = meyveler.pop(0)
print(cikarilan)       # "elma"
print(meyveler)        # ["portakal", "armut", "çilek", "kivi"]

# .sort() → Listeyi sıralar (yerinde - in-place)
sayilar = [5, 2, 8, 1, 9]
sayilar.sort()
print(sayilar)         # [1, 2, 5, 8, 9]

# .reverse() → Listeyi tersine çevirir
sayilar.reverse()
print(sayilar)         # [9, 8, 5, 2, 1]

# "in" operatörü → Bir elemanın listede olup olmadığını kontrol eder
print("armut" in meyveler)   # True
print("ananas" in meyveler)  # False