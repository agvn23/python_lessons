# ═══════════════════════════════════════════════════════════════
# TWO SUM - BRUTE FORCE (Kaba Kuvvet) Çözümü
# Zaman Karmaşıklığı: O(n²) → İç içe iki döngü
# Alan Karmaşıklığı:  O(1) → Ekstra alan kullanmıyoruz
# ═══════════════════════════════════════════════════════════════

def two_sum_brute(nums, target):
    """
    Her elemanı, kendinden sonraki her elemanla dener.
    
    Mantık:
    -------
    nums = [2, 7, 11, 15], target = 9
    
    i=0, j=1: nums[0]+nums[1] = 2+7 = 9 ✓ BULUNDU! → [0, 1]
    
    Eğer ilk denemede bulmasaydık:
    i=0, j=2: 2+11=13 ✗
    i=0, j=3: 2+15=17 ✗
    i=1, j=2: 7+11=18 ✗
    ... şeklinde devam ederdi
    """
    # len(nums) → Listenin uzunluğunu döner
    # range(len(nums)) → 0'dan n-1'e kadar index üretir
    for i in range(len(nums)):
        # i+1'den başlıyoruz çünkü:
        # 1) Kendisiyle kendisini toplamak yasak
        # 2) Önceki çiftleri tekrar kontrol etmeye gerek yok
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  # Çözüm bulunamazsa (ama problem garanti diyor)

# TEST
print(two_sum_brute([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum_brute([3, 2, 4], 6))         # [1, 2]
print(two_sum_brute([3, 3], 6))            # [0, 1]