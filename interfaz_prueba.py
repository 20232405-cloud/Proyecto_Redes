import threading
import serial
import tkinter as tk
from tkinter import ttk
from indicadores import calcular_ping, calcular_jitter, calcular_perdida

# ---------------------------
# CONFIGURACIÓN SERIAL
# ---------------------------
ser = serial.Serial('COM10', 115200)

# Variables globales
rtts = []
enviados_global = 0
recibidos_global = 0

# ---------------------------
# INTERFAZ TKINTER
# ---------------------------
root = tk.Tk()
root.title("Monitor de Red - ESP32")
root.geometry("400x300")

# Variables dinámicas (para actualizar labels)
rtt_var = tk.StringVar(value="Esperando datos...")
ping_var = tk.StringVar(value="---")
jitter_var = tk.StringVar(value="---")
perdida_var = tk.StringVar(value="---")

# Títulos
ttk.Label(root, text="Monitor de Red", font=("Arial", 16)).pack(pady=10)

# Campos
ttk.Label(root, text="RTT actual:").pack()
ttk.Label(root, textvariable=rtt_var, font=("Arial", 12)).pack()

ttk.Label(root, text="Ping promedio (10 muestras):").pack()
ttk.Label(root, textvariable=ping_var, font=("Arial", 12)).pack()

ttk.Label(root, text="Jitter:").pack()
ttk.Label(root, textvariable=jitter_var, font=("Arial", 12)).pack()

ttk.Label(root, text="Pérdida de paquetes:").pack()
ttk.Label(root, textvariable=perdida_var, font=("Arial", 12)).pack()

# ---------------------------
# FUNCIÓN DE LECTURA SERIAL
# ---------------------------
def leer_serial():
    global enviados_global, recibidos_global

    while True:
        linea = ser.readline().decode().strip()
        print("Serial:", linea)

        # Detectar RTT
        if "ms" in linea:
            try:
                rtt = int(linea.split()[0])
            except:
                continue

            # Actualizar RTT actual en GUI
            rtt_var.set(f"{rtt} ms")

            rtts.append(rtt)

            enviados_global += 1
            recibidos_global += 1  # debes ajustarlo realmente según tu lógica

            if len(rtts) == 10:
                ping = calcular_ping(rtts)
                jitter = calcular_jitter(rtts)
                perdida = calcular_perdida(enviados_global, recibidos_global)

                # Actualizar GUI
                ping_var.set(f"{ping:.2f} ms")
                jitter_var.set(f"{jitter:.2f} ms")
                perdida_var.set(f"{perdida:.1f} %")

                rtts.clear()

# ---------------------------
# INICIAR THREAD PARA PUERTO SERIAL
# ---------------------------
thread = threading.Thread(target=leer_serial, daemon=True)
thread.start()

root.mainloop()
