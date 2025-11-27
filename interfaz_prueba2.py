import tkinter as tk
import json
import os

def leer_json():
    if not os.path.exists("metrics.json"):
        return {
            "ping_promedio": 0,
            "jitter": 0,
            "enviados": 0,
            "recibidos": 0,
            "perdida": 0
        }

    with open("metrics.json", "r") as f:
        return json.load(f)

def actualizar_datos():
    datos = leer_json()

    lbl_ping.config(text=f"{datos['ping_promedio']} ms")
    lbl_jitter.config(text=f"{datos['jitter']} ms")
    lbl_enviados.config(text=f"{datos['enviados']}")
    lbl_recibidos.config(text=f"{datos['recibidos']}")
    lbl_perdida.config(text=f"{datos['perdida']} %")

    ventana.after(1000, actualizar_datos)  # refrescar cada segundo

# Ventana
ventana = tk.Tk()
ventana.title("Monitor de Red - ESP32")
ventana.geometry("350x250")

tk.Label(ventana, text="Ping promedio:", font=("Arial", 12)).pack()
lbl_ping = tk.Label(ventana, text="---", font=("Arial", 14))
lbl_ping.pack()

tk.Label(ventana, text="Jitter:", font=("Arial", 12)).pack()
lbl_jitter = tk.Label(ventana, text="---", font=("Arial", 14))
lbl_jitter.pack()

tk.Label(ventana, text="Paquetes enviados:", font=("Arial", 12)).pack()
lbl_enviados = tk.Label(ventana, text="---", font=("Arial", 14))
lbl_enviados.pack()

tk.Label(ventana, text="Paquetes recibidos:", font=("Arial", 12)).pack()
lbl_recibidos = tk.Label(ventana, text="---", font=("Arial", 14))
lbl_recibidos.pack()

tk.Label(ventana, text="Pérdida:", font=("Arial", 12)).pack()
lbl_perdida = tk.Label(ventana, text="---", font=("Arial", 14))
lbl_perdida.pack()

actualizar_datos()
ventana.mainloop()
