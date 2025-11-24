
import serial
from indicadores import calcular_ping, calcular_jitter, calcular_perdida

ser = serial.Serial('COM10', 115200)

rtts = []
enviados_global = 0
recibidos_global = 0

while True:
    linea = ser.readline().decode().strip()
    print(linea)

    # Leer acumulados enviados y recibidos
    if "Enviados_global:" in linea:
        enviados_global = int(linea.split(":")[1].strip())
    elif "Recibidos_global:" in linea:
        recibidos_global = int(linea.split(":")[1].strip())

    # Leer RTT promedio
    if "ms" in linea:
        rtt = int(linea.split()[0])
        rtts.append(rtt)

        if len(rtts) == 10:  # cada 10 bloques

            print("RTTs individuales:")
            for i, valor in enumerate(rtts, start=1):
                print(f"RTT {i}: {valor} ms")

            #Luego calcular y mostrar los indicadores
            print("Ping promedio:", calcular_ping(rtts), "ms")
            print("Jitter:", calcular_jitter(rtts), "ms")
            print("Pérdida global:", calcular_perdida(enviados_global, recibidos_global), "%")

            # Reiniciar para el siguiente ciclo
            rtts.clear()
            enviados_global = 0
            recibidos_global = 0