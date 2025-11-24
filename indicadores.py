

def calcular_ping(rtts):
    if not rtts:
        return 0
    return sum(rtts) / len(rtts)

def calcular_jitter(rtts):
    if len(rtts) < 2:
        return 0
    difs = [abs(rtts[i] - rtts[i-1]) for i in range(1, len(rtts))]
    return sum(difs) / len(difs)

def calcular_perdida(enviados, recibidos):
    if enviados == 0:
        return 0
    return (enviados - recibidos) * 100 / enviados

