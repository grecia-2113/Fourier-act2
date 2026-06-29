Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000                # Frecuencia de muestreo
T = 1                    # Duración en segundos
t = np.linspace(0, T, fs, endpoint=False)

# ==========================
# SEÑALES
# ==========================

# Señal senoidal
f = 5
senal_seno = np.sin(2 * np.pi * f * t)

# Pulso rectangular
pulso = np.where((t >= 0.4) & (t <= 0.6), 1, 0)

# Escalón unitario
escalon = np.where(t >= 0.5, 1, 0)

# ==========================
# FUNCIÓN FFT
# ==========================
def analizar_fft(signal, titulo):
    N = len(signal)
    fft_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, 1/fs)

    magnitud = np.abs(fft_signal)
    fase = np.angle(fft_signal)

...     plt.figure(figsize=(12,4))
...     plt.subplot(1,2,1)
...     plt.plot(freqs[:N//2], magnitud[:N//2])
...     plt.title(f'Magnitud - {titulo}')
...     plt.xlabel('Frecuencia (Hz)')
...     plt.ylabel('Magnitud')
... 
...     plt.subplot(1,2,2)
...     plt.plot(freqs[:N//2], fase[:N//2])
...     plt.title(f'Fase - {titulo}')
...     plt.xlabel('Frecuencia (Hz)')
...     plt.ylabel('Fase')
...     plt.tight_layout()
...     plt.show()
... 
... # ==========================
... # GRÁFICAS EN TIEMPO
... # ==========================
... 
... plt.figure(figsize=(12,6))
... 
... plt.subplot(3,1,1)
... plt.plot(t, senal_seno)
... plt.title('Señal senoidal')
... 
... plt.subplot(3,1,2)
... plt.plot(t, pulso)
... plt.title('Pulso rectangular')
... 
... plt.subplot(3,1,3)
... plt.plot(t, escalon)
... plt.title('Escalón unitario')
... 
... plt.tight_layout()
... plt.show()
... 
... # FFT
... analizar_fft(senal_seno, "Senoidal")
... analizar_fft(pulso, "Pulso Rectangular")
