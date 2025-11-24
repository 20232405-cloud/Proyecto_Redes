
# Instala primero las librerías necesarias:
# pip install gspread oauth2client

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. Definir el alcance (scope) de acceso
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# 2. Cargar credenciales desde tu archivo JSON
# Cambia "credenciales.json" por el nombre real de tu archivo descargado
creds = ServiceAccountCredentials.from_json_keyfile_name("medicionesred.json", scope)

# 3. Autorizar cliente
client = gspread.authorize(creds)

# 4. Abrir tu hoja de cálculo
# Usa el nombre exacto de tu Google Sheet (ejemplo: "REDES_MEDICION DE RED")
sheet = client.open("REDES_MEDICION DE RED").sheet1

# 5. Escribir datos en la hoja
# Cada lista es una fila nueva
sheet.append_row(["Ubicación", "RSSI", "Ping", "Jitter", " % Pérdida", "Descarga", "Subida", "QoE"])

# Ejemplo de insertar valores reales
sheet.append_row(["Laboratorio", -65, 45, 5, "2%", 50.3, 10.2, 85])