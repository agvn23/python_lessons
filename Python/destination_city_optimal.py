# ═══════════════════════════════════════════════════════════════
# DESTINATION CITY - Set Çözümü
# Zaman Karmaşıklığı: O(n) → İki ayrı döngü (iç içe değil)
# Alan Karmaşıklığı:  O(n) → Set için ekstra alan
# ═══════════════════════════════════════════════════════════════

def dest_city_optimal(paths):
    """
    Temel Fikir:
    ───────────
    1. Tüm KAYNAK şehirleri bir set'e topla
    2. Tüm HEDEF şehirleri kontrol et
    3. Hangi hedef şehir kaynak set'inde YOK → O varış şehri
    
    Neden Set?
    ─────────
    Set'te "var mı?" sorusu O(1) sürer (hash table yapısı).
    Liste'de bu soru O(n) sürer (tek tek bakmak gerekir).
    
    Trace:
    ─────
    paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]
    
    Adım 1: Kaynak set'i oluştur
    sources = {"London", "New York", "Lima"}
    
    Adım 2: Hedef şehirleri kontrol et
    "New York" in sources? → Evet → Varış değil
    "Lima" in sources?     → Evet → Varış değil
    "Sao Paulo" in sources? → HAYIR → Bu varış şehri!
    """
    # Set comprehension: her yolun kaynak şehrini (path[0]) topla
    # {expression for item in iterable} → Set oluşturur
    sources = set()
    for path in paths:
        sources.add(path[0])
    
    # Alternatif (Set Comprehension - daha kısa yazım):
    # sources = {path[0] for path in paths}
    
    # Her hedef şehri kontrol et
    for path in paths:
        if path[1] not in sources:    # O(1) arama
            return path[1]
    
    return None

# TEST
print(dest_city_optimal([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
# → "Sao Paulo"
print(dest_city_optimal([["B","C"],["D","B"],["C","A"]]))
# → "A"
print(dest_city_optimal([["A","Z"]]))
# → "Z"

# ═══════════════════════════════════════════════════════════════
# KARŞILAŞTIRMA:
# Brute Force: O(n²) → 100 yol = ~10,000 kontrol
# Set Çözümü:  O(n)  → 100 yol = ~200 kontrol
# ═══════════════════════════════════════════════════════════════