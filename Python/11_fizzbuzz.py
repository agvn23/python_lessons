# ═══════════════════════════════════════════════════════════════
# FIZZBUZZ
# 1'den n'e kadar sayıları yazdır:
# - 3'e bölünüyorsa → "Fizz"
# - 5'e bölünüyorsa → "Buzz"
# - Her ikisine bölünüyorsa → "FizzBuzz"
# - Hiçbirine bölünmüyorsa → Sayının kendisi
# ═══════════════════════════════════════════════════════════════

def fizzbuzz(n):
    """
    Kullanılan kavramlar:
    - % (modulo): Bölme işleminden kalanı verir
      15 % 3 = 0 → 3'e tam bölünür
      15 % 5 = 0 → 5'e tam bölünür
      7 % 3 = 1  → 3'e tam bölünmez
    - if/elif/else: Koşul kontrol zinciri
      İlk doğru olan koşul çalışır, geri kalanlar atlanır
      ÖNEMLİ: "her ikisine bölünme" kontrolü İLK sırada olmalı!
    """
    result = []
    
    for i in range(1, n + 1):      # 1'den n'e kadar (n dahil)
        if i % 3 == 0 and i % 5 == 0:    # ÖNCELİKLE: Her ikisine?
            result.append("FizzBuzz")
        elif i % 3 == 0:                   # Sadece 3'e?
            result.append("Fizz")
        elif i % 5 == 0:                   # Sadece 5'e?
            result.append("Buzz")
        else:                              # Hiçbirine bölünmüyor
            result.append(str(i))          # str(i): int → string çevirimi
    
    return result

# TEST
for item in fizzbuzz(15):
    print(item)
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz