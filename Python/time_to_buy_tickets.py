# ═══════════════════════════════════════════════════════════════
# TIME TO BUY TICKETS - Queue (Kuyruk) Simülasyonu
# Zaman Karmaşıklığı: O(n × m) → n=kişi sayısı, m=max bilet
# Alan Karmaşıklığı:  O(n)     → Queue için
# ═══════════════════════════════════════════════════════════════

from collections import deque
# deque (double-ended queue) = çift taraflı kuyruk
# .append()   → Sağdan ekle   O(1)
# .popleft()  → Soldan çıkar  O(1)  ← Normal listede bu O(n) olurdu!

def time_to_buy_tickets(tickets, k):
    """
    Algoritma:
    ─────────
    1. Her kişiyi (index, kalan_bilet) olarak queue'ya ekle
    2. Her saniye:
       a. Kuyruğun başından bir kişi çıkar
       b. Bilet sayısını 1 azalt
       c. Eğer hedef kişiyse (index == k) VE biletleri bittiyse → Süreyi döndür
       d. Hâlâ bileti varsa → Kuyruğun sonuna tekrar ekle
    
    Kullanılan Fonksiyonlar:
    ───────────────────────
    - deque()        → Boş kuyruk oluşturur
    - .append()      → Kuyruğun sonuna ekle
    - .popleft()     → Kuyruğun başından çıkar
    - enumerate()    → (index, değer) çiftleri verir
    
    Trace: tickets = [2, 3, 2], k = 2
    ──────
    Başlangıç queue: [(0,2), (1,3), (2,2)]
    
    Saniye 1: (0,2) çıkar → bilet: 2-1=1 → 1>0 → tekrar ekle
              queue: [(1,3), (2,2), (0,1)]     süre: 1
    
    Saniye 2: (1,3) çıkar → bilet: 3-1=2 → 2>0 → tekrar ekle
              queue: [(2,2), (0,1), (1,2)]     süre: 2
    
    Saniye 3: (2,2) çıkar → bilet: 2-1=1 → index=2=k ama 1>0 → tekrar ekle
              queue: [(0,1), (1,2), (2,1)]     süre: 3
    
    Saniye 4: (0,1) çıkar → bilet: 1-1=0 → 0=0 → kuyruğu terk eder
              queue: [(1,2), (2,1)]            süre: 4
    
    Saniye 5: (1,2) çıkar → bilet: 2-1=1 → 1>0 → tekrar ekle
              queue: [(2,1), (1,1)]            süre: 5
    
    Saniye 6: (2,1) çıkar → bilet: 1-1=0 → index=2=k VE bilet=0 → BULDUK!
              return 6 ✓
    """
    # Queue oluştur: her eleman (orijinal_index, kalan_bilet)
    queue = deque()
    for i, ticket_count in enumerate(tickets):
        queue.append((i, ticket_count))
    
    # Alternatif (daha kısa):
    # queue = deque(enumerate(tickets))  → Aynı sonucu verir
    
    time = 0    # Geçen süre (saniye sayacı)
    
    while queue:                        # Queue boş olana kadar
        index, remaining = queue.popleft()   # Baştaki kişiyi çıkar
        remaining -= 1                        # 1 bilet aldı
        time += 1                             # 1 saniye geçti
        
        if index == k and remaining == 0:
            # Hedef kişi VE biletleri bitti → Cevap bulundu!
            return time
        
        if remaining > 0:
            # Hâlâ bileti var → Kuyruğun sonuna geç
            queue.append((index, remaining))
    
    return time   # Buraya normalde ulaşılmaz

# TEST
print(time_to_buy_tickets([2, 3, 2], 2))      # 6
print(time_to_buy_tickets([5, 1, 1, 1], 0))   # 8