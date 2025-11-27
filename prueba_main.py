import serial
import json
from indicadores import calcular_ping, calcular_jitter, calcular_perdida

ser = serial.Serial('COM20', 115200)

rtts = []
enviados_global = 0
recibidos_global = 0

def guardar_json(ping, jitter, enviados, recibidos):
    datos = {
        "ping_promedio": ping,
        "jitter": jitter,
        "enviados": enviados,
        "recibidos": recibidos,
        "perdida": calcular_perdida(enviados, recibidos)
    }

    with open("metrics.json", "w") as f:
        json.dump(datos, f, indent=4)

while True:
    linea = ser.readline().decode().strip()
    print(linea)

    if "ms" in linea:
        partes = linea.split()
        rtt = int(partes[-2])

        rtts.append(rtt)
        enviados_global += 1
        recibidos_global += 1

        if len(rtts) == 10:
            ping = calcular_ping(rtts)
            jitter = calcular_jitter(rtts)

            print("RTTs:", rtts)
            print("Ping promedio:", ping, "ms")
            print("Jitter:", jitter, "ms")

            guardar_json(ping, jitter, enviados_global, recibidos_global)
            print("✔ Datos guardados en metrics.json")

            rtts.clear()
