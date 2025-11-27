import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class InterfazMetricas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métricas de Red")
        self.geometry("450x380")

        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="Métricas registradas", font=("Arial", 16, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(frame, columns=("valor"), show="headings")
        self.tree.heading("valor", text="Valor")
        self.tree.pack(expand=True, fill="both")

        ttk.Button(frame, text="Actualizar", command=self.cargar).pack(pady=10)

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
            self.tree.insert("", tk.END, values=(f"{key}: {value}",))


if __name__ == "__main__":
    InterfazMetricas().mainloop()
