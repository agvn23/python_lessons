# --- QUEUE (KUYRUK) ---
# Düşün: Market kuyruğu → İlk gelen ilk çıkar
# Python'da collections.deque kullanılır (list'ten daha verimli)

from collections import deque

#  TEMEL İŞLEMLER:
#  enqueue → .append()    → Kuyruğun sonuna ekle
#  dequeue → .popleft()   → Kuyruğun başından çıkar
#  peek    → queue[0]     → Baştakine bak

kuyruk = deque()

# Enqueue (ekleme)
kuyruk.append("Kişi 1")
kuyruk.append("Kişi 2")
kuyruk.append("Kişi 3")
print(kuyruk)           # deque(['Kişi 1', 'Kişi 2', 'Kişi 3'])

# Dequeue (çıkarma - baştan)
print(kuyruk.popleft())  # "Kişi 1" → İlk gelen ilk çıkar
print(kuyruk)            # deque(['Kişi 2', 'Kişi 3'])

# Peek
print(kuyruk[0])         # "Kişi 2"