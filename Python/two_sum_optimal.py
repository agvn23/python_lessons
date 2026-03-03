# ═══════════════════════════════════════════════════════════════
# TWO SUM - HASH MAP (Sözlük) Çözümü
# Zaman Karmaşıklığı: O(n)   → Tek döngü
# Alan Karmaşıklığı:  O(n)   → Sözlük için ekstra alan
# ═══════════════════════════════════════════════════════════════

def two_sum_optimal(nums, target):
    """
    Temel Fikir:
    ───────────
    Eğer target = 9 ve şu anki sayı 2 ise,
    aradığımız "tamamlayıcı" (complement) = 9 - 2 = 7
    
    Soru: 7 daha önce gördüğümüz bir sayı mı?
    → Evetse: İndexlerini döndür
    → Hayırsa: 2'yi "gördüklerimiz" sözlüğüne ekle, devam et
    
    Neden O(n)?
    ──────────
    Sözlükte arama (lookup) O(1) sürer.
    Listeyi sadece bir kez geziyoruz → n eleman × O(1) arama = O(n)
    
    Adım adım:
    ──────────
    nums = [2, 7, 11, 15], target = 9
    
    Adım 1: num=2, complement=9-2=7, seen={} → 7 yok → seen={2:0}
    Adım 2: num=7, complement=9-7=2, seen={2:0} → 2 VAR! → return [0, 1]
    """
    # seen sözlüğü: {sayı_değeri: index}
    # Gördüğümüz her sayıyı ve index'ini kaydediyoruz
    seen = {}
    
    # enumerate(nums) → Her adımda (index, değer) çifti verir
    # i = index, num = değer
    for i, num in enumerate(nums):
        # Tamamlayıcıyı hesapla
        complement = target - num
        
        # Tamamlayıcı daha önce görüldü mü?
        if complement in seen:       # O(1) arama - sözlükte key aramak çok hızlı
            return [seen[complement], i]
        
        # Bu sayıyı sözlüğe kaydet
        seen[num] = i
    
    return []

# TEST
print(two_sum_optimal([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum_optimal([3, 2, 4], 6))         # [1, 2]
print(two_sum_optimal([3, 3], 6))            # [0, 1]

# ═══════════════════════════════════════════════════════════════
# KARŞILAŞTIRMA:
# ─────────────
# Brute Force: O(n²) → 10,000 eleman = ~100,000,000 işlem
# Hash Map:    O(n)  → 10,000 eleman = ~10,000 işlem
# → Hash Map yaklaşık 10,000 kat daha hızlı!
# ═══════════════════════════════════════════════════════════════