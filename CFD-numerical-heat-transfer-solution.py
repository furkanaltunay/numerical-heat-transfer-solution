import math
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

TA = 560
TB = 660
q= 15000000
k= 7.5
dx=0.075/10
A= 1
L=0.075
x=0.075

table = PrettyTable()
table.field_names = ["x", "Analitik Sonuç (K)"]
T2 = []
for i in range(21):
    x = i/10*(L/2)
    t = (((TB-TA)/L) + ((q/(2*k))*(L-x)))*x+TA
    T2.append(float(t))
    table.add_row([x, t])

print(table)

print([T2[1], T2[3], T2[5], T2[7], T2[9], T2[11], T2[13], T2[15], T2[17], T2[19]])

# Grafikte sıcaklık değerlerini gösterme
x2_values = np.linspace(0, 0.075, 21)
plt.plot(x2_values, T2, label="Analitik")
plt.xlabel("Mesafe (m)")
plt.ylabel("Sıcaklık (K)")
plt.title("Sıcaklık Dağılımı")
plt.legend()

#iç hücre (2,3,4,5,6,7,8,9 düğüm noktalarındaki kontrol hacimleri için geçerlidir)
aw1= float((-k/dx)*A)
ae1= float((-k/dx)*A)
sp1= 0
ap1= float(-(aw1+ae1-sp1))
su1= float(q*A*dx)

#soldaki sınır hücre (1 düğüm noktaları için)
aw2= 0
ae2= float((-k/dx)*A)
sp2= float(2*((k/dx)*A))
ap2= float(-(aw2+ae2-sp2))
su2= float(q*A*dx + (2*((k/dx)*A))*TA)

#soldaki sınır hücre (10 düğüm noktaları için)
aw3= float((-k/dx)*A)
ae3= 0
sp3= float(2*((k/dx)*A))
ap3= float(-(aw2+ae2-sp2))
su3= float(q*A*dx + (2*((k/dx)*A))*TB)

table = PrettyTable()
table.field_names = ["Hücre", "aw", "ae", "ap", "sp", "su"]
table.add_row(["1", aw2, ae2, ap2, sp2, su2])
for i in range(2, 10):
    table.add_row([str(i), aw1, ae1, ap1, sp1, su1])
table.add_row(["10", aw3, ae3, ap3, sp3, su3])

print(table)

# Katsayı matrisi A
A = np.array([[ap2, ae2, 0, 0, 0, 0, 0, 0, 0, 0],
              [aw1, ap1, ae1, 0, 0, 0, 0, 0, 0, 0],
              [0, aw1, ap1, ae1, 0, 0, 0, 0, 0, 0],
              [0, 0, aw1, ap1, ae1, 0, 0, 0, 0, 0],
              [0, 0, 0, aw1, ap1, ae1, 0, 0, 0, 0],
              [0, 0, 0, 0, aw1, ap1, ae1, 0, 0, 0],
              [0, 0, 0, 0, 0, aw1, ap1, ae1, 0, 0],
              [0, 0, 0, 0, 0, 0, aw1, ap1, ae1, 0],
              [0, 0, 0, 0, 0, 0, 0, aw1, ap1, ae1,],
              [0, 0, 0, 0, 0, 0, 0, 0, aw3, ap3,]])

# Sabit terim matrisi C
C = np.array([[su2], [su1], [su1], [su1], [su1], [su1], [su1], [su1], [su1], [su3]])

# Denklemi çözerek sıcaklık değerlerini bulma
T = np.linalg.inv(A) @ C
print("Nümerik Sonuçlar")
table = PrettyTable()
table.field_names = ["Düğüm Noktası", "Sıcaklık (K)"]
for i, temp in enumerate(T):
    table.add_row([str(i+1), round(float(temp), 2)])
print(table)

#Yüzde hata hesaplama
T22 = ([T2[1], T2[3], T2[5], T2[7], T2[9], T2[11], T2[13], T2[15], T2[17], T2[19]])
for i in range(1, 11):
    hata_yuzdesi = abs(T22[i-1] - T[i-1]) / T22[i-1] * 100
    print(f"{i}. ölçümün yüzde hatası: {hata_yuzdesi[0]:.2f}%")

# Grafikte sıcaklık değerlerini gösterme
x_values = np.linspace(0.00375, 0.07125, 10)

plt.scatter(x_values, T, color='red', label="Sayısal")
plt.scatter(0, TA, color='red')
plt.scatter(0.075, TB, color='red')
plt.xlabel("Mesafe, x (m)")
plt.ylabel("Sıcaklık, T (K)")
plt.title("Sıcaklık Dağılımı")
plt.legend()
plt.grid(True)
plt.show()




