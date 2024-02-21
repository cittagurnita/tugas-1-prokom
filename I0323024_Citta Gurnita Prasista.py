
# Tugas I Mata Kuliah Progama Komputer
# Citta Gurnita Prasista / I0323024

# 8888 detik ke jam, menit, detik
import math

x     = 8888

jam   = x / 3600
jam   = math.floor(jam)

sisa  = x - (jam * 3600)

menit = sisa / 60
menit = math.floor(menit)

detik = sisa - (menit * 60)

print(jam, 'jam,', menit, 'menit,', detik, 'detik.')