# ═══════════════════════════════════════════════════════════════
# MAXIMUM SUBARRAY - Kadane's Algorithm
# Bir dizideki ardışık elemanların en büyük toplamını bul
# Zaman: O(n), Alan: O(1)
# ═══════════════════════════════════════════════════════════════

def max_subarray(nums):
    """
    Temel Fikir:
    ───────────
    Her elemanda karar ver:
    → Önceki toplamla devam mı etsem, yoksa buradan yeniden mi başlasam?
    
    Eğer önceki toplam negatifse → Yeniden başla (negatif toplam yük olur)
    Eğer önceki toplam pozitifse → Devam et (katkı sağlar)
    
    max() fonksiyonu: İki değerden büyüğünü döner
    max(3, 5) → 5
    max(-2, 0) → 0
    
    Trace: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ─────
    i=0: num=-2 → current=max(-2, 0+(-2))=max(-2,-2)=-2  → best=-2
    i=1: num=1  → current=max(1, -2+1)=max(1,-1)=1       → best=1
    i=2: num=-3 → current=max(-3, 1+(-3))=max(-3,-2)=-2  → best=1
    i=3: num=4  → current=max(4, -2+4)=max(4,2)=4        → best=4
    i=4: num=-1 → current=max(-1, 4+(-1))=max(-1,3)=3    → best=4
    i=5: num=2  → current=max(2, 3+2)=max(2,5)=5         → best=5
    i=6: num=1  → current=max(1, 5+1)=max(1,6)=6         → best=6 ✓
    i=7: num=-5 → current=max(-5, 6+(-5))=max(-5,1)=1    → best=6
    i=8: num=4  → current=max(4, 1+4)=max(4,5)=5         → best=6
    
    return 6 → Alt dizi: [4, -1, 2, 1]
    """
    current_sum = 0
    best_sum = nums[0]      # En küçük olası değerle başla
    
    for num in nums:
        # Ya bu elemanla yeniden başla, ya da önceki toplama ekle
        current_sum = max(num, current_sum + num)
        # En iyi toplamı güncelle
        best_sum = max(best_sum, current_sum)
    
    return best_sum

# TEST
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
print(max_subarray([1]))                                   # 1
print(max_subarray([5, 4, -1, 7, 8]))                     # 23