import numpy as np
import matplotlib.pyplot as plt

# 1. Ayarlar: Çekirdek ve Hareket frekansları
f1 = 5   # Yavaş dalga (Temel yapı)
f2 = 25  # Hızlı dalga (Detay/Hareket)

# 2. Zaman ekseni
zaman = np.linspace(0, 1, 1000)

# 3. İki ayrı frekansın oluşturulması
dalga1 = np.sin(2 * np.pi * f1 * zaman)
dalga2 = 0.3 * np.sin(2 * np.pi * f2 * zaman) # Bu biraz daha küçük bir dalga

# 4. İki frekansın "Ekilmesi" (Birleşimi)
birlesik_hareket = dalga1 + dalga2

# 5. Görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(zaman, birlesik_hareket, color='purple', label='Bileşik Frekans')
plt.title("İki Frekansın Birleşimi: Çekirdek ve Hareket")
plt.grid(True)
plt.show()
