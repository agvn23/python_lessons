# ═══════════════════════════════════════════════════════════════
# DESTINATION CITY - Brute Force Çözümü (Senin Çözümün)
# Zaman Karmaşıklığı: O(n²) → İç içe iki döngü
# Alan Karmaşıklığı:  O(1) → Ekstra alan yok
# ═══════════════════════════════════════════════════════════════

def dest_city_brute(paths):
    """
    Mantık:
    ──────
    Her yolun hedef şehrini (city_b) al.
    Bu hedef şehir, başka bir yolun kaynak şehri mi kontrol et.
    Eğer hiçbir yolun kaynağı değilse → Bu varış şehri!
    
    Kullanılan Yapılar:
    ──────────────────
    - range(len(paths)) → 0'dan paths uzunluğu-1'e kadar index üretir
    - paths[i][0]       → i. yolun kaynak şehri (cityA)
    - paths[i][1]       → i. yolun hedef şehri (cityB)
    - break             → İç döngüyü durdurur (bu şehir kaynak olarak
    -                      bulundu, daha aramaya gerek yok)
    
    Trace:
    ─────
    paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]
    
    i=0: city_b = "New York"
         j=1: paths[0][1]="New York" == paths[1][0]="New York" → Eşleşti!
         → is_destination = False → Devam
    
    i=1: city_b = "Lima"
         j=2: paths[1][1]="Lima" == paths[2][0]="Lima" → Eşleşti!
         → is_destination = False → Devam
    
    i=2: city_b = "Sao Paulo"
         j=0: paths[2][1]="Sao Paulo" != paths[0][0]="London" ✗
         j=1: paths[2][1]="Sao Paulo" != paths[1][0]="New York" ✗
         → Hiçbiriyle eşleşmedi → is_destination = True
         → return "Sao Paulo" ✓
    """
    for i in range(len(paths)):
        city_b = paths[i][1]     # Hedef şehir
        is_destination = True     # Varsayım: bu varış şehri

        for j in range(len(paths)):
            if i != j and paths[i][1] == paths[j][0]:
                # paths[i][1] = hedef şehir
                # paths[j][0] = başka bir yolun kaynak şehri
                # Eğer eşitlerse → Bu şehir bir yere daha gidiyor → Varış değil
                is_destination = False
                break           # Daha aramaya gerek yok

        if is_destination:
            return city_b

    return None

# TEST
print(dest_city_brute([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
# → "Sao Paulo"