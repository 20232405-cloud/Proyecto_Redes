
import socket, time

HOST = "10.143.181.227"  # IP del ESP32 (la que imprime en Serial)
PORT = 8080

# --- SUBIDA: enviar datos al ESP32 ---
data = b"A" * 1000000  # 1 MB

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("📤 Enviando datos al ESP32...")
start = time.time()
s.sendall(data)
end = time.time()

tiempo = end - start
velocidad_mbps = (len(data) * 8) / (tiempo * 1e6)
print(f"Velocidad de subida: {velocidad_mbps:.2f} Mbps")

# --- DESCARGA: recibir datos desde ESP32 ---
print("📥 Recibiendo datos desde ESP32...")
start = time.time()
recibidos = 0
while recibidos < len(data):
    chunk = s.recv(4096)
    if not chunk:
        break
    recibidos += len(chunk)
end = time.time()

tiempo = end - start
velocidad_mbps = (recibidos * 8) / (tiempo * 1e6)
print(f"Velocidad de descarga: {velocidad_mbps:.2f} Mbps")

s.close()