import tkinter as tk
from tkinter import ttk, messagebox
import json, os

class InterfazMetricas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métricas de Red")
        self.geometry("500x450")
        self.configure(bg="#f4f4f4")

        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="📊 Métricas registradas", 
                  font=("Arial", 18, "bold")).pack(pady=10)

        # Tabla con dos columnas
        self.tree = ttk.Treeview(frame, columns=("clave","valor"), show="headings", height=6)
        self.tree.heading("clave", text="Métrica")
        self.tree.heading("valor", text="Valor")
        self.tree.column("clave", width=200)
        self.tree.column("valor", width=150)
        self.tree.pack(expand=True, fill="both", pady=10)

        # Gauge de subida
        ttk.Label(frame, text="Velocidad de subida (Mbps)", font=("Arial", 12)).pack(pady=5)
        self.gauge_up = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
        self.gauge_up.pack(pady=5)

        # Gauge de descarga
        ttk.Label(frame, text="Velocidad de descarga (Mbps)", font=("Arial", 12)).pack(pady=5)
        self.gauge_down = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
        self.gauge_down.pack(pady=5)

        ttk.Button(frame, text="🔄 Actualizar", command=self.cargar).pack(pady=15)

        self.cargar()

    def cargar(self):
        if not os.path.exists("metricas.json"):
            messagebox.showwarning("Advertencia", "Primero ejecuta prueba_main.py")
            return

        with open("metricas.json", "r") as f:
            data = json.load(f)

        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar valores
        for key, value in data.items():
            self.tree.insert("", tk.END, values=(key, value))

        # Actualizar gauges si existen las métricas
        if "velocidad_subida_mbps" in data:
            self.gauge_up["value"] = min(data["velocidad_subida_mbps"], 100)  # escala hasta 100 Mbps
        if "velocidad_descarga_mbps" in data:
            self.gauge_down["value"] = min(data["velocidad_descarga_mbps"], 100)

if __name__ == "__main__":
    InterfazMetricas().mainloop()