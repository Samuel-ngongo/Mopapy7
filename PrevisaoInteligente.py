
import random
import matplotlib.pyplot as plt

historico = []

def prever_proximo_valor(historico):
    if not historico:
        return "Aguardando dados suficientes...", 50

    ultimos = historico[-10:]
    altos = [v for v in ultimos if v > 2.0]
    baixos = [v for v in ultimos if v <= 2.0]

    if len(altos) >= 5:
        return "Possível reversão: valores baixos podem aparecer", 65
    elif len(baixos) >= 5:
        return "Possível reversão: chance de valor alto em breve", 70
    elif historico[-1] > 3.0 and historico[-2] > 3.0:
        return "Alta sequência detectada: cuidado com queda", 60
    elif historico[-1] < 1.5 and historico[-2] < 1.5:
        return "Sequência baixa detectada: possível subida", 55

    media = sum(ultimos) / len(ultimos)
    if media > 2.5:
        return "Tendência geral: Alta", 60
    elif media < 1.8:
        return "Tendência geral: Baixa", 60
    else:
        return "Tendência média: Análise neutra", 50

def adicionar_valor(valor):
    historico.append(valor)
    mensagem, confianca = prever_proximo_valor(historico)
    print(f"Valor: {valor} | {mensagem} | Confianca: {confianca}%")
    return mensagem, confianca

# Exemplo de uso (simulação)
for _ in range(30):
    valor_simulado = round(random.uniform(1.0, 5.0), 2)
    adicionar_valor(valor_simulado)

# Gráfico
plt.plot(historico, marker='o', linestyle='-', color='blue')
plt.axhline(y=2.0, color='red', linestyle='--', label='Limite de análise')
plt.title("Histórico de Valores")
plt.xlabel("Rodadas")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.show()
