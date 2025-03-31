import random
import time
#chama bibliotecas PY

ips = ["192.168.1.10", "192.168.1.15", "192.168.1.20", "200.150.10.5"]
# Lista de IPs monitorados


tentativas = {}
# Dicionário para contar tentativas por IP

limite = 5
# Limite de tentativas antes de gerar alerta

print("Monitorando tráfego de rede...\n")

while True:
    # Escolhe um IP aleatoriamente para simular um acesso
    ip = random.choice(ips)
    

    tentativas[ip] = tentativas.get(ip, 0) + 1
        # Registra a tentativa no dicionário usando um contador, iniciando com 0 se o IP for novo

    print(f"Tentativa de acesso do IP {ip} - Total: {tentativas[ip]}")
    
    if tentativas[ip] > limite:
        print(f"ALERTA: Atividade suspeita detectada do IP {ip}. Encerrando o monitoramento.")
        # Se o IP ultrapassar o limite, alerta e encerra o monitoramento

        break  
# Sai do loop imediatamente
    
    time.sleep(1) 
# Aguarda 1 segundo para simular o tempo real
